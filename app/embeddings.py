""" 
Builds a FAISS vector database from PDF text.

The process is below:
Documents ==> Split into chunks ==> Generate embeddings ==> Store in FAISS
"""

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS

from app.config import EMBEDDING_MODEL

def build_index(docs: dict):
    """
    docs example:
    {
        "paper1.pdf": "text..."
        "paper2.pdf": "text..."
    }
    """

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000, chunk_overlap=200
        )
    
    texts = []
    metadata = []

    for filename, content in docs.items():

        chunks = splitter.split_text(content)

        for chunk in chunks:
            texts.append(chunk)
            metadata.append(
                {"source": filename}
            )
    embed_model = HuggingFaceEmbeddings(
        model_name=EMBEDDING_MODEL
        )
    
    vectorstore = FAISS.from_texts(
        texts = texts,
        embedding=embed_model,
        metadatas=metadata
    )

    return vectorstore