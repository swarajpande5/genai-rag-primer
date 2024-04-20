import os

from dotenv import load_dotenv
from pathlib import Path

load_dotenv()


class Config:
    CHROMADB_PATH = os.environ.get('CHROMADB_PATH', str(Path.home() / 'chromadb'))
    COLLECTION_NAME = os.environ.get('COLLECTION_NAME', 'gemini-rag')
    GEMINI_API_KEY = os.environ.get('GEMINI_API_KEY')
    GEMINI_EMBEDDING_MODEL = os.environ.get('GEMINI_EMBEDDING_MODEL', 'models/embedding-001')
    GEMINI_MODEL = os.environ.get('GEMINI_MODEL', 'gemini-pro')
    N_RESULTS = os.environ.get('N_RESULTS', 3)
