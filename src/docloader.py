import os

from abc import abstractmethod
from dataclasses import dataclass
from pypdf import PdfReader


@dataclass
class Document:
    content: str
    metadata: dict


class BaseLoader:
    def __init__(self, file_path: str):
        self.file_path = file_path

        if not os.path.isfile(self.file_path):
            raise ValueError("Invalid file path")

    @abstractmethod
    def load(self):
        pass


class PDFLoader(BaseLoader):
    def load(self) -> Document:
        reader = PdfReader(self.file_path)

        text = ""
        for page in reader.pages:
            text += page.extract_text()

        return Document(content=text, metadata=self._generate_metadata(reader))

    @staticmethod
    def _generate_metadata(reader: PdfReader) -> dict:
        metadata = reader.metadata
        num_pages = len(reader.pages)

        return {
            'producer': metadata.producer,
            'author': metadata.author,
            'title': metadata.title,
            'num_pages': num_pages
        }
