import os
import sys
import time

import fitz
import requests

OLLAMA_HOST = "http://localhost:11434"

OLLAMA_MODEL = "nomic-embed-text"
CHUNK_SIZE = 2048  # Max characters per text block


# OLLAMA_MODEL = "avr/sfr-embedding-mistral"
# CHUNK_SIZE = 32768

# OLLAMA_MODEL = "mistral"
# CHUNK_SIZE = 32768


def read_txt(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()


def read_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])


def chunk_text(text, size):
    return [text[i:i + size] for i in range(0, len(text), size)]


def embed_text(text):
    response = requests.post(f"{OLLAMA_HOST}/api/embeddings", json={
        "model": OLLAMA_MODEL,
        "prompt": text
    })

    resp_json = response.json()

    print("Response: ", resp_json)

    if resp_json.get("error") is not None:
        print("Error in response: ", resp_json)
        sys.exit(1)

    if resp_json.get("embedding") is None:
        print("Embedding is not found in response: ", resp_json)
        sys.exit(1)

    return resp_json.get("embedding")


def process_folder(folder_path):
    for fname in os.listdir(folder_path):
        path = os.path.join(folder_path, fname)
        if fname.lower().endswith(".txt"):
            text = read_txt(path)
        elif fname.lower().endswith(".pdf"):
            text = read_pdf(path)
        else:
            continue

        chunks = chunk_text(text, CHUNK_SIZE)
        total_time = 0
        char_count = 0
        for i, chunk in enumerate(chunks):
            start_time = time.time()
            char_count += len(chunk)
            embedding = embed_text(chunk)
            elapsed_time = time.time() - start_time
            total_time += elapsed_time
            print("Embedding processing time: ", elapsed_time)

            # print(f"{fname} chunk {i + 1} chunk: {chunk}\n")
            print(
                f"{fname} chunk {i + 1}({len(chunk)} chars) vector({len(embedding)}): {embedding[:3]}...{embedding[-3:]}")  # Print first and last 3 floats

        print(f"Embedding ({char_count} chars) total processing time: ", total_time)


current_dir = os.getcwd()
print("Current folder: ", current_dir)

doc_folder_path = os.path.join(current_dir, "resources/documents")
print("Processing documents from folder: ", doc_folder_path)

process_folder(doc_folder_path)
