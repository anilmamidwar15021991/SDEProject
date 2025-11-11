# SDEProject
# 🧠 Design of a Scalable ETL Pipeline for PDF Data Embedding and Vector Storage

## 📘 Overview
This project implements a **scalable ETL (Extract–Transform–Load) pipeline** for processing PDF files, generating semantic vector embeddings using **Sentence Transformers**, and storing them efficiently in **PostgreSQL** with the **pgvector** extension.

The system automates the process of:
1. Downloading PDF documents from Google Drive,
2. Extracting and chunking text,
3. Generating dense embeddings,
4. Storing embeddings and metadata in a database,
5. Enabling semantic similarity search over document content.

---

## 🚀 Features
- **End-to-End Automation:** Fully automated ETL process from Google Drive to database.
- **Semantic Search Ready:** Stored embeddings enable contextual and meaning-based queries.
- **Scalable Storage:** Uses PostgreSQL with the `pgvector` extension for efficient vector operations.
- **Model Flexibility:** Compatible with any SentenceTransformer model (e.g., MiniLM, MPNet).
- **Containerized Setup:** Easily deployable using Docker Compose.

---

## 🧩 System Architecture



---

## ⚙️ Tech Stack

| Component | Technology |
|------------|-------------|
| Language | Python 3.10 |
| Embedding Model | Sentence Transformers (`all-MiniLM-L6-v2`) |
| Database | PostgreSQL 16 + pgvector |
| Deployment | Docker & Docker Compose |
| File Source | Google Drive API |
| Libraries | `sqlalchemy`, `psycopg2`, `PyPDF2`, `sentence-transformers`, `tqdm`, `python-dotenv` |

---

## 🏗️ Setup and Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/your-username/pdf-etl-pgvector.git
cd pdf-etl-pgvector
