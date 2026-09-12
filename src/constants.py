import os

MODEL = os.getenv("MODEL", "ollama/qwen3:14b")
CHAT_MODEL = os.getenv("MODEL", "ollama_chat/qwen3:14b")
DATASET_MODEL = os.getenv("DATASET_MODEL", "ollama/llama3.2:3b")
GRADING_MODEL = os.getenv("GRADING_MODEL", "ollama/phi4-reasoning:14b")
EMBEDDING_MODEL = os.getenv("EMBEDDING_MODEL", "ollama/nomic-embed-text:latest")
