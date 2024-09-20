from llama_index.core import VectorStoreIndex
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core.retrievers import VectorIndexRetriever
from dotenv import load_dotenv

load_dotenv()

from custom_gmail_reader import CustomGmailReader

# Instantiate the CustomGmailReader
loader = CustomGmailReader(
    query="",
    max_results=50,
    results_per_page=10,
    service=None
)

# Load the emails
documents = loader.load_data()

# Print email information
print(f"Number of documents: {len(documents)}")
for i, doc in enumerate(documents[:5]):
    print(f"Document {i+1}:")
    print(f"To: {doc.metadata.get('to', 'N/A')}")
    print(f"From: {doc.metadata.get('from', 'N/A')}")
    print(f"Subject: {doc.metadata.get('subject', 'N/A')}")
    print(f"Date: {doc.metadata.get('date', 'N/A')}")
    print(f"Content snippet: {doc.text[:1000]}...")
    print("=" * 50)

    # Create index
index = VectorStoreIndex.from_documents(documents)

# Create retriever
retriever = VectorIndexRetriever(index=index)

# Create query engine
query_engine = RetrieverQueryEngine(retriever=retriever)

# Example query
response = query_engine.query("<Insert a question that can be answered from your email>")
print(response)
