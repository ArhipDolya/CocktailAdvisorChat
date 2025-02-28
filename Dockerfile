FROM python:3.10-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install poetry

COPY pyproject.toml poetry.lock ./
COPY final_cocktails.csv ./

RUN poetry config virtualenvs.create false

RUN poetry install --only main --no-root

COPY . .

EXPOSE 8000