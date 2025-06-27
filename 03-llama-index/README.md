## 🦙 LlamaIndex - Framework for LLM-Powered Indexing and Retrieval

**[LlamaIndex](https://github.com/jerryjliu/llama_index)** is an open-source framework for building **retrieval-augmented generation (RAG)** systems and structured interfaces to large language models.

### 🔧 Key Features

- Connect structured and unstructured data to LLMs
- Build custom **document loaders**, **indexes**, **retrievers**, and **chat engines**
- Works with **OpenAI**, **Ollama**, **LM Studio**, **HuggingFace**, etc.
- Supports tools like:
  - Vector databases (e.g., FAISS, Chroma, Weaviate)
  - Local LLMs via OpenAI-compatible APIs

### 🧰 Installation

```
pip install llama-index[llms]  # for LLM wrappers
```



#### Execution

run llamaindex-ollama-embeddings.py, it will print query and search result in debug output:

`Search query:  What is this document about?`

Output:

`Search response:  This document is about Google introducing new state-of-the-art open models called Gemma.`

To see stored vectors, print vector store.

API documentation: [vector stores](https://docs.llamaindex.ai/community/integrations/vector_stores.md), [vector store index](https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/), [retrievers](https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/)

