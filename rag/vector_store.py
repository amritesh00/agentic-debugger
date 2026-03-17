import chromadb
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.Client()
collection = client.get_or_create_collection("debug_docs")

def load_documents():
    with open("data/debugging_knowledge.txt","r") as f:
        docs = f.read().split("---------------------------------------")

    for i,doc in enumerate(docs):
        embedding = model.encode(doc).tolist()
        collection.add(
            documents=[doc],
            embeddings=[embedding],
            ids=[str(i)]
        )

def search_docs(query):
    embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=2
    )

    return results["documents"][0]