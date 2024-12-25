from langchain_chroma import Chroma
from langchain_ollama import ChatOllama
from langchain.storage import InMemoryStore
from langchain_ollama import OllamaEmbeddings
from langchain_core.messages import HumanMessage
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain.retrievers.multi_vector import MultiVectorRetriever

# Initialize embeddings
embeddings = OllamaEmbeddings(model='llama3')

# Load the existing Chroma DB
vectorstore = Chroma(persist_directory='../data/chroma_db', embedding_function=embeddings)

# Initialize the in-memory document store
store = InMemoryStore()
id_key = "doc_id"

# Create the MultiVectorRetriever
retriever = MultiVectorRetriever(
    vectorstore=vectorstore,
    docstore=store,
    id_key=id_key,
)

# Initialize ChatOllama model
llm = ChatOllama(model="llama2:13b-chat", temperature=0)

# Define the chat function
def chat(question: str) -> str:
    # Prompt template
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
    response = chain.invoke(question)
    return response


