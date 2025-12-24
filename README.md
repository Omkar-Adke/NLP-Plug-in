# NLP-Plug-in: Custom Stopwords Plugin

A lightweight, flexible plugin system for managing custom stopwords in NLTK. Easily add domain-specific stopwords to your text processing pipeline and process text files with advanced filtering capabilities.

## Features

✨ **Core Features:**
- Add/remove custom stopwords dynamically
- Persistent storage in JSON format
- Integration with NLTK stopwords
- Text preprocessing with stopword filtering
- File processing capabilities
- Word frequency analysis
- Multi-language support

## Installation

### Requirements
- Python 3.7+
- NLTK library

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Omkar-Adke/NLP-Plug-in.git
   cd NLP-Plug-in
   ```

2. **Install dependencies:**
   ```bash
   pip install nltk
   ```

3. **Download NLTK stopwords (first time only):**
   ```bash
   python -c "import nltk; nltk.download('stopwords')"
   ```

## Quick Start

### Basic Usage

```python
from custom_stopwords import CustomStopwords

# Initialize the plugin
stopwords = CustomStopwords()

# Add custom stopwords
stopwords.add("api")
stopwords.add(["client", "request", "server"])

# Check if a word is a stopword
if stopwords.is_stopword("api"):
    print("'api' is a stopword")

# Get all stopwords
all_stopwords = stopwords.get_all()

# Remove a stopword
stopwords.remove("api")
```

### Text Processing

```python
from custom_stopwords import CustomStopwords, preprocess
from text_processor import TextProcessor

# Create processor with custom stopwords
processor = TextProcessor()
processor.add_custom_stopwords(["api", "client", "request"])

# Process text
text = "The API client sends a request to the server"
tokens = preprocess(text, processor.stopwords_plugin, remove_stopwords=True)
print(tokens)
```

### File Processing

```python
from text_processor import TextProcessor

processor = TextProcessor()

# Process a single file
result = processor.process_file("document.txt", remove_stopwords=True)
print(f"Tokens: {result['tokens']}")
print(f"Token count: {result['token_count']}")

# Get word frequency
freq = processor.get_word_frequency("document.txt", top_n=10)
for word, count in freq:
    print(f"{word}: {count}")

# Process all files in a directory
results = processor.process_directory("./documents", pattern="*.txt")
```

## API Reference

### CustomStopwords Class

**`__init__(language="english", storage_path="custom_stopwords.json")`**
- Initializes the plugin
- Parameters:
  - `language`: Language code (default: "english")
  - `storage_path`: JSON file location for custom stopwords

**`add(words)`**
- Add custom stopword(s)

**`remove(words)`**
- Remove custom stopword(s)

**`get_all()`**
- Returns: Set of all stopwords (base + custom)

**`is_stopword(word)`**
- Check if word is in stopwords

### TextProcessor Class

**`process_file(file_path, remove_stopwords=True)`**
- Process a single text file

**`process_directory(directory, pattern="*.txt", remove_stopwords=True)`**
- Process all matching files in directory

**`get_word_frequency(file_path, top_n=10, remove_stopwords=True)`**
- Get most frequent words

## Running the Examples

Execute the included example script:

```bash
python example.py
```

This will demonstrate:
1. Basic stopword management
2. Text preprocessing
3. File processing with statistics

## File Structure

```
NLP-Plug-in/
├── custom_stopwords.py      # Main plugin with CustomStopwords class
├── custom_stopwords.json    # Persistent storage for custom stopwords
├── text_processor.py        # TextProcessor for file handling
├── example.py              # Usage examples
└── README.md               # This file
```

## Use Cases

- **Web Scraping**: Remove domain-specific stopwords from web content
- **Document Analysis**: Extract relevant terms from technical documents
- **Text Mining**: Preprocess text with custom filtering rules
- **NLP Pipelines**: Integrate as preprocessing step in ML workflows
- **Search/Indexing**: Filter irrelevant terms before indexing
- **Content Analysis**: Analyze text while excluding domain-specific words

## Troubleshooting

**Q: NLTK stopwords not found?**
```bash
python -c "import nltk; nltk.download('stopwords')"
```

## License

MIT License

## Author

Omkar Adke
