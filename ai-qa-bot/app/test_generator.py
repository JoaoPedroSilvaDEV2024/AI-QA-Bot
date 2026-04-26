import openai

class TestGenerator:

    def generate(self, endpoint):
        prompt = f"""
        Você é um engenheiro de QA.
        Gere testes para o endpoint: {endpoint}

        Retorne em JSON com:
        - endpoint
        - expected_key
        """

        # versão simples (mock se não quiser API paga)
        return [
            {"endpoint": "/price", "expected_key": "price"},
            {"endpoint": "/status", "expected_key": "status"}
        ]