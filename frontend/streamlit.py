import json
import requests
import streamlit as st


st.title('MultiModal RAG')

query = st.text_query('Enter your request or your question below')
inputs = {'query': query}

if st.button('Answer'):
    res = requests.post(url="http://127.0.0.1:8000", data = json.dump(inputs))
    st.write("Insight generated by RAG:")
    st.write(res.text)
