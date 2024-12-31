import json
import requests
import streamlit as st
from backend.worker import request_response





# Title and description
st.title('MultiModal Retrieval-Augmented Generation (RAG)')
st.markdown("""
Welcome to the MultiModal RAG app! You can input any query or request below, and 
our backend system will generate insights based on your input. Give it a try!
""")

# Sidebar for additional navigation or options
st.sidebar.title("Instructions")
st.sidebar.markdown("""
1. Enter your question or request in the input box below.
2. Click 'Answer' to get an insight generated by our RAG system.
3. This tool can answer a wide range of queries based on the provided data.
""")

# Input text for user query
query = st.text_input('Enter your request or question below')

# Displaying a loader until the answer is generated
with st.spinner('Generating insight...'):
    if st.button('Answer'):
        if query.strip():  # Check if the query is not empty
            inputs = {'query': query}
            try:
                res = request_response(input['query'])
                st.write("### Insight generated by RAG:")
                st.write(res)
            except requests.exceptions.RequestException as e:
                st.error(f"An error occurred while fetching data: {e}")
        else:
            st.warning("Please enter a valid query.")

# Additional information section
st.markdown("""
### How it works:
- This app leverages a multi-modal RAG model that combines retrieval-based techniques with generative capabilities.
- You can ask a wide variety of questions, from general knowledge to specific data-driven queries.
""")

# Adding a footer or credits section
st.markdown("---")

st.markdown("""
            Made with ❤️ by **Youssef Lyousfi**.  
            For questions or feedback, feel free to reach out at [Youssef's GitHub](https://github.com/youcef.ely).
            """
)
