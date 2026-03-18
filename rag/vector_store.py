# LIGHTWEIGHT VERSION (NO ML MODELS)

def load_documents():
    global docs
    
    with open("data/debugging_knowledge.txt", "r") as f:
        docs = f.read().split("---------------------------------------")


def search_docs(query):
    # simple keyword search instead of embeddings
    results = []
    
    for doc in docs:
        if any(word.lower() in doc.lower() for word in query.split()):
            results.append(doc)

    return results[:2] if results else ["General debugging: Check logic and syntax."]