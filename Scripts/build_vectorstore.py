from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain.text_splitter import CharacterTextSplitter
import os

def build_vector_index(folder_path: str = "rag_docs/logs", index_dir: str = "vectorstore_index"):
    loader = DirectoryLoader(folder_path, glob="**/*.txt", loader_cls=TextLoader)
    docs = loader.load()

    text_splitter = CharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    splits = text_splitter.split_documents(docs)

    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(splits, embeddings)

    vectorstore.save_local(index_dir)
    print(f"Vector index saved to '{index_dir}'")

if __name__ == "__main__":
    build_vector_index()
