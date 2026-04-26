import json
from datetime import datetime

class Logger:

    def save(self, data):
        data["timestamp"] = str(datetime.now())

        with open("app/report.json", "a") as f:
            f.write(json.dumps(data) + "\n")