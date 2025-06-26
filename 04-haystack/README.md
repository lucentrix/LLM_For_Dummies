## 🌾 Haystack - RAG Framework for LLM Applications

**Haystack** is an open-source framework for building **powerful LLM pipelines**, especially for **retrieval-augmented generation**, **question answering**, and **search-based assistants**.

It supports many backends including:

- **Vector DBs**: FAISS, Weaviate, Milvus, Qdrant, etc.
- **LLMs**: OpenAI, Cohere, Hugging Face, Ollama, LM Studio (via OpenAI API)
- **Connectors**: PDF, websites, Markdown, Notion, and more

### 🔧 Key Features

- Modular pipelines for search, summarization, and chat
- Seamless integration with OpenAI-compatible LLM APIs
- Fast prototyping with **DocumentStore + Retriever + Generator**
- Production-ready: FastAPI endpoints, streaming, async, etc.

------

### 📦 Installation

```
pip install farm-haystack[all]
```

if using LLM only:

```
pip install farm-haystack[llm]
```