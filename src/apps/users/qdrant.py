from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance


client = QdrantClient(
    host="qdrant",
    port=6333
)


def init_collection():

    collections = client.get_collections()

    exists = any(
        c.name == "users"
        for c in collections.collections
    )

    if not exists:
        client.create_collection(
            collection_name="users",
            vectors_config=VectorParams(
                size=384,
                distance=Distance.COSINE
            )
        )