import chromadb
from app.utils.llm_models import get_embedding
from app.utils.config import VECTOR_DB_PATH

# Initialize ChromaDB client (persistent storage)
client = chromadb.PersistentClient(path=VECTOR_DB_PATH)

# Create/Get collection
collection = client.get_or_create_collection(
    name="documents",
    embedding_function=None  # we'll pass embeddings manually
)

# ---------------- Insert into Vector DB ----------------
def add_to_vector_db(documents, ids=None, metadatas=None):
    """
    Add documents to ChromaDB using embeddings from HuggingFace model.
    """
    if ids is None:
        ids = [str(i) for i in range(len(documents))]

    embeddings = [get_embedding(doc) for doc in documents]

    collection.add(
        documents=documents,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )
    return {"status": "success", "count": len(documents)}

# ---------------- Search in Vector DB ----------------
def search_vector_db(query, top_k=3):
    """
    Search ChromaDB for similar documents.
    """
    query_embedding = get_embedding(query)
    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=top_k
    )
    return results
