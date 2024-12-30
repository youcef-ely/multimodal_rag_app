import os
from src.utils import load_config, load_from_pickle

from langchain_chroma import Chroma
from langchain_ollama import ChatOllama, OllamaEmbeddings
from langchain.storage import InMemoryByteStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers.multi_vector import MultiVectorRetriever

# Load configuration

DATA_DIR = os.path.join('..', 'data')
CHROMA_DB_DIR = os.path.join(DATA_DIR, 'chroma_db')
DOCSTORE_PATH = os.path.join(DATA_DIR, 'docstore.pkl')

config = load_config('../../config.yaml')
CHAT_MODEL = config['models']['chat_model']
EMBEDDING_MODEL = config['models']['embedding_model']
COLLECTION_NAME = config['parameters']['collection_name']

# Initialize embedding model
embeddings = OllamaEmbeddings(model=EMBEDDING_MODEL)

# Initialize vector store
vectorstore = Chroma(
    embedding_function=embeddings,
    persist_directory=CHROMA_DB_DIR,
)

# Load document store
store_dict = load_from_pickle(DOCSTORE_PATH)

store = InMemoryByteStore()
store.mset(list(store_dict.items()))

# Create retriever
retriever = MultiVectorRetriever(
    id_key='doc_id',
    vectorstore=vectorstore,
    byte_store=store,
)

# Initialize language model
llm = ChatOllama(model=CHAT_MODEL, temperature=0)

# Define the prompt template
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# Define the processing chain
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def request_response(query: str):
    """Process a query through the chain and return the response.

    Args:
        query (str): The input query.

    Returns:
        str: The generated response.
    """
    return chain.invoke(query)
