from qdrant_client.models import PointStruct
from .qdrant import client


class VectorRepository:

    def save(self, user_id, vector, text):

        client.upsert(
            collection_name="users",
            points=[
                PointStruct(
                    id=user_id,
                    vector=vector,
                    payload={
                        "user_id": user_id,
                        "text": text
                    }
                )
            ]
        )