import os
import fitz
from app.utils import clean_text

def extract_text_from_pdf(path: str) -> str:
    doc = fitz.open(path)
    texts = []

    for page in doc:
        texts.append(clean_text(page.get_text()))

    return "\n".join(texts)


def ingest_folder(folder_path: str):
    docs = {}

    for filename in os.listdir(folder_path):
        if filename.lower().endswith(".pdf"):
            full_path = os.path.join(folder_path, filename)
            docs[filename] = extract_text_from_pdf(full_path)

    return docs