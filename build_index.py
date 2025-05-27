from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import pandas as pd
import pickle

# Load pretrained model (skip fine-tuning)
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load cleaned quotes
df = pd.read_csv("quotes_clean.csv")

# Encode
embeddings = model.encode(df['quote'].tolist(), show_progress_bar=True)

# FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(np.array(embeddings).astype('float32'))

# Save
faiss.write_index(index, "quotes_index.faiss")
with open("quotes_meta.pkl", "wb") as f:
    pickle.dump(df.to_dict(), f)
