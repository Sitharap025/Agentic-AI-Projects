import os
os.environ["USE_TF"] = "0"
import faiss
import pickle
from sentence_transformers import SentenceTransformer
from pathlib import Path



docs_dir = Path("rag_docs/logs")
embeddings_path = "embeddings/rag_faiss.index"
DOC_MAP_PATH = "embeddings/doc_map.pkl"

model=SentenceTransformer("BAAI/bge-small-en")

texts = []
filenames = []

for file in Path(docs_dir).glob("*.txt"):
    with open(file, "r", encoding="utf-8") as f:
        text = f.read()
        texts.append(text)
        filenames.append(str(file.name))

print(f"Loaded {len(texts)} documents")

#Generate Embeddings
embeddings=model.encode(texts, show_progress_bar=True)

#store in FAISS
dimension = embeddings[0].shape[0]
index=faiss.IndexFlatL2(dimension)
index.add(embeddings)

#Save the index and mapping

os.makedirs("embeddings", exist_ok=True)
faiss.write_index(index, embeddings_path)
with open(DOC_MAP_PATH, "wb") as f:
    pickle.dump(filenames, f)

print("Embedded and indexed documents successfully.")
