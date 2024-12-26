# Multimodal RAG System for PDF Analysis
This project is an implementation of a **multimodal retrieval-augmented generation (RAG)** model based on the research paper titled  ### [🔗 Towards an Intelligent Model for Dysgraphia Evolution Tracking](https://hal.science/hal-04593939/) which was presented at the 28th International Conference on Knowledge-Based and Intelligent Information & Engineering Systems (KES 2024). The research paper explored a machine learning model for dysgraphia detection and tracking. 

In this implementation, we implemented a RAG system to retrieve and process information from diverse sources, including **images**, **tables**, and **texts**. The system is capable of leveraging retrieval techniques to generate relevant responses based on the retrieved data.

## Overview

The system leverages the power of a retrieval-augmented generation approach, which allows us to combine both retrieval and generation for information synthesis. This project aims to retrieve data from multiple data sources (images, tables, and texts) and use it in conjunction with the learned model to provide relevant outputs based on the input queries.

## Features

- **Text Retrieval**: Use a vector search model to retrieve relevant textual data from a large corpus.
- **Table Retrieval**: Extract information from structured tables and process it into useful insights.
- **Image Retrieval**: Employ image-based models to retrieve and analyze image data.
- **Integrated Generation**: Combine the retrieved information with generation models to provide detailed and coherent responses.

## **Important Note**

Before running the system, make sure to adapt the file paths (such as data directories) and API keys (like Groq API keys) according to your local environment. These configurations are necessary for correct data handling and API access.

Also, please note that this project was implemented on **Kaggle** due to its available large GPU and RAM capacities, which were crucial for handling the resource-intensive operations required by the RAG model.

## Dependencies

To install the necessary dependencies for the project, you can either run the following commands directly or use the `requirements.txt` file. 

### Direct Installation:

Run the following commands:

```bash
!pip install -Uq "unstructured[all-docs]" pillow lxml pillow --quiet --progress-bar off
!pip install -Uq chromadb tiktoken --quiet --progress-bar off
!pip install -Uq langchain langchain-community langchain-groq --quiet --progress-bar off
!pip install -Uq python_dotenv --quiet --progress-bar off
!sudo apt-get install poppler-utils tesseract-ocr libmagic-dev
!pip install langchain_huggingface --quiet
!pip install langchain-chroma --quiet
```

or 

```bash
!python install_packages.py
```

Please refer to [Ollama's repository](https://github.com/ollama/ollama) to install and download the models.