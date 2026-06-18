"""
Runs the ScholarAgent retrieval and reasoning pipeline.

Workflow:
1. The agent receives a user query.
2. The agent retrieves relevant documents from the FAISS vector database.
3. The agent uses the retrieved documents to generate a response to the user query.
"""    

from app.config import NUM_CHUNKS
from app.utils import trim_text 

def run_agent_pipeline(query: str, vectorstore):
    """
    Searches the FAISS index and return a summary
    """

    docs = vectorstore.similarity_search(
        query, k=NUM_CHUNKS
    )

    if not docs:
        return "No relevant documents found."
    
    summary = "=== ScholarAgent Summary ===\n\n"

    for i, doc in enumerate(docs, start=1):
        summary += (
            f"Document Chunk {i}\n"
            f"Source: {doc.metadata.get('source', 'Unknown')}\n\n"
            f"{trim_text(doc.page_content)}\n\n"
            "-----------------------------\n\n"
        )

    return summary