"""
import faiss
import pickle
from sentence_transformers import SentenceTransformer

EMBEDDINGS_PATH = "embeddings/rag_faiss.index"
DOC_MAP_PATH = "embeddings/doc_map.pkl"
DOCS_FOLDER = "rag_docs/logs"

model = SentenceTransformer("BAAI/bge-small-en")

index = faiss.read_index(EMBEDDINGS_PATH)
with open(DOC_MAP_PATH, "rb") as f:
    doc_map = pickle.load(f)

def retrieve_similar_docs(query, top_k=2):
    query_embedding = model.encode([query])
    D, I = index.search(query_embedding, top_k)

    results = []
    for i in I[0]:
        filename = doc_map[i]
        with open(f"{DOCS_FOLDER}/{filename}", "r") as f:
            results.append((filename, f.read()))
    return results

"""

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings
from langchain.prompts import PromptTemplate
from langchain.chains import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

def retrieve_similar_docs(query: str, index_dir: str = "vectorstore_index"):
    embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    vectorstore = FAISS.load_local(index_dir, embeddings, allow_dangerous_deserialization=True)

    #vectorstore = FAISS.load_local(index_dir, embeddings)

    retriever = vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": 2})
    results = retriever.get_relevant_documents(query)

    return results
