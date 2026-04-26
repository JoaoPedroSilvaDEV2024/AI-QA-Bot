from fastapi import FastAPI

app = FastAPI()

@app.get("/price")
def get_price():
    return {"price": 49.90}

@app.get("/status")
def status():
    return {"status": "ok"}