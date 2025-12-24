import json
import os
import re
from nltk.corpus import stopwords
from typing import List, Set, Union


class CustomStopwords:
    """
    Plugin for managing custom stopwords in NLTK.
    Allows adding, removing, and checking stopwords for text processing.
    """

    def __init__(self, language: str = "english", storage_path: str = "custom_stopwords.json"):
        """
        Initialize the CustomStopwords plugin.
        
        Args:
            language: Language for stopwords (default: "english")
            storage_path: Path to JSON file storing custom stopwords
        """
        self.language = language
        self.storage_path = storage_path

        if not os.path.exists(self.storage_path):
            self._initialize_storage()

        self._load_custom_stopwords()

    def _initialize_storage(self):
        """Initialize empty storage file."""
        with open(self.storage_path, "w") as f:
            json.dump({}, f)

    def _load_custom_stopwords(self):
        """Load custom and base stopwords from storage and NLTK."""
        with open(self.storage_path, "r") as f:
            data = json.load(f)

        self.custom_stopwords: Set[str] = set(data.get(self.language, []))
        self.base_stopwords: Set[str] = set(stopwords.words(self.language))

    def add(self, words: Union[str, List[str]]) -> None:
        """
        Add custom stopwords.
        
        Args:
            words: Single word (str) or list of words to add
        """
        if isinstance(words, str):
            words = [words]

        self.custom_stopwords.update(word.lower() for word in words)
        self._save()

    def remove(self, words: Union[str, List[str]]) -> None:
        """
        Remove custom stopwords.
        
        Args:
            words: Single word (str) or list of words to remove
        """
        if isinstance(words, str):
            words = [words]

        for word in words:
            self.custom_stopwords.discard(word.lower())

        self._save()

    def get_all(self) -> Set[str]:
        """Get all stopwords (base + custom)."""
        return self.base_stopwords.union(self.custom_stopwords)

    def is_stopword(self, word: str) -> bool:
        """Check if a word is a stopword."""
        return word.lower() in self.get_all()

    def _save(self) -> None:
        """Save custom stopwords to storage file."""
        with open(self.storage_path, "r") as f:
            data = json.load(f)

        data[self.language] = sorted(self.custom_stopwords)

        with open(self.storage_path, "w") as f:
            json.dump(data, f, indent=4)


def preprocess(text: str, stopwords_plugin: CustomStopwords, remove_stopwords: bool = True) -> List[str]:
    """
    Preprocess text by tokenizing and optionally removing stopwords.
    
    Args:
        text: Input text to process
        stopwords_plugin: CustomStopwords plugin instance
        remove_stopwords: Whether to remove stopwords (default: True)
    
    Returns:
        List of processed tokens
    """
    # Convert to lowercase and split into words
    words = re.findall(r'\b\w+\b', text.lower())
    
    if remove_stopwords:
        return [word for word in words if not stopwords_plugin.is_stopword(word)]
    
    return words
