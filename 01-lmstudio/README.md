## LM Studio - Local Language Model Server

**[LM Studio](https://lmstudio.ai/)** is a desktop application that lets you **run open-access language models locally** on your computer with a simple UI and built-in server. It supports models like **LLaMA, Mistral, Gemma**, and more via **GGUF format**, running efficiently using **GGML/llama.cpp** backends.

### 🔧 Key Features

- **Run LLMs locally** on CPU or GPU (Metal/ROCm/CUDA depending on platform).
- **No internet required** after model download — fully offline inference.
- **OpenAI-compatible API server** for seamless integration with tools like:
  - LangChain
  - LlamaIndex
  - Python `openai` client
- Cross-platform: **macOS, Windows, Linux (via Wine or workaround)**

### 🧪 Local API Mode (OpenAI-compatible)

To use LM Studio in local projects:

1. Go to **Settings > Developer > Enable local server**.

2. Set port (default: `1234`).

3. Load a supported **GGUF model** (e.g., `llama3-8b-instruct`).

4. LM Studio exposes:

   ```
   http://localhost:1234/v1/chat/completions
   ```