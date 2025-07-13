
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agents.retrieve_docs import retrieve_similar_docs

query = "High temperature and vibration near 0.7. Possible filter or airflow issue."
docs = retrieve_similar_docs(query)

for fname, content in docs:
    print(f"\n📄 {fname}")
    print(content)



