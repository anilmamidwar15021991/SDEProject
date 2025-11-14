from PyPDF2 import PdfReader,PdfFileReader


def extract_text(pdf_path):
    reader = PdfReader(pdf_path)
    pages = []
    for p in reader.pages:
        t = p.extract_text()
        if t:
            pages.append(t)
    return " ".join(pages)

def chunk_text(text, chunk_size=500):
    words = text.split()
    for i in range(0, len(words), chunk_size):
        yield " ".join(words[i:i+chunk_size])