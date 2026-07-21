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

    def search(self, vector, limit=5):
    
        result = client.query_points(
            collection_name="users",
            query=vector,
            limit=limit
        )
    
        return [
            {
                "user_id": point.id,
                "score": point.score
            }
            for point in result.points
        ]