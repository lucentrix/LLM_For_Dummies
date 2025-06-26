

### Ollama embeddings

One of the best LLM models for embedding large text blocks with high quality and performance is mistral:instruct (or mistral:latest) in Ollama, or a MiniLM/E5 model for lower VRAM usage if embedding is your sole goal.

For long-context embedding, the nomic-embed-text or nomic-embed-mistral (supports long text and produces high-quality embeddings) is also a top choice.
nomic-embed-text is optimized for long-form embeddings, ideal for large documents.

For fast performance with smaller VRAM footprint, try e5-mistral or mini-lm (via Hugging Face).

### Models details

`nomic-embed-text:latest 
https://ollama.com/library/nomic-embed-text:latest
A high-performing open embedding model with a large token context window. 
Context size: 2048`

Command:
`ollama run nomic-embed-text`

`mistral or mistral:7b
The 7B model released by Mistral AI, updated to version 0.3. 
https://ollama.com/library/mistral
Context size: 32768`

`ollama run mistral`

### Requirements

    Ollama running with nomic-embed-text, mistral, or llama2 model installed.
    
    PyMuPDF (for PDF parsing), llama-index (wrapper), sentence-transformers (optional for external models).



### Installation

install pdf parser library:

`pip install PyMuPDF`

To run ollama server:

`ollama serve`

Ollama cli doesn't do embeddings. Use the API from python or directly from terminal:

You can send POST request to Ollama to generate embedding:

`curl localhost:11434/api/embed -d "{\"model\":\"nomic-embed-text\",\"input\":\"why is the sky blue?\"}"`

Ollama will send response:

`{"model":"nomic-embed-text","embeddings":[[0.017111959,0.04398493,-0.14886934,....,-0.016646868,-0.043208014,0.028309498]],"total_duration":16852916,"load_duration":3220879,"prompt_eval_count":7}`



​    





