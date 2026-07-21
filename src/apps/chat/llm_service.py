import requests


class LLMService:

    def generate(self, message, context):

        prompt = f"""
            你是一個人才推薦 AI。

            請根據提供的資料回答使用者問題。

            使用者問題：
            {message}

            參考資料：
            {context}

            請用簡潔中文回答。
            """

        response = requests.post(
            "http://ollama:11434/api/generate",
            json={
                "model": "qwen2.5:3b",
                "prompt": prompt,
                "stream": False
            }
        )

        result = response.json()

        return result["response"]