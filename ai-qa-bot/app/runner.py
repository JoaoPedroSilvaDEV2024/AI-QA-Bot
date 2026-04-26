import requests

class Runner:
    def run(self, test):
        url = f"http://127.0.0.1:8000{test['endpoint']}"
        response = requests.get(url)
        data = response.json()

        return test["expected_key"] in data