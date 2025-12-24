"""
Pipeline Integration Example - Demonstrates the complete NLP pipeline with multiple document types
"""

from nlp_pipeline import NLPPipeline
from document_processors import ProcessorRegistry


def example_basic_pipeline():
    """Example 1: Basic pipeline with default processor"""
    print("\n" + "="*60)
    print("EXAMPLE 1: Basic NLP Pipeline")
    print("="*60 + "\n")
    
    pipeline = NLPPipeline(default_type="technical")
    
    # Sample technical text
    tech_text = """
    The API framework provides methods to handle client requests.
    The server processes queries using the database module.
    Function parameters control the response behavior.
    """
    
    result = pipeline.process_text(tech_text, get_frequency=True, top_n=5)
    
    print(f"Document Type: {result['type']}")
    print(f"Original length: {result['original_length']} characters")
    print(f"Tokens (after filtering): {result['token_count']}")
    print(f"Unique tokens: {result['unique_tokens']}")
    print(f"Reduction: {result['reduction_percent']}%")
    print(f"Tokens: {result['tokens']}")
    print(f"\nTop 5 words: {result.get('top_words', [])}")
    print()


def example_multi_type_pipeline():
    """Example 2: Pipeline with different document types"""
    print("="*60)
    print("EXAMPLE 2: Multi-Type Document Processing")
    print("="*60 + "\n")
    
    pipeline = NLPPipeline()
    
    # Technical document
    tech_text = """
    The API client sends HTTP requests to the server endpoint.
    The server responds with JSON data containing the query results.
    """
    
    # Business document
    business_text = """
    The company's business strategy focuses on market expansion.
    Our product sales revenue increased by improving customer service.
    """
    
    # Web content
    web_text = """
    The website has a clean design with HTML forms and JavaScript validation.
    The user can click buttons to submit the page and navigate between links.
    """
    
    # Process with different types
    tech_result = pipeline.process_text(tech_text, doc_type="technical", get_frequency=True, top_n=3)
    business_result = pipeline.process_text(business_text, doc_type="business", get_frequency=True, top_n=3)
    web_result = pipeline.process_text(web_text, doc_type="web", get_frequency=True, top_n=3)
    
    print("Technical Document:")
    print(f"  Tokens: {tech_result['token_count']} | Unique: {tech_result['unique_tokens']}")
    print(f"  Top words: {tech_result.get('top_words', [])}")
    
    print("\nBusiness Document:")
    print(f"  Tokens: {business_result['token_count']} | Unique: {business_result['unique_tokens']}")
    print(f"  Top words: {business_result.get('top_words', [])}")
    
    print("\nWeb Content Document:")
    print(f"  Tokens: {web_result['token_count']} | Unique: {web_result['unique_tokens']}")
    print(f"  Top words: {web_result.get('top_words', [])}")
    
    print("\n" + "Pipeline Statistics:")
    stats = pipeline.get_pipeline_stats()
    print(f"  Total documents: {stats['total_documents']}")
    print(f"  Total tokens: {stats['total_tokens']}")
    print(f"  Average tokens per doc: {stats['avg_tokens_per_doc']}")
    print(f"  Document types processed: {stats['document_types']}")
    print()


def example_batch_processing():
    """Example 3: Batch processing with mixed document types"""
    print("="*60)
    print("EXAMPLE 3: Batch Processing Pipeline")
    print("="*60 + "\n")
    
    pipeline = NLPPipeline()
    
    # Create batch of texts with their types
    batch_data = [
        ("The API method handles client requests efficiently", "technical"),
        ("Our business strategy targets new market opportunities", "business"),
        ("Click the button to navigate the web page", "web"),
        ("The research study analyzes academic methodology and results", "academic"),
        ("The news reported that the company announced new product sales", "news"),
    ]
    
    results = pipeline.process_batch(batch_data)
    
    print("Batch Processing Results:\n")
    for i, result in enumerate(results, 1):
        text_preview = batch_data[i-1][0][:40] + "..."
        print(f"{i}. Type: {result['type']:10} | Tokens: {result['token_count']:2} | {text_preview}")
    
    stats = pipeline.get_pipeline_stats()
    print(f"\nTotal Processed: {stats['total_documents']} documents")
    print(f"Total Tokens: {stats['total_tokens']}")
    print()


def example_available_types():
    """Example 4: Show available document types"""
    print("="*60)
    print("EXAMPLE 4: Available Document Types")
    print("="*60 + "\n")
    
    pipeline = NLPPipeline()
    available_types = pipeline.available_document_types()
    
    print("Available document types:")
    for doc_type in available_types:
        print(f"  ✓ {doc_type}")
    
    print("\nEach type comes with pre-configured stopwords for optimal filtering.")
    print()


def example_file_processing_pipeline():
    """Example 5: Pipeline file processing"""
    print("="*60)
    print("EXAMPLE 5: File Processing Pipeline")
    print("="*60 + "\n")
    
    # Create sample files
    files = {
        "technical_doc.txt": "The API client sends requests to the server using HTTP protocol",
        "business_doc.txt": "Our business strategy focuses on customer product service and revenue growth",
        "web_content.txt": "The website uses HTML CSS and JavaScript for interactive web pages",
    }
    
    # Create files
    for filename, content in files.items():
        with open(filename, "w") as f:
            f.write(content)
        print(f"✓ Created {filename}")
    
    # Process with pipeline
    pipeline = NLPPipeline()
    
    print("\nProcessing technical document...")
    tech_result = pipeline.process_file("technical_doc.txt", doc_type="technical")
    print(f"  Tokens: {tech_result['token_count']} | Unique: {tech_result['unique_tokens']}")
    
    print("Processing business document...")
    bus_result = pipeline.process_file("business_doc.txt", doc_type="business")
    print(f"  Tokens: {bus_result['token_count']} | Unique: {bus_result['unique_tokens']}")
    
    print("Processing web content...")
    web_result = pipeline.process_file("web_content.txt", doc_type="web")
    print(f"  Tokens: {web_result['token_count']} | Unique: {web_result['unique_tokens']}")
    
    # Cleanup
    import os
    for filename in files.keys():
        os.remove(filename)
        print(f"✓ Cleaned up {filename}")
    
    print()


def main():
    """Run all pipeline examples"""
    print("\n")
    print("╔════════════════════════════════════════════════════════════╗")
    print("║   NLP PIPELINE: Advanced Integration Examples              ║")
    print("║   Multi-Document Type Processing                           ║")
    print("╚════════════════════════════════════════════════════════════╝")
    print()
    
    try:
        example_basic_pipeline()
        example_multi_type_pipeline()
        example_batch_processing()
        example_available_types()
        example_file_processing_pipeline()
        
        print("="*60)
        print("✓ All pipeline examples completed successfully!")
        print("="*60)
        print()
        
    except Exception as e:
        print(f"\n✗ Error: {e}")
        import traceback
        traceback.print_exc()


if __name__ == "__main__":
    main()
