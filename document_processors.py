"""
Document Type Processors - Pre-configured TextProcessor instances for different document types
This module provides specialized processors for various content domains
"""

from custom_stopwords import CustomStopwords
from text_processor import TextProcessor


class DocumentTypeProcessors:
    """Factory for creating specialized TextProcessor instances for different document types"""

    @staticmethod
    def create_technical_processor():
        """
        Create processor for technical documentation, code comments, and API docs.
        Filters out technical jargon common in these documents.
        """
        stopwords = CustomStopwords(language="english", storage_path="custom_stopwords.json")
        # Load technical domain stopwords if available
        processor = TextProcessor(stopwords_plugin=stopwords)
        return processor

    @staticmethod
    def create_web_content_processor():
        """
        Create processor for web content, articles, and blog posts.
        Removes common web-related stopwords.
        """
        stopwords = CustomStopwords(language="english", storage_path="custom_stopwords.json")
        # Add additional web-specific terms
        web_terms = ["html", "css", "javascript", "browser", "page", "link", "button", "form"]
        stopwords.add(web_terms)
        processor = TextProcessor(stopwords_plugin=stopwords)
        return processor

    @staticmethod
    def create_business_processor():
        """
        Create processor for business documents, reports, and proposals.
        Filters business-specific terminology.
        """
        stopwords = CustomStopwords(language="english", storage_path="custom_stopwords.json")
        # Add business-specific terms
        business_terms = ["company", "business", "market", "customer", "product", "revenue", "profit"]
        stopwords.add(business_terms)
        processor = TextProcessor(stopwords_plugin=stopwords)
        return processor

    @staticmethod
    def create_academic_processor():
        """
        Create processor for academic papers and research documents.
        """
        stopwords = CustomStopwords(language="english", storage_path="custom_stopwords.json")
        # Add academic-specific terms
        academic_terms = ["abstract", "introduction", "conclusion", "method", "result", "study", "research", "paper", "author"]
        stopwords.add(academic_terms)
        processor = TextProcessor(stopwords_plugin=stopwords)
        return processor

    @staticmethod
    def create_news_processor():
        """
        Create processor for news articles and journalistic content.
        """
        stopwords = CustomStopwords(language="english", storage_path="custom_stopwords.json")
        # Add news-specific terms
        news_terms = ["said", "says", "reported", "according", "news", "article", "story", "source", "today"]
        stopwords.add(news_terms)
        processor = TextProcessor(stopwords_plugin=stopwords)
        return processor


class ProcessorRegistry:
    """Registry of available document type processors"""

    _processors = {
        "technical": DocumentTypeProcessors.create_technical_processor,
        "web": DocumentTypeProcessors.create_web_content_processor,
        "business": DocumentTypeProcessors.create_business_processor,
        "academic": DocumentTypeProcessors.create_academic_processor,
        "news": DocumentTypeProcessors.create_news_processor,
    }

    @classmethod
    def get_processor(cls, doc_type: str):
        """
        Get a processor for the specified document type.
        
        Args:
            doc_type: Type of document ('technical', 'web', 'business', 'academic', 'news')
        
        Returns:
            Configured TextProcessor instance
        
        Raises:
            ValueError: If document type is not recognized
        """
        if doc_type not in cls._processors:
            available = ", ".join(cls._processors.keys())
            raise ValueError(f"Unknown document type '{doc_type}'. Available: {available}")
        
        return cls._processors[doc_type]()

    @classmethod
    def list_types(cls):
        """Get list of available document types"""
        return list(cls._processors.keys())

    @classmethod
    def register_processor(cls, doc_type: str, processor_factory):
        """
        Register a custom document type processor.
        
        Args:
            doc_type: Name of the document type
            processor_factory: Callable that returns a TextProcessor instance
        """
        cls._processors[doc_type] = processor_factory
