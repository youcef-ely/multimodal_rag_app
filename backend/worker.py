import os, sys

from groq import Client
from langchain_groq import ChatGroq

from langchain_chroma import Chroma

from langchain_ollama import OllamaEmbeddings
from langchain.storage import InMemoryByteStore
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain.retrievers.multi_vector import MultiVectorRetriever


current_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(current_dir, '..', 'src'))

from utils import load_config, load_from_pickle


current_dir = os.path.dirname(os.path.abspath(__file__))

# Load configuration

CHROMA_DB_DIR = os.path.join(current_dir, '..', 'data/chroma_db')
DOCSTORE_PATH = os.path.join(current_dir, '..', 'data/docstore.pkl')

config = load_config()
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


client = Client(api_key=os.getenv("GROQ_API_KEY"))
model = ChatGroq(temperature=0.5, model=CHAT_MODEL)

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
    | model
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
