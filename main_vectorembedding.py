import numpy as np
import pandas as pd
#import streamlit as st
import os
import io
import sys;sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from dotenv import dotenv_values,load_dotenv
import glob
import time
from urllib.parse import unquote
from PyPDF2 import PdfReader,PdfFileReader

import asyncio
from tqdm import tqdm
import psycopg2
#from sharepoint_service import sp_model,sharepoint_connect_New,sharepoint_restapi_New

from psycopg2 import sql
from sqlalchemy import create_engine,text
from sentence_transformers import SentenceTransformer,util
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores.pgvector import PGVector
from langchain_community.document_loaders import PyPDFLoader,TextLoader
from langchain_core.document_loaders import Blob,BaseBlobParser
from langchain_core.documents import Document
from langchain_community.embeddings import SentenceTransformerEmbeddings
from typing import AsyncIterator, Iterator


env_config=dotenv_values('config\.env')


print('Creating SQL connection to PostGreSQL')

db_connection_params = {
    "host": "localhost",
    "dbname": "SDE",
    "user": "postgres",
    "password": "admin",
    "port":"5432"
    
}

vector_dbname='SDE_pdf_contents'


CONNECTION_STRING=(f'postgresql://{db_connection_params["user"]}:{db_connection_params["password"]}@{db_connection_params["host"]}:{db_connection_params["port"]}/{db_connection_params["dbname"]}')
#embeddings=SentenceTransformerEmbeddings(model_name="sentence-transformers/distiluse-base-multilingual-cased-v1")
embeddings=SentenceTransformerEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")




