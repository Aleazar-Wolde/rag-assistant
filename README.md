# RAG Assistant

A question-answering chatbot that answers questions about your documents using Retrieval Augmented Generation (RAG).

## What it does

Upload any document and ask questions about it. The system searches through the document by meaning — not just keywords — and returns accurate answers.

## How it works

1. **Ingest** — documents are chunked and stored in a vector database (ChromaDB)
2. **Retrieve** — when a question is asked, the system finds the most relevant chunks
3. **Generate** — the chunks and question are sent to an LLM to produce an answer

## Tech Stack

- Python
- LangChain
- ChromaDB
- FastAPI
- OpenAI

## Project Structure
