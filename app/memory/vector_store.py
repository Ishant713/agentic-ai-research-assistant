
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

embedding_model = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

vector_db = Chroma(
    collection_name="research_memory",
    embedding_function=embedding_model,
    persist_directory="./chroma_db"
)

def add_to_vector_store(texts):
    vector_db.add_texts(texts)

def similarity_search(query):
    return vector_db.similarity_search(query, k=3)