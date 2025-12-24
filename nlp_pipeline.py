"""
NLP Pipeline - End-to-end text processing pipeline with multiple document types
Integrates CustomStopwords and TextProcessor for comprehensive text analysis
"""

from typing import Dict, List, Tuple, Optional
from pathlib import Path
from custom_stopwords import CustomStopwords
from text_processor import TextProcessor
from document_processors import ProcessorRegistry


class NLPPipeline:
    """
    Comprehensive NLP pipeline for processing text documents.
    Supports multiple document types with specialized stopword filtering.
    """

    def __init__(self, default_type: str = "technical"):
        """
        Initialize the NLP pipeline.
        
        Args:
            default_type: Default document type for processing
        """
        self.default_type = default_type
        self.processors: Dict[str, TextProcessor] = {}
        self.results: List[Dict] = []

    def get_processor(self, doc_type: str) -> TextProcessor:
        """
        Get or create a processor for the specified document type.
        
        Args:
            doc_type: Type of document to process
        
        Returns:
            TextProcessor instance for the document type
        """
        if doc_type not in self.processors:
            self.processors[doc_type] = ProcessorRegistry.get_processor(doc_type)
        return self.processors[doc_type]

    def process_text(self, text: str, doc_type: Optional[str] = None, 
                    get_frequency: bool = False, top_n: int = 10) -> Dict:
        """
        Process a single text string.
        
        Args:
            text: Text to process
            doc_type: Document type (uses default if None)
            get_frequency: Whether to compute word frequency
            top_n: Number of top words for frequency analysis
        
        Returns:
            Dictionary with processing results
        """
        doc_type = doc_type or self.default_type
        processor = self.get_processor(doc_type)
        
        from custom_stopwords import preprocess
        
        tokens = preprocess(text, processor.stopwords_plugin, remove_stopwords=True)
        
        result = {
            "type": doc_type,
            "original_length": len(text),
            "token_count": len(tokens),
            "unique_tokens": len(set(tokens)),
            "tokens": tokens,
            "reduction_percent": round((1 - len(tokens) / len(text.split())) * 100, 2) if text.split() else 0
        }
        
        if get_frequency:
            from collections import Counter
            freq = Counter(tokens)
            result["top_words"] = freq.most_common(top_n)
        
        self.results.append(result)
        return result

    def process_file(self, file_path: str, doc_type: Optional[str] = None,
                    get_frequency: bool = False, top_n: int = 10) -> Dict:
        """
        Process a single file.
        
        Args:
            file_path: Path to text file
            doc_type: Document type (uses default if None)
            get_frequency: Whether to compute word frequency
            top_n: Number of top words for frequency analysis
        
        Returns:
            Dictionary with processing results
        """
        doc_type = doc_type or self.default_type
        processor = self.get_processor(doc_type)
        
        try:
            with open(file_path, "r", encoding="utf-8") as f:
                text = f.read()
            
            result = self.process_text(text, doc_type, get_frequency, top_n)
            result["file"] = file_path
            
            return result
        
        except FileNotFoundError:
            return {"file": file_path, "error": "File not found"}
        except Exception as e:
            return {"file": file_path, "error": str(e)}

    def process_directory(self, directory: str, pattern: str = "*.txt",
                         doc_type: Optional[str] = None,
                         get_frequency: bool = False) -> List[Dict]:
        """
        Process all files matching pattern in a directory.
        
        Args:
            directory: Path to directory
            pattern: File pattern (default: "*.txt")
            doc_type: Document type for all files
            get_frequency: Whether to compute word frequency
        
        Returns:
            List of results for each processed file
        """
        doc_type = doc_type or self.default_type
        directory_path = Path(directory)
        results = []
        
        for file_path in directory_path.glob(pattern):
            if file_path.is_file():
                result = self.process_file(str(file_path), doc_type, get_frequency)
                results.append(result)
        
        return results

    def process_batch(self, texts: List[Tuple[str, str]]) -> List[Dict]:
        """
        Process multiple texts with potentially different types.
        
        Args:
            texts: List of (text, doc_type) tuples
        
        Returns:
            List of processing results
        """
        results = []
        for text, doc_type in texts:
            result = self.process_text(text, doc_type)
            results.append(result)
        return results

    def get_pipeline_stats(self) -> Dict:
        """
        Get statistics about the pipeline processing.
        
        Returns:
            Dictionary with pipeline statistics
        """
        if not self.results:
            return {"message": "No results yet"}
        
        total_tokens = sum(r.get("token_count", 0) for r in self.results)
        total_unique = sum(r.get("unique_tokens", 0) for r in self.results)
        
        return {
            "total_documents": len(self.results),
            "total_tokens": total_tokens,
            "total_unique_tokens": total_unique,
            "avg_tokens_per_doc": round(total_tokens / len(self.results), 2),
            "document_types": list(set(r.get("type") for r in self.results if "type" in r))
        }

    def reset(self):
        """Clear all results from the pipeline"""
        self.results = []

    def available_document_types(self) -> List[str]:
        """Get list of available document types"""
        return ProcessorRegistry.list_types()
