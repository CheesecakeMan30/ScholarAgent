"""
Helper functions for the app.
"""

import re
from app.config import MAX_LENGTH


def clean_text(text: str) -> str:
    """
    Clean the text by removing extra whitespace and newlines.
    """
    text = re.sub(r'\s+', ' ', text)  # Replace multiple whitespace with a single space
    return text.strip()

def trim_text(text: str) -> str: 
    """
    Limit the amount of text sent to the LLM. 
    """
    return text[:MAX_LENGTH]