CREATE EXTENSION IF NOT EXISTS VECTOR;
CREATE TABLE IF NOT EXISTS documents (
    id SERIAL PRIMARY KEY,
    file_name TEXT,
    chunk_id INT,
    content TEXT,
    embedding VECTOR(384)
);