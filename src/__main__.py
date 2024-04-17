from src.rag import create_index_pdf, generate_response

pdf_path = input("Enter path of the pdf: ")

collection = create_index_pdf(pdf_path)

query = input("Enter query: ")

response = generate_response(query)

print(response)
