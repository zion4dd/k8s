import socket

from fastapi import FastAPI
from fastapi.responses import HTMLResponse


def get_server_ip():
    hostname = socket.gethostname()
    server_ip = socket.gethostbyname(hostname)
    return server_ip


app = FastAPI()


@app.get("/", response_class=HTMLResponse)
async def read_root():
    ip = get_server_ip()
    return f"<html><body><h1>Hello from FastAPI v2.0.0 IP={ip}</h1></body></html>"
