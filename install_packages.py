import os

commands = [
    'pip install -Uq "unstructured[all-docs]" pillow lxml pillow --quiet --progress-bar off',
    'pip install -Uq chromadb tiktoken --quiet --progress-bar off',
    'pip install -Uq langchain langchain-community langchain-groq --quiet --progress-bar off',
    'pip install -Uq python_dotenv --quiet --progress-bar off',
    'sudo apt-get install poppler-utils tesseract-ocr libmagic-dev'
]

for command in commands:
    os.system(command)
