# rag_inference.py
import pandas as pd
import faiss
import numpy as np
import pickle
from sentence_transformers import SentenceTransformer
from transformers import pipeline

# Load model, index, metadata
model = SentenceTransformer('fine_tuned_quotes_model')
index = faiss.read_index("quotes_index.faiss")
with open("quotes_meta.pkl", "rb") as f:
    quotes_data = pickle.load(f)
df = pd.DataFrame(quotes_data)

# LLM setup (OpenAI API or use Hugging Face models)
llm = pipeline("text-generation", model="gpt2")  # or GPT-4 API

# Retrieval + Generation
def get_quotes(query, top_k=3):
    query_emb = model.encode([query])
    distances, indices = index.search(np.array(query_emb).astype('float32'), top_k)
    results = df.iloc[indices[0]]
    
    context = "\n".join([f"{r['quote']} - {r['author']}" for _, r in results.iterrows()])
    prompt = f"Here are some quotes:\n{context}\n\nAnswer the query: {query}"
    response = llm(prompt, max_length=100, do_sample=True)
    
    return {"query": query, "quotes": results.to_dict(orient="records"), "generated_answer": response[0]['generated_text']}

# Example
print(get_quotes("inspirational quotes by women"))
