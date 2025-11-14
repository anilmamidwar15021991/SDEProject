
import sys, os
print("python:", sys.executable)
print("cwd   :", os.getcwd())

from drive_auth import authenticate_drive, download_pdf
from data_extraction import extract_text, chunk_text
from Embedding import Embedder
from db import insert_chunk
from config.config import GOOGLE_CREDENTIALS_FILE, EMBED_MODEL, CHUNK_SIZE

def run_etl(service, file_id, file_name):
    print("Download PDF file has been started")
    pdf_path = download_pdf(service, file_id, file_name)
    text = extract_text(pdf_path)
    chunks = list(chunk_text(text, CHUNK_SIZE))
    embedder = Embedder(EMBED_MODEL)
    embeddings = embedder.embed(chunks)
    
    for i, (chunk, emb) in enumerate(zip(chunks, embeddings)):
        insert_chunk(file_name, i, chunk, emb)
    print("Done", file_name)

if __name__ == "__main__":
    svc = authenticate_drive(GOOGLE_CREDENTIALS_FILE)
    # file has been added to drive 
    files = [{"id":"1DwOd0ZbjVU3nDv2QJABlcEUdDJWcgCwW", "name":"0321815734.pdf"},{"id":"1vyMu5gikAD5w-zit4t8BwwnJXWs5S59F","name":"SOFTWARE-DESIGN-BUDGEN.pdf"}]
    for f in files:
        print(f'{f["name"]} Started')
        run_etl(svc, f["id"], f["name"])
    print("process completed")
