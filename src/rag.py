import google.generativeai as generativeai

from src.chroma import Chroma
from src.config import Config
from src.docloader import PDFLoader
from src.embedder import GeminiEmbeddingFunction
from src.prompt import make_prompt, make_rag_prompt
from src.utils import split_text


def create_index_pdf(file_path):
    pdf_loader = PDFLoader(file_path=file_path)
    text = pdf_loader.load().content

    # Split / Chunk the text
    chunked_text = split_text(text)

    # Create index
    chroma_instance = Chroma(embedding_function=GeminiEmbeddingFunction())
    collection_name = chroma_instance.add(chunked_text)

    return collection_name


def query_text(collection_name, query, n_results):
    chroma_instance = Chroma(
        collection_name=collection_name,
        embedding_function=GeminiEmbeddingFunction()
    )
    response = chroma_instance.query_text(query=query, n_results=n_results)

    return response


def query_gemini(prompt, **kwargs):
    model = generativeai.GenerativeModel(Config.GEMINI_MODEL)
    answer = model.generate_content(prompt)

    return answer.text


def generate_response(query):
    response = query_text(Config.COLLECTION_NAME, query, Config.N_RESULTS)
    rag_prompt = make_rag_prompt(
        query=query,
        relevant_passage='\n'.join(response)
    )
    answer = query_gemini(rag_prompt)

    return answer
