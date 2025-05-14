from pathlib import Path

def load_pdf(file_path):
    from langchain_community.document_loaders import PyMuPDFLoader
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    return docs

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def extract_page(file_path, start_page, end_page):
    docs = load_pdf(file_path)
    return format_docs(docs[start_page:end_page])

def save_extracted_text(text, book_title):
    dir = Path("temp")
    save_file_path = dir / "extracted_text.txt"
    with open(save_file_path, "a", encoding="utf-8") as file:
        file.write(get_prompt(book_title))
        file.write(text)

def get_prompt(book_title=None):
    return f"Please analyze {f"the following chapter from the book { book_title }" if book_title else "the following text"}\n* Provide roadmap of author's logic / thought process (try checkboxes to guide reading if deem suitable)\n* Provide thorough coverage of the material. get technical\nHere's the text:\n"
    """
    Learning style:
    - emphasize learning through application rather than isolated study, with cross-domain connections acting as the "bridge" to tie abstract principles to actionable work.
    - Prefer dynamic, incremental learning over flat information
    - Learn better with (historical) context, patterns, narratives
    - Get excited when see connections between abstract concepts and real-world applications
    - Like to understand the "why" behind systems
    - Need real motivation beyond just "should learn this"
    - Analogy in different category confuses me. Explain within context.
    - Avoid oversimplification
    """

if __name__ == '__main__':
    # file_path = Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs" / 'epub_pdf/dev/ddia/string/Cstring.pdf'
    # file_path = Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs" / 'epub_pdf/dev/ddia/string/Gusfield strings, trees, and sequences.pdf'
    file_path = Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs" / 'epub_pdf/history/network_soviet.pdf'
    book_title="How Not to Network a Nation: The Uneasy History of the Soviet Internet by Benjamin Peters"

    # file_path = Path.home() / "Library" / "Mobile Documents" / "com~apple~CloudDocs" / 'epub_pdf/dev/chip.pdf'
    # book_title="The Chip : How Two Americans Invented the Microchip and Launched a Revolution"
    start = 95 # n-1
    end = 121 # page of next chapter - 1
    text = extract_page(file_path, start, end)
    save_extracted_text(text, book_title)

"""
python3 -m venv venv
source venv/bin/activate
pip install pymupdf langchain_community
python pdf_extract.py
"""