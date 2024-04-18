from src.chroma import Chroma
from src.embedder import GeminiEmbeddingFunction
from src.rag import create_index_pdf, generate_response


def print_options():
    print("1. Add pdf to knowledgebase")
    print("2. Print embeddings in the vector db")
    print("3. Ask a query")
    print("4. Exit")
    option = input("Enter your option: ")
    
    return option


if __name__ == '__main__':
    while(True):
        op = print_options()
        if op == '1':
            pdf_path = input("Enter path of the pdf: ")
            collection = create_index_pdf(pdf_path)
            print("\nAdded the pdf to the knowledgebase.\n")
        elif op == '2':
            chroma_instance = Chroma(embedding_function=GeminiEmbeddingFunction())
            print(f"\n{chroma_instance._collection.get(include=['embeddings'])}\n")
        elif op == '3':
            query = input("Enter query: ")
            response = generate_response(query)
            print(f"{response} \n")
        elif op == '4':
            break 
        else:
            print("\nInvalid Option.\n")