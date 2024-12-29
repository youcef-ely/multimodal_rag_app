
import pickle
from src.utils import load_config
from langchain_chroma  import Chroma
from langchain_ollama import ChatOllama
from langchain_ollama import OllamaEmbeddings
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_vector import MultiVectorRetriever
from langchain_core.output_parsers import StrOutputParser

config = load_config('config.yaml')
COLLECTION_NAME = config['parameters']['collection_name']
EMBEDDING_MODEL = config['models']['embedding_model']
CHAT_MODEL = config['models']['chat_model']


vectorstore = Chroma(
    collection_name=COLLECTION_NAME,
    persist_directory='/kaggle/working/chroma_db',
)

with open('/kaggle/working/docstore.pkl', 'rb') as f:
    retriever_config = pickle.load(f)

retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=retriever_config['docstore'],
    id_key=retriever_config['id_key'],
)



llm = ChatOllama(model=CHAT_MODEL, temperature=0)

template = """Answer the question based only on the following context:
{context}
Question: {question}
"""

prompt = ChatPromptTemplate.from_template(template)
chain = (
    {"context": retriever, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

def request_response(query: str):
    return chain.invoke(query)
