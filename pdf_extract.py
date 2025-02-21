from pathlib import Path

def load_pdf(file_path):
    from langchain_community.document_loaders import PyMuPDFLoader
    loader = PyMuPDFLoader(file_path)
    docs = loader.load()
    print(f"{len(docs)} pages")
    return docs

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def extract_page(file_path, start_page, end_page):
    docs = load_pdf(file_path)
    return format_docs(docs[start_page:end_page])

def save_extracted_text(text):
    dir = Path("temp")
    save_file_path = dir / "extracted_text.txt"
    with open(save_file_path, "a", encoding="utf-8") as file:
        file.write(get_prompt())
        file.write(text)

def get_prompt():
    return """Please provide a detailed explanation for 
the following chapter from the book
The Chip: How Two Americans Invented the Microchip and Launched a Revolution by T.R. Reid.

* Provide roadmap of author's logic (try checkboxes to guide my reading if you deem suitable)
* Include questions and answers that a beginner might ask.
* ensure thorough coverage of the material.

Audience info: 
- math and bio degree. software developer. 
- limit knowledge in hardware. She has read the book *Code: The Hidden Language of Computer Hardware and Software*. the book matches her learning style.
- want to get technical and able to learn quickly with explanation with context.
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
    file_path = '/Users/sixuan/Downloads/books/Microchip.pdf'
    start = 20 # Start from page n-1, n is the page number of first page of the chapter
    end = 47 # End at page n
    text = extract_page(file_path, start, end)
    save_extracted_text(text)
