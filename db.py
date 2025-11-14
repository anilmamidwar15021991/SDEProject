from sqlalchemy import create_engine, text
from sqlalchemy.engine import Engine
import numpy as np
from config.config import PG_URI


engine: Engine = create_engine(PG_URI)

def insert_chunk(file_name, chunk_id, content, embedding):
    # convert to Python list to pass to pgvector via SQLAlchemy
    emb_list = embedding.tolist()
    with engine.begin() as conn:
        conn.execute(text("""
            INSERT INTO documents (file_name, chunk_id, content, embedding)
            VALUES (:f, :i, :c, :e)
        """), {"f": file_name, "i": chunk_id, "c": content, "e": emb_list})
