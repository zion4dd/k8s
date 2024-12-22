from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def read_root():
    return "<html><body><h1>Hello from FastAPI v2.0.0</h1></body></html>"
