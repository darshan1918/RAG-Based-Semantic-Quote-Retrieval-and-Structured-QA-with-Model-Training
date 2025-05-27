import streamlit as st
from rag_inference import get_quotes

st.title("Semantic Quote Retrieval Model")

query = st.text_input("Enter your query:")

if st.button("Get Quotes"):
    result = get_quotes(query)
    st.json(result)
