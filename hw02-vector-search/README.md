# Homework 2 - Vector Search

This repository contains my solution for **Homework 2: Vector Search** from the **LLM Zoomcamp 2026** by DataTalksClub.

## Overview

The goal of this homework is to build a semantic search system using text embeddings and compare different retrieval approaches.

The workflow includes:

- Generating sentence embeddings with the ONNX version of **all-MiniLM-L6-v2**
- Computing cosine similarity manually
- Chunking lesson pages into overlapping passages
- Implementing vector search
- Comparing vector search with keyword-based search
- Combining both methods using Reciprocal Rank Fusion (RRF)

Unlike Homework 1, this assignment focuses only on **retrieval** and does not include a Retrieval-Augmented Generation (RAG) pipeline.

## Dataset

The knowledge base consists of the lesson pages from the **LLM Zoomcamp** course repository.

- Repository: https://github.com/DataTalksClub/llm-zoomcamp
- Commit: `8c1834d`
- Documents: **72 Markdown lesson pages**

Each document contains:

- `filename`
- `content`

The documents are later split into overlapping chunks before indexing.

## Technologies

- Python
- Jupyter Notebook
- ONNX Runtime
- all-MiniLM-L6-v2 (ONNX)
- NumPy
- minsearch
- gitsource

## Tasks

This homework consists of six questions:

1. Generate an embedding for a query.
2. Compute cosine similarity manually.
3. Perform vector search by computing similarities directly.
4. Use `VectorSearch` from `minsearch`.
5. Compare keyword search and vector search.
6. Implement Hybrid Search using Reciprocal Rank Fusion (RRF).

## Results

| Question | Topic |
|----------|-------|
| Q1 | Query embedding |
| Q2 | Cosine similarity |
| Q3 | Manual vector search |
| Q4 | Vector search with `minsearch` |
| Q5 | Keyword search vs. vector search |
| Q6 | Hybrid search (RRF) |

All homework questions were completed successfully.

## Project Structure

```
hw02-vector-search/
│
├── homework2.ipynb
├── embedder.py
├── download.py
├── models/
│   └── Xenova/
│       └── all-MiniLM-L6-v2/
│
└── README.md
```

## References

- LLM Zoomcamp 2026
- https://github.com/DataTalksClub/llm-zoomcamp
- ONNX Runtime
- all-MiniLM-L6-v2
- minsearch