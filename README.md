## Gen AI Primer with Gemini

#### Local setup steps:

1. Create an account on [Google Cloud Platform](https://console.cloud.google.com).

2. Head over to [ai.google.dev](https://ai.google.dev/) and get the Gemini API Key (Save the API somewhere safe for later).

3. Install Python 3.11 (Refer [Python documentation](https://www.python.org/)).

4. Clone the repository and `cd` inside it,
    ```
    $ git clone https://github.com/swarajpande5/genai-rag-primer.git
    $ cd genai-rag-primer
    ```

5. Create a virtual environment and activate the same,
    ```
    $ python3.11 -m venv venv
    $ source venv/bin/activate
    ```

6. Install the project and its dependencies,
    ```
    $ pip install -e .
    ```

7. Add the `GEMINI_API_KEY` as the environment variable,
    ```
    $ export GEMINI_API_KEY=<PASTE THE API KEY>
    ```
    OR
    
    Create a `.env` file and specify the `GEMINI_API_KEY` inside it,
    ```yaml
    # .env file
    GEMINI_API_KEY=<PASTE THE API KEY>
    ```

8. (Optional) The following environment variables can be specified in the same way as above.  

    - **CHROMADB_PATH** : The path on the local system where Chroma vector database will be created (Default: **$HOME/chromadb**).
    - **COLLECTION_NAME** : The name of the collection inside Chroma vector database where vector embeddings will be stored (Default: **gemini-rag**).
    - **GEMINI_EMBEDDING_MODEL** : The model which will be used to create embeddings (Default: **models/embedding-001**).
    - **GEMINI_MODEL** : The LLM which will be used (Default: **gemini-pro**).
    - **N_RESULTS** : The number of relevant results from vector database to fetch, which will be passed to the model later (Default: **3**).
    
        **Note:** The number of matching embeddings can be less as compared to N_RESULTS. 

9.  Start the CLI application,
    ```
    $ python3.11 src/__main__.py
    ```

#### References

- [Medium article](https://medium.com/@saurabhgssingh/understanding-rag-building-a-rag-system-from-scratch-with-gemini-api-b11ad9fc1bf7) by Saurabh Singh
- [Google's Gemini API Documentation](https://ai.google.dev/gemini-api/docs)
- [ChromaDB Documentation](https://www.trychroma.com/)
