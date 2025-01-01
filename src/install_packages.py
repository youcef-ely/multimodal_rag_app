import os
import subprocess
from tqdm import tqdm
os.environ['PYTHONWARNINGS'] = 'ignore'


commands = [
    'pip install -Uq "unstructured[all-docs]" pillow lxml pillow --quiet --progress-bar off',
    'pip install -Uq chromadb tiktoken --quiet --progress-bar off',
    'pip install -Uq langchain langchain-community langchain-groq --quiet --progress-bar off',
    'pip install -Uq python_dotenv --quiet --progress-bar off',
    'sudo apt-get install poppler-utils tesseract-ocr libmagic-dev',
    'pip install langchain_huggingface --quiet --progress-bar off',
    'pip install langchain-chroma --quiet --progress-bar off',
    'pip install streamlit --quiet --progress-bar off',
    'pip install -U langchain-ollama --quiet',
    'pip install evaluate rouge_score --quiet',
    'pip install pretty_errors --quiet',
]

for command in tqdm(commands, desc='Installing packages'):
    subprocess.run(command, shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
