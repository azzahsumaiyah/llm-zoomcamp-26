# Homework 1: Building an Agentic RAG System from Scratch

This project implements a **Retrieval-Augmented Generation (RAG)** system that is progressively enhanced from a basic retrieval pipeline into a dynamic **Agentic RAG** system powered by Google's Gemini model through the OpenAI-compatible API.

## 🚀 Project Overview

The knowledge base used throughout this homework consists of all lesson pages (Markdown files) from the `DataTalksClub/llm-zoomcamp` GitHub repository, pinned to commit `8c1834d` to ensure reproducibility.

The following experiments were completed in `homework_1.ipynb`:

### 1. Data Preparation & Exploration (Q1)

- Retrieved course lesson pages directly from GitHub using `gitsource.GithubRepositoryDataReader`.
- Parsed the Markdown files into a searchable knowledge base.
- **Result:** Successfully collected **72 lesson pages**.

### 2. Basic Indexing & Information Retrieval (Q2)

- Built an in-memory search engine using `minsearch`.
- Indexed the `content` field as searchable text and the `filename` field as a keyword field.
- Tested the search engine using the query:

  > *"How does the agentic loop keep calling the model until it stops?"*

- **Result:** The highest-ranked document was:

  ```
  01-agentic-rag/lessons/14-agentic-loop.md
  ```

### 3. Plain RAG Implementation & Token Metrics (Q3)

- Built a basic Retrieval-Augmented Generation (RAG) pipeline by inserting the retrieved document into the LLM prompt.
- Sent the prompt to the `gemini-2.5-flash` model through the OpenAI-compatible client.
- **Result:** The system generated a context-aware answer while consuming approximately **11,461 input tokens**, corresponding to the closest answer choice (**7,000 tokens**) in the homework.

### 4. Text Chunking Optimization (Q4 & Q5)

- Improved retrieval quality and reduced token usage by applying a sliding-window chunking strategy (`size=2000`, `step=1000`).
- **Q4 Result:** The lesson pages were divided into **295 text chunks**.
- **Q5 Result:** Rebuilding the RAG pipeline on chunked documents reduced prompt usage to **5,339 input tokens**, making the system roughly **2× more efficient** (closest homework option: **3× fewer tokens**).

### 5. Transition to Agentic RAG (Q6)

- Upgraded the static RAG pipeline into an autonomous **Agentic RAG** workflow.
- Exposed the search engine as a callable tool (`search_course_material`) for the language model.
- Added system instructions enabling the model to iteratively search the knowledge base using different keywords before generating a final answer.
- **Result:** The agent autonomously decided to invoke the search tool **twice** (using the keywords **"agentic loop"** and **"RAG pipeline"**) before producing a comprehensive final response (closest homework option: **4 tool calls**).

## 🛠️ Tech Stack & Environment

- **Language:** Python 3.12 (managed with `uv`)
- **Environment:** GitHub Codespaces (Ubuntu Linux)
- **LLM Provider:** Google Gemini API (`gemini-2.5-flash`) via the OpenAI-compatible client
- **Libraries:** `gitsource`, `minsearch`, `python-dotenv`, `ipykernel`