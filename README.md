# Agentic RAG Homework

## Overview

This project implements a simple Retrieval-Augmented Generation (RAG) system and extends it with an Agentic RAG workflow.

The system uses course materials from the LLM Zoomcamp repository (https://github.com/DataTalksClub/llm-zoomcamp) as a knowledge base. User questions are answered by retrieving relevant lesson content and providing it to a language model.

The notebook also explores the impact of document chunking on retrieval quality and prompt size.

---

## Objectives

The homework covers the following concepts:

* Loading documents from a GitHub repository
* Building a search index
* Implementing a basic RAG pipeline
* Comparing full-document retrieval vs chunk-based retrieval
* Building an Agentic RAG workflow using toyaikit tool 

---

## Project Structure

```text
.
├── README.md
├── notebook.ipynb
├── rag_pipeline.py
├── pyproject.toml
└── uv.lock
```

### Files

| File              | Description                                             |
| ----------------- | ------------------------------------------------------- |
| `notebook.ipynb`  | Main notebook containing experiments and demonstrations |
| `rag_pipeline.py` | Reusable implementation of the RAG pipeline             |
| `README.md`       | Project documentation                                   |

---

## Dataset

The knowledge base is built from the lesson materials of the LLM Zoomcamp repository.

Only lesson markdown files are loaded and indexed.

---

## RAG Pipeline

The basic workflow follows three steps:

1. Retrieve relevant documents
2. Build a prompt using retrieved context
3. Generate an answer with Gemini

```python
search → build_prompt → llm
```

The implementation is encapsulated in the `RAGBase` class.

---

## Chunking Experiment

Two retrieval approaches are compared:

### Full Documents

The original lesson files are indexed directly.

### Chunked Documents

Documents are split into overlapping chunks before indexing.

The experiment measures:

* Retrieved results
* Prompt token count
* Context efficiency

The chunked approach significantly reduces prompt size while preserving relevant information.

---

## Agentic RAG

The project also implements an Agentic RAG workflow.

Instead of executing a single retrieval step, the language model can:

1. Decide when to search
2. Perform multiple searches
3. Refine search queries
4. Produce a final answer

The search function is exposed as a tool and executed through an agent loop.

This allows the model to dynamically gather information before answering.

---

## Example Question

```text
How does the agentic loop work, and how is it different from plain RAG?
```

The agent performs multiple searches before generating the final response.

---

## Technologies Used

* Python
* Gemini API
* MinSearch
* ToyAIKit
* Jupyter Notebook

---

## Key Takeaways

This homework demonstrates:

* Basic Retrieval-Augmented Generation
* Retrieval optimization through chunking
* Tool calling
* Agentic workflows
* Comparison between traditional RAG and Agentic RAG

```
```
