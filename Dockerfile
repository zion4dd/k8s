FROM python:3.12-slim

COPY --from=ghcr.io/astral-sh/uv:latest /uv /uvx /bin/

WORKDIR /app

COPY pyproject.toml .
ENV UV_SYSTEM_PYTHON=1
RUN uv pip install -r pyproject.toml

COPY hello.py .

EXPOSE 8000

CMD ["uv", "run", "uvicorn", "hello:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
