from fastembed import TextEmbedding


class EmbeddingService:

    def __init__(self):
        self.model = TextEmbedding(
            model_name="BAAI/bge-small-en-v1.5"
        )

    def create(self, text):

        embeddings = self.model.embed([text])

        return list(embeddings)[0].tolist()