import os

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama

llm = Ollama(
    model="llama3",  # or another chat-capable local model
    base_url="http://localhost:11434"
)

embed_model = OllamaEmbedding(
    model_name="mxbai-embed-large",
    base_url="http://localhost:11434"  # Optional: specify if different from default
)

# Apply global settings (recommended in new LlamaIndex)
Settings.llm = llm
Settings.embed_model = embed_model

current_dir = os.getcwd()
print("Current folder: ", current_dir)

doc_folder_path = os.path.join(current_dir, "../resources/documents")
print("Processing documents from folder: ", doc_folder_path)

documents = SimpleDirectoryReader(doc_folder_path).load_data()

#  When you use from_documents, your Documents are split into chunks and parsed into Node objects, lightweight
#  abstractions over text strings that keep track of metadata and relationships.
#
# For mode details, see documentation
# https://docs.llamaindex.ai/community/integrations/vector_stores.md
# https://docs.llamaindex.ai/en/stable/module_guides/indexing/vector_store_index/
# https://docs.llamaindex.ai/en/stable/examples/retrievers/composable_retrievers/
index = VectorStoreIndex.from_documents(documents)

# Search / embed
query_engine = index.as_query_engine()
query = "What is this document about?"
print("Search query: ", query)
response = query_engine.query(query)
print("Search response: ", str(response))
