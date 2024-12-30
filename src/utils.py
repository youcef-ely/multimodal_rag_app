import os
import uuid
import yaml
import pickle
import base64
from IPython.display import Image, display
from langchain.schema.document import Document

# Global constant for ID key
ID_KEY = "doc_id"

def load_config() -> dict:
    """
    Load configuration from a YAML file.

    Args:
        config_file (str): Path to the YAML configuration file.

    Returns:
        dict: Parsed configuration data as a dictionary.
    """

    current_dir = os.path.dirname(os.path.abspath(__file__))
    # Navigate to the parent directory and construct the path to config.yaml
    config_path = os.path.join(current_dir, '..', 'config.yaml')

    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
    return config


def display_base64_image(base64_code: str) -> None:
    """
    Display an image encoded in Base64.

    Args:
        base64_code (str): Base64-encoded image data.

    Returns:
        None
    """
    image_data = base64.b64decode(base64_code)
    display(Image(data=image_data))


def load_from_pickle(filename: str):
    """
    Load an object from a pickle file.

    Args:
        filename (str): Path to the pickle file.

    Returns:
        Any: The object loaded from the pickle file.
    """
    with open(filename, "rb") as file:
        return pickle.load(file)


def save_to_pickle(obj: object, filename: str) -> None:
    """
    Save an object to a pickle file.

    Args:
        obj (object): The object to save.
        filename (str): Path to the output pickle file.

    Returns:
        None
    """
    with open(filename, "wb") as file:
        pickle.dump(obj, file, pickle.HIGHEST_PROTOCOL)


def generate_ids(items: list) -> list:
    """
    Generate unique UUIDs for a list of items.

    Args:
        items (list): List of items to generate IDs for.

    Returns:
        list: List of unique UUID strings.
    """
    return [str(uuid.uuid4()) for _ in items]


def create_documents(items: list, ids: list, summaries: list) -> tuple:
    """
    Create Document objects and their summaries.

    Args:
        items (list): List of document contents.
        ids (list): List of unique document IDs.
        summaries (list): List of summary contents.

    Returns:
        tuple: A tuple containing two lists:
            - List of Document objects with full content.
            - List of Document objects with summary content.
    """
    if len(items) != len(ids) or len(items) != len(summaries):
        raise ValueError("Length of items, IDs, and summaries must be equal.")
    
    docs = [
        Document(page_content=text, metadata={ID_KEY: ids[i]})
        for i, text in enumerate(items)
    ]
    summary_docs = [
        Document(page_content=summary, metadata={ID_KEY: ids[i]})
        for i, summary in enumerate(summaries)
    ]
    return docs, summary_docs
