"""
Example usage of the CustomStopwords Plugin with TextProcessor
Demonstrates how to use the NLP plugin for text file processing
"""

from custom_stopwords import CustomStopwords, preprocess
from text_processor import TextProcessor


def example_basic_usage():
    """Example 1: Basic stopwords management"""
    print("=" * 60)
    print("EXAMPLE 1: Basic Stopwords Management")
    print("=" * 60)
    
    # Initialize the plugin
    stopwords = CustomStopwords()
    
    # Add custom stopwords
    stopwords.add(["api", "client", "request", "server"])
    print(f"✓ Added custom stopwords: api, client, request, server")
    
    # Check if words are stopwords
    test_words = ["the", "and", "api", "hello"]
    for word in test_words:
        is_stop = stopwords.is_stopword(word)
        print(f"  '{word}' is stopword: {is_stop}")
    
    # Get statistics
    stats = stopwords.get_all()
    print(f"\n✓ Total stopwords: {len(stats)}")
    print()


def example_text_processing():
    """Example 2: Process text with stopword filtering"""
    print("=" * 60)
    print("EXAMPLE 2: Text Processing with Stopword Filtering")
    print("=" * 60)
    
    # Initialize processor
    processor = TextProcessor()
    
    # Add custom domain-specific stopwords
    processor.add_custom_stopwords(["api", "client", "request"])
    print("✓ Added domain-specific stopwords")
    
    # Sample text
    sample_text = """
    The API client sends a request to the server.
    The request contains important data and parameters.
    The server processes the request and returns a response.
    """
    
    # Process text
    tokens = preprocess(sample_text, processor.stopwords_plugin, remove_stopwords=True)
    tokens_with_stopwords = preprocess(sample_text, processor.stopwords_plugin, 
                                       remove_stopwords=False)
    
    print(f"\nOriginal text length: {len(sample_text)} characters")
    print(f"Tokens (stopwords removed): {len(tokens)} words")
    print(f"  → {tokens}")
    print(f"\nTokens (with stopwords): {len(tokens_with_stopwords)} words")
    print(f"  → {tokens_with_stopwords}")
    print()


def example_file_processing():
    """Example 3: Process a file"""
    print("=" * 60)
    print("EXAMPLE 3: File Processing")
    print("=" * 60)
    
    processor = TextProcessor()
    processor.add_custom_stopwords(["api", "client", "request", "server"])
    
    # Create a sample file
    sample_file = "sample_text.txt"
    sample_content = """
    The API client sends a request to the server.
    The server processes the request and returns a response.
    Data processing is essential for all requests.
    """
    
    with open(sample_file, "w") as f:
        f.write(sample_content)
    
    print(f"✓ Created sample file: {sample_file}")
    
    # Process the file
    result = processor.process_file(sample_file, remove_stopwords=True)
    
    print(f"\nFile: {result['file']}")
    print(f"Total tokens: {result['token_count']}")
    print(f"Unique tokens: {result['unique_tokens']}")
    print(f"Tokens: {result['tokens']}")
    
    # Get word frequency
    freq = processor.get_word_frequency(sample_file, top_n=5)
    print(f"\nTop 5 most frequent words:")
    for word, count in freq:
        print(f"  {word}: {count}")
    
    # Show stopwords stats
    stats = processor.get_stopwords_stats()
    print(f"\nStopwords Statistics:")
    print(f"  Total stopwords: {stats['total_stopwords']}")
    print(f"  Base stopwords: {stats['base_stopwords']}")
    print(f"  Custom stopwords: {stats['custom_stopwords']}")
    print(f"  Custom words: {stats['custom_words_list']}")
    
    # Cleanup
    import os
    os.remove(sample_file)
    print(f"\n✓ Cleaned up sample file")
    print()


def main():
    """Run all examples"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║   NLP PLUGIN: Custom Stopwords for Text Processing         ║")
    print("║   Examples and Usage Guide                                 ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print("\n")
    
    try:
        example_basic_usage()
        example_text_processing()
        example_file_processing()
        
        print("=" * 60)
        print("✓ All examples completed successfully!")
        print("=" * 60)
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
