## 🐪 Ollama - Local LLM Runtime with OpenAI API Compatibility

**[Ollama](https://ollama.com/)** is a fast, developer-friendly tool for running large language models **locally** via a
command-line interface and **OpenAI-compatible HTTP API**. It simplifies downloading, managing, and running models
like **LLaMA 3**, **Mistral**, **Gemma**, and **Phi** with a single command.

### 🔧 Key Features

- Run **quantized GGUF models** locally (CPU or GPU)
- Simple model management: `ollama run llama3`
- Built-in **OpenAI-compatible API** on `http://localhost:11434/v1`
- Works seamlessly with:
    - LangChain
    - LlamaIndex
    - OpenAI SDKs

### 🧪 API Setup

1. **Install Ollama**:
   https://ollama.com/download

2. **Run the server**:

   ```
   ollama serve
   ```

3. **Pull and run a model** (e.g., LLaMA 3):
   ```
   ollama run llama3
   ```

4. Ollama serves:
   ```
   http://localhost:11434/v1/chat/completions
   ```

### 📦 System Requirements

  - macOS, Windows, or Linux
  - ~8–16 GB RAM recommended
  - GPU optional (uses llama.cpp under the hood)