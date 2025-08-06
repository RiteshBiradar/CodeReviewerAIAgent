import chromadb

def get_chroma_collection():
    client = chromadb.Client()
    collection = client.get_or_create_collection(name="code_feedback")
    return collection
