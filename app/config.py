"""
Configuration values used throughout the app. 
Keep them here here makes it easier to change later. 
"""

# Number of document chunks retrieved from FAISS
NUM_CHUNKS = 5

# Embedding model from Hugging Face
EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"

# Maximum number of characters to send to the LLM
MAX_LENGTH = 4000