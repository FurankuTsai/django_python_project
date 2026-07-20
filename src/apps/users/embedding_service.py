from fastembed import TextEmbedding


class EmbeddingService:

    def __init__(self):
        self.model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def create(self, text):

        embeddings = self.model.embed([text])

        return list(embeddings)[0].tolist()
    
    def search_users(self, keyword):

        vector = self.embedding.create(keyword)
    
        result = self.vector_repo.search(vector)
    
        return result