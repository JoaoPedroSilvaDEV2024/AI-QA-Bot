class Analyzer:

    def analyze(self, results):

        total = len(results)
        passed = len([r for r in results if r["status"]])

        fail_cases = [r for r in results if not r["status"]]

        return {
            "total": total,
            "passed": passed,
            "failed": len(fail_cases),
            "accuracy": round((passed / total) * 100, 2),
            "fail_cases": fail_cases
        }