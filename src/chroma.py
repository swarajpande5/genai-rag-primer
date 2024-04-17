import chromadb

from typing import Optional, List, Union

from src.config import Config


class Chroma:
    def __init__(
            self,
            path_to_persistent_directory: str = Config.CHROMADB_PATH,
            collection_name: str = Config.COLLECTION_NAME,
            embedding_function: Optional[chromadb.EmbeddingFunction] = None
    ):
        self.persistent_directory = path_to_persistent_directory
        self.collection_name = collection_name
        self.embedding_function = embedding_function

        self._client = chromadb.PersistentClient(path=self.persistent_directory)

        self._collection = self._client.get_or_create_collection(
            name=self.collection_name,
            embedding_function=self.embedding_function
        )

    def add(self, documents: List[str]):
        try:
            for i, d in enumerate(documents):
                self._collection.add(documents=d, ids=str(i))
            return self.collection_name
        except Exception as e:
            raise (e)

    def query(self, query: Union[List[str], str], n_results: int):
        """
        Query the collection. Returns the metadata along with the text.
        """
        return self._collection.query(query_texts=query, n_results=n_results)

    def query_text(self, query: str, n_results: int):
        """
        Query the collection. Return only the text.
        """
        return self.query(query=[query], n_results=n_results)['documents'][0]
