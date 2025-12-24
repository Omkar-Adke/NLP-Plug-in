"""
Text Processing Module - Uses the CustomStopwords plugin
Handles processing of text files with custom stopword filtering
"""

import os
from typing import List, Dict
from custom_stopwords import CustomStopwords, preprocess


class TextProcessor:
    """
    Main processor for handling text files with custom stopword filtering.
    Uses CustomStopwords plugin for stopword management.
    """

    def __init__(self, stopwords_plugin: CustomStopwords = None):
        """
        Initialize TextProcessor with optional custom stopwords plugin.
        
        Args:
            stopwords_plugin: CustomStopwords instance (creates default if None)
        """
        self.stopwords_plugin = stopwords_plugin or CustomStopwords()

    def process_file(self, file_path: str, remove_stopwords: bool = True) -> Dict:
        """
        Process a text file and remove/filter stopwords.
        
        Args:
            file_path: Path to the text file
            remove_stopwords: Whether to filter stopwords
        
        Returns:
            Dictionary with original text, tokens, and statistics
        
        Raises:
            FileNotFoundError: If file doesn't exist
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"File not found: {file_path}")

        with open(file_path, "r", encoding="utf-8") as f:
            text = f.read()

        tokens = preprocess(text, self.stopwords_plugin, remove_stopwords)
        
        return {
            "file": file_path,
            "original_text": text,
            "tokens": tokens,
            "token_count": len(tokens),
            "unique_tokens": len(set(tokens)),
            "remove_stopwords": remove_stopwords
        }

    def process_directory(self, directory: str, pattern: str = "*.txt", 
                         remove_stopwords: bool = True) -> List[Dict]:
        """
        Process all text files in a directory.
        
        Args:
            directory: Path to directory
            pattern: File pattern to match (default: "*.txt")
            remove_stopwords: Whether to filter stopwords
        
        Returns:
            List of processing results for each file
        """
        import glob
        
        results = []
        files = glob.glob(os.path.join(directory, pattern))
        
        for file_path in files:
            try:
                result = self.process_file(file_path, remove_stopwords)
                results.append(result)
            except Exception as e:
                results.append({
                    "file": file_path,
                    "error": str(e)
                })
        
        return results

    def get_word_frequency(self, file_path: str, top_n: int = 10, 
                          remove_stopwords: bool = True) -> List[tuple]:
        """
        Get most frequent words in a file.
        
        Args:
            file_path: Path to text file
            top_n: Number of top words to return
            remove_stopwords: Whether to filter stopwords
        
        Returns:
            List of (word, frequency) tuples
        """
        from collections import Counter
        
        result = self.process_file(file_path, remove_stopwords)
        word_counts = Counter(result["tokens"])
        
        return word_counts.most_common(top_n)

    def add_custom_stopwords(self, words: List[str]) -> None:
        """Add custom stopwords via the plugin."""
        self.stopwords_plugin.add(words)

    def remove_custom_stopwords(self, words: List[str]) -> None:
        """Remove custom stopwords via the plugin."""
        self.stopwords_plugin.remove(words)

    def get_stopwords_stats(self) -> Dict:
        """Get statistics about stopwords."""
        all_stopwords = self.stopwords_plugin.get_all()
        custom_stopwords = self.stopwords_plugin.custom_stopwords
        
        return {
            "total_stopwords": len(all_stopwords),
            "base_stopwords": len(self.stopwords_plugin.base_stopwords),
            "custom_stopwords": len(custom_stopwords),
            "custom_words_list": sorted(list(custom_stopwords))
        }
