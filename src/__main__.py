from src.rag import create_index_pdf, generate_response


def print_options():
    print("1. Add pdf to knowledgebase")
    print("2. Ask a query")
    print("3. Exit")
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
            query = input("Enter query: ")
            response = generate_response(query)
            print(f"{response} \n")
        elif op == '3':
            break 
        else:
            print("Invalid Option. \n")