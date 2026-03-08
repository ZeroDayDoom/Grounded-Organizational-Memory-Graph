
from sentence_transformers import SentenceTransformer
import numpy as np
import faiss

model = SentenceTransformer("all-MiniLM-L6-v2")

def build_index(claims):

    texts = [
        f'{c["subject"]} {c["relation"]} {c["object"]}'
        for c in claims
    ]

    embeddings = model.encode(texts)

    index = faiss.IndexFlatL2(len(embeddings[0]))
    index.add(np.array(embeddings))

    return index, texts

def search(index, texts, query):

    q = model.encode([query])

    D, I = index.search(np.array(q), 3)

    print("Top matches:")
    for i in I[0]:
        print(texts[i])
