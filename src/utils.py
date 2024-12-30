import uuid
import yaml 
import pickle
import base64
from IPython.display import Image, display
from langchain.schema.document import Document


id_key = "doc_id"


def load_config(config_file): 
    with open(config_file, 'r') as file: 
        config = yaml.safe_load(file) 
        return config


def display_base64_image(base64_code):
    image_data = base64.b64decode(base64_code)
    display(Image(data=image_data))


def load_from_pickle(filename):
    with open(filename, "rb") as file:
        return pickle.load(file)

def save_to_pickle(obj, filename):
    with open(filename, "wb") as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)

def generate_ids(items):
    return [str(uuid.uuid4()) for _ in items]

def create_documents(items, ids, summaries):
    docs = [Document(page_content=text, metadata={id_key: ids[i]}) for i, text in enumerate(items)]
    summary_docs = [Document(page_content=summary, metadata={id_key: ids[i]}) for i, summary in enumerate(summaries)]
    return docs, summary_docs
   