#  Semantic Quote Retrieval with RAG

The RAG system accurately retrieves quotes based on query semantics. For instance, 
the query "Quotes about insanity attributed to Einstein" 
retrieved relevant quotes like "Insanity is doing the same thing over and over again..." w
ith a high relevance score.The system's performance is satisfactory,
but improvements like using GPT-4 could enhance generation fluency.
## Project Overview

This project builds a **semantic quote retrieval system** using the [Abirate/english_quotes](https://huggingface.co/datasets/Abirate/english_quotes) dataset. 
The system leverages **Retrieval Augmented Generation (RAG)** to retrieve quotes based on user queries, combining a **Sentence Transformer** model for embeddings, 
**FAISS** for efficient similarity search, and an **LLM** (e.g., GPT-2) 
for query understanding and response generation.

###  Example Queries
- "Quotes about insanity attributed to Einstein"
- "Motivational quotes tagged ‘accomplishment’"
- "All Oscar Wilde quotes with humor"

---

## Project Structure
 data_prep.py # Data loading and cleaning
├── build_index.py # Build FAISS index from embeddings
├── rag_pipeline.py # Retrieval + LLM pipeline
├── rag_evaluation.py # Evaluation script (RAGAS or manual)
├── app.py # Streamlit app for user queries
├── quotes_clean.csv # Cleaned dataset (generated)
├── quotes_index.faiss # FAISS index (generated)
├── quotes_meta.pkl # Metadata for quotes (generated)
├── README.md # This file

##Run Instructions
   #python data_prep.py
    #python build_index.py
    #streamlit run app.py

