# ScholarAgent

ScholarAgent is an AI-powered research assistant that ingests academic PDF documents, converts them into semantic embeddings, stores them in a FAISS vector database, retrieves relevant information using similarity search, and generates structured summaries through a local Large Language Model (LLM).

The project demonstrates core concepts used in modern Retrieval-Augmented Generation (RAG) systems:

* Document Ingestion
* Semantic Embeddings
* Vector Databases
* Similarity Search
* Retrieval-Augmented Generation (RAG)
* Local LLM Inference
* Streamlit Deployment

---

# Project Overview

Traditional LLMs cannot answer questions about documents they have never seen.

ScholarAgent solves this problem by:

1. Reading PDF documents.
2. Extracting text.
3. Breaking text into chunks.
4. Converting chunks into vector embeddings.
5. Storing embeddings inside FAISS.
6. Retrieving relevant chunks for a query.
7. Passing retrieved information into a local LLM.
8. Returning a structured summary.

This architecture is called Retrieval-Augmented Generation (RAG).

---

# Architecture

```text
PDF Files
    │
    ▼
Document Ingestion
    │
    ▼
Text Cleaning
    │
    ▼
Chunking
    │
    ▼
Hugging Face Embeddings
    │
    ▼
FAISS Vector Database
    │
    ▼
Similarity Search
    │
    ▼
Local LLM (GPT4All)
    │
    ▼
Generated Summary
```

---

# Project Structure

```text
ScholarAgent/
│
├── app/
│   ├── __init__.py
│   ├── agent_pipeline.py
│   ├── config.py
│   ├── embeddings.py
│   ├── ingest.py
│   ├── main.py
│   └── utils.py
│
├── demo/
│   └── demo_papers/
│       └── sample.pdf
│
├── outputs/
│
├── webapp/
│   ├── __init__.py
│   └── streamlit_app.py
│
├── requirements.txt
├── .gitignore
└── README.md
```

---

# How the Code Works

---

## ingest.py

Purpose:

Reads PDF documents and extracts text.

Key Concepts:

* PyMuPDF
* PDF parsing
* Text extraction

Workflow:

```python
extract_text_from_pdf()
```

1. Opens a PDF.
2. Reads every page.
3. Extracts text.
4. Cleans text.
5. Returns a string.

```python
ingest_folder()
```

1. Searches a directory.
2. Finds all PDF files.
3. Extracts text from each.
4. Returns:

```python
{
    "paper1.pdf": "...text...",
    "paper2.pdf": "...text..."
}
```

---

## utils.py

Purpose:

Contains helper functions.

Examples:

### clean_text()

Removes:

* Extra whitespace
* Empty lines
* Formatting artifacts

### trim_text()

Reduces document size before sending text into the LLM.

Benefits:

* Faster generation
* Lower memory usage

---

## embeddings.py

Purpose:

Creates vector embeddings and stores them in FAISS.

Key Concepts:

### Embeddings

Embeddings convert text into numerical vectors.

Example:

```text
"Transformers are useful"
        ↓
[0.23, -0.11, 0.81, ...]
```

Similar meanings produce similar vectors.

---

### Chunking

Large papers are split into smaller sections:

```text
Paper
  ↓
Chunk 1
Chunk 2
Chunk 3
...
```

This improves retrieval accuracy.

---

### FAISS

Facebook AI Similarity Search

Stores vectors efficiently and enables fast search.

Workflow:

```python
build_index()
```

1. Split documents into chunks.
2. Generate embeddings.
3. Store vectors in FAISS.
4. Return vector database.

---

## config.py

Purpose:

Stores project configuration.

Examples:

```python
TOP_K_RETRIEVAL = 3
```

Controls how many document chunks are retrieved.

Benefits:

* Centralized settings
* Easier maintenance

---

## agent_pipeline.py

Purpose:

Main AI reasoning pipeline.

This is the heart of ScholarAgent.

Workflow:

### Step 1

Receive user query.

Example:

```text
What are the key findings?
```

---

### Step 2

Perform similarity search.

```python
vectorstore.similarity_search()
```

Returns the most relevant document chunks.

---

### Step 3

Create prompt.

Example:

```text
Summarize this research paper.
```

---

### Step 4

Send prompt to local LLM.

The LLM receives:

* Query
* Retrieved content

---

### Step 5

Generate structured summary.

Output:

```text
TL;DR
Methods
Results
Limitations
```

---

## main.py

Purpose:

Command-line entry point.

Workflow:

1. Load PDFs.
2. Build vector database.
3. Run retrieval.
4. Generate summaries.
5. Save outputs.

Run:

```bash
python -m app.main
```

---

## streamlit_app.py

Purpose:

Provides graphical user interface.

Features:

* Build Index button
* Query input
* Summary generation
* Results display

Run:

```bash
streamlit run webapp/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

# Installation

## Clone Repository

```bash
git clone https://github.com/CheesecakeMan30/ScholarAgent.git
```

```bash
cd ScholarAgent
```

---

## Create Virtual Environment

Windows:

```powershell
python -m venv venv
```

Activate:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\venv\Scripts\Activate.ps1
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Running ScholarAgent

---

## Option 1: Command Line

Place PDFs in:

```text
demo/demo_papers/
```

Run:

```bash
python -m app.main
```

---

## Option 2: Streamlit Interface

Run:

```bash
streamlit run webapp/streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

# Example Workflow

1. Add PDF files.
2. Build Index.
3. Ask a question.
4. Retrieve relevant chunks.
5. Generate summary.
6. Review results.

---

# Technologies Used

* Python
* Streamlit
* LangChain
* Hugging Face
* Sentence Transformers
* FAISS
* GPT4All
* PyMuPDF

---

# Future Improvements

* Citation generation
* Multi-document comparison
* Research trend analysis
* ArXiv integration
* Cloud deployment
* Multi-agent collaboration

---

# Resume Description

ScholarAgent – AI Research Assistant

Developed a Retrieval-Augmented Generation (RAG) system that ingests academic PDFs, generates semantic embeddings using Hugging Face models, indexes documents with FAISS, and produces structured research summaries through a local Large Language Model. Designed a modular Python architecture integrating document processing, vector search, semantic retrieval, and Streamlit-based user interaction while eliminating reliance on paid AI APIs.

---

# License

Educational and Portfolio Use.
