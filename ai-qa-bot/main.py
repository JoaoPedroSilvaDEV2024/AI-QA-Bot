from app.test_generator import TestGenerator
from app.runner import Runner
from app.analyzer import Analyzer
from app.logger import Logger

generator = TestGenerator()
runner = Runner()
analyzer = Analyzer()
logger = Logger()

tests = generator.generate("/price")

results = []

for t in tests:
    status = runner.run(t)

    result = {
        "endpoint": t["endpoint"],
        "status": status
    }

    results.append(result)
    logger.save(result)

report = analyzer.analyze(results)

print("\n📊 RELATÓRIO FINAL:")
print(report)