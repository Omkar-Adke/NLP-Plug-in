#!/usr/bin/env python3
"""
Quick Start Guide for NLP-Plug-in
Run this file to get started with the CustomStopwords plugin
"""

from custom_stopwords import CustomStopwords, preprocess
from text_processor import TextProcessor


def main():
    print("\n" + "="*60)
    print("NLP-Plug-in: Quick Start Guide")
    print("="*60 + "\n")
    
    # ===== STEP 1: Basic Initialization =====
    print("STEP 1: Initialize the Plugin")
    print("-" * 60)
    stopwords = CustomStopwords()
    print("✓ CustomStopwords plugin initialized")
    print(f"  - Language: English")
    print(f"  - Base stopwords: {len(stopwords.base_stopwords)}")
    print()
    
    # ===== STEP 2: Add Custom Stopwords =====
    print("STEP 2: Add Custom Stopwords")
    print("-" * 60)
    custom_words = ["api", "client", "request"]
    stopwords.add(custom_words)
    print(f"✓ Added custom stopwords: {', '.join(custom_words)}")
    stats = stopwords.get_all()
    print(f"  - Total stopwords now: {len(stats)}")
    print()
    
    # ===== STEP 3: Check Stopwords =====
    print("STEP 3: Check if Words are Stopwords")
    print("-" * 60)
    test_words = ["the", "api", "python", "request"]
    for word in test_words:
        is_stop = stopwords.is_stopword(word)
        status = "✓ stopword" if is_stop else "✗ not stopword"
        print(f"  '{word}': {status}")
    print()
    
    # ===== STEP 4: Text Processing =====
    print("STEP 4: Process Text")
    print("-" * 60)
    text = "The API client makes a request to the server"
    print(f"Original: {text}")
    
    tokens = preprocess(text, stopwords, remove_stopwords=True)
    print(f"Processed (stopwords removed): {tokens}")
    
    tokens_with_stops = preprocess(text, stopwords, remove_stopwords=False)
    print(f"All tokens: {tokens_with_stops}")
    print()
    
    # ===== STEP 5: File Processing =====
    print("STEP 5: Process Text Files")
    print("-" * 60)
    processor = TextProcessor(stopwords)
    
    # Create sample file
    sample_file = "sample.txt"
    with open(sample_file, "w") as f:
        f.write("The API client sends requests to the server")
    
    result = processor.process_file(sample_file)
    print(f"File: {result['file']}")
    print(f"Token count: {result['token_count']}")
    print(f"Unique tokens: {result['unique_tokens']}")
    print(f"Tokens: {result['tokens']}")
    
    # Cleanup
    import os
    os.remove(sample_file)
    print()
    
    # ===== STEP 6: Word Frequency =====
    print("STEP 6: Analyze Word Frequency")
    print("-" * 60)
    sample_file = "frequency_sample.txt"
    with open(sample_file, "w") as f:
        f.write("""
        The server processes requests from clients.
        Each request is handled by the server.
        API requests are important for the system.
        Clients communicate with the server via API.
        """)
    
    freq = processor.get_word_frequency(sample_file, top_n=5)
    print("Top 5 most frequent words:")
    for word, count in freq:
        print(f"  {word}: {count}")
    
    os.remove(sample_file)
    print()
    
    # ===== Summary =====
    print("="*60)
    print("✓ Quick Start Complete!")
    print("="*60)
    print("\nNext Steps:")
    print("  1. Edit custom_stopwords.json to persist custom stopwords")
    print("  2. Create text_processor instances for different document types")
    print("  3. Integrate into your NLP pipeline")
    print("  4. Run 'python example.py' for more detailed examples")
    print()


if __name__ == "__main__":
    main()
