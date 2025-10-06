import chromadb
from app.utils.llm_models import get_embedding
from app.utils.config import VECTOR_DB_PATH
import logging

logger = logging.getLogger(__name__)

# Initialize ChromaDB client
try:
    client = chromadb.PersistentClient(path=VECTOR_DB_PATH)
    collection = client.get_or_create_collection(
        name="documents",
        embedding_function=None
    )
except Exception as e:
    logger.error(f"ChromaDB initialization error: {e}")
    raise

def add_to_vector_db(documents, ids=None, metadatas=None):
    try:
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
    except Exception as e:
        logger.error(f"Error adding to vector DB: {e}")
        return {"status": "error", "message": str(e)}

def search_vector_db(query, top_k=3):
    try:
        query_embedding = get_embedding(query)
        results = collection.query(
            query_embeddings=[query_embedding],
            n_results=top_k
        )
        return results
    except Exception as e:
        logger.error(f"Error searching vector DB: {e}")
        return {"documents": [], "metadatas": [], "distances": []}