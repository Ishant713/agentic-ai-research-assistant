from app.memory.vector_store import similarity_search

def retrieve_context(query):
    docs = similarity_search(query)

    return "\n\n".join([doc.page_content for doc in docs])
