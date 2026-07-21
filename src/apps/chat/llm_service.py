class LLMService:

    def generate(self, message, context):

        return f"""
            使用者問題：
            {message}
            
            參考資料：
            {context}
            
            """