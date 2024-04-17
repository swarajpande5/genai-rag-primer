import google.generativeai as generativeai

from chromadb import Documents, EmbeddingFunction, Embeddings

from src.config import Config


class GeminiEmbeddingFunction(EmbeddingFunction):
    def __call__(self, input: Documents) -> Embeddings:
        gemini_api_key = Config.GEMINI_API_KEY
        if not gemini_api_key:
            raise ValueError(
                "GEMINI_API_KEY not provided. Please provide it as environment variable"
            )

        generativeai.configure(api_key=gemini_api_key)
        model = Config.GEMINI_EMBEDDING_MODEL
        title = "Custom Query (Gemini Embedding)"

        return generativeai.embed_content(
            model=model,
            content=input,
            task_type="retrieval_document",
            title=title
        )['embedding']
