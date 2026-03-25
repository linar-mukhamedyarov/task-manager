from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get("/")
def home_page():
    return {"status": "done"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0")