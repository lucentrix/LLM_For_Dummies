# 🤖 LLM for Dummies

Welcome to **LLM for Dummies** – a beginner-friendly guide and code collection demonstrating how to use **Large Language Models (LLMs)** locally with **consumer hardware** (like your gaming PC with 16GB VRAM). This project focuses on practical examples using:

- [**LM Studio**](https://lmstudio.ai) – A GUI-based LLM interface
- [**Ollama**](https://ollama.com) – Easy CLI/API tool for running models locally
- [**LlamaIndex**](https://llamaindex.ai) – Connecting LLMs to custom/private data
- [**Haystack**](https://haystack.deepset.ai/) - Retrieval-augmented generation (RAG) and agentic pipeline
- [**Quantized models**] – Models optimized to run on mid-tier GPUs

> **Audience**: Developers or tinkerers with basic programming and LLM knowledge. No deep ML or GPU programming required.

### OpenAI API Support

| Framework      | Supports OpenAI API  | Can use with Ollama / LM Studio? | Notes                      |
| -------------- | -------------------- | -------------------------------- | -------------------------- |
| **LangChain**  | ✅ Yes                | ✅ Yes (set `openai_api_base`)    | Most flexible              |
| **LlamaIndex** | ✅ Yes                | ✅ Yes                            | Easy to configure          |
| **Haystack**   | ✅ Yes                | ✅ Partial                        | May need adapter for local |
| **LM Studio**  | ⚠️ Partial (API host) | ✅ Yes                            | Needs local server enabled |
| **Ollama**     | ⚠️ Not a framework    | ✅ Yes (runs OpenAI API)          | Use with `ollama serve`    |

---

## 🧠 Key Concepts Covered

- Running LLMs on your own machine (no OpenAI key needed)
- Using quantized models (GGUF/GGML) for fast, low-resource inference
- Accessing LLMs through local APIs
- Searching PDFs, documents, and private datasets
- Building simple chatbot-like apps

---

## 📦 Folder Structure

```
LLM_For_Dummies/
├── 01-lmstudio/
│   └── mistral_function_calc.py
├── 02-ollama/
│   │── embeddings.py
│   └── README.md
├── 03-llama-index/
├──── llamaindex-ollama/
│     │── llamaindex-ollama-embeddings.py
│     └── README.md
├──── requirements.txt
└── README.md
```

---

## ✅ Prerequisites

- A PC or laptop with:
  - **16 GB GPU VRAM** (RTX 3080, 4070, etc.)
  - **Python 3.10+**
  - **Git + pip + virtualenv**
- Optional: [Ollama installed](https://ollama.com/download), [LM Studio](https://lmstudio.ai)

---

## 🚀 Quick Start

### 1. Clone the Repo

```bash
git clone https://github.com/lucentrix/LLM_For_Dummies.git
cd LLM_For_Dummies/01-lmstudio
```

### 2. Create a Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

### 3. Try a Demo

```bash
cd 01-ollama-basic-chat
python mistral_function_calc.py
```

---

## 🧪 Example Scenarios


### 🔸 01: LM Studio HTTP API
- Connects to LM Studio running on port `1234`
- Sends prompts and receives model responses
- Great for testing quantized GGUF models


---

## 💾 Models Tested

| Model         | Format  | Size | Notes |
|---------------|---------|------|-------|
| Mistral 7B    | GGUF    | ~4GB | Fast and smart |
| LLaMA 2 13B   | GGUF    | ~8GB | Needs more VRAM |
| Phi-2         | GGUF    | ~2GB | Small, good for basics |
| Zephyr        | GGUF    | ~4GB | Chat-tuned model |
| Nous Hermes 2 | GGUF    | ~7GB | Good for multi-turn chats |

> All models run **locally** with **no internet needed** once downloaded.

---

## 🔧 Tips for Best Performance

- Prefer **Q4_0** or **Q5_K_M** quantization for a good speed/quality tradeoff
- Use **Ollama** for background model serving
- Combine **LlamaIndex + Ollama** for building RAG (Retrieval Augmented Generation) apps

---

## 🛠️ Troubleshooting

- **CUDA OOM**? Try smaller quantized model or reduce context length.
- **API not responding?** Make sure LM Studio/Ollama is running.
- **Python error?** Check your `requirements.txt` versions and re-install.

---

## 📚 Resources

- [LM Studio Docs](https://docs.lmstudio.ai/)
- [Ollama CLI Docs](https://ollama.com/library)
- [LlamaIndex Quickstart](https://docs.llamaindex.ai)
- [GGUF Model List](https://huggingface.co/TheBloke)

---

## 👥 Contributing

Found a bug? Want to add a demo? PRs are welcome. Just follow the structure and keep examples beginner-friendly.

---

## 📜 License

This project is MIT-licensed. Free to use, modify, and share.

---

## ✨ About

Made by hobbyists for hobbyists. LLMs should be **fun**, **private**, and **free to tinker with**.

> *"The best way to learn is to break stuff and fix it."* 🛠️

