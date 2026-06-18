from app.ingest import extract_text_from_pdf

def main():
    pdf_path = "demo/demo_paper/sample.pdf"

    text = extract_text_from_pdf(pdf_path)

    print("Extracted text from PDF:")
    print(text[:500])  # Print the first 500 characters of the extracted text

if __name__ == "__main__":
    main()