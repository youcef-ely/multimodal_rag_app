import os, sys
import requests
import streamlit as st

current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', 'backend'))


from worker import request_response



query = st.text_input('Give your question:')

# Displaying a loader until the answer is generated
if st.button('Submit'):
    res = request_response(query)
    st.write(res)
