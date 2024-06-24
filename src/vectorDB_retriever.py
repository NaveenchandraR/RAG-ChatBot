import os

from langchain_community.document_loaders.csv_loader import CSVLoader
from langchain_text_splitters import CharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_chroma import Chroma


abspath = os.path.abspath('run_chat.py')
dname = os.path.dirname(abspath)


def get_embedding_method():
    model_name = "sentence-transformers/all-MiniLM-L6-v2"
    embedding_function = HuggingFaceEmbeddings(model_name=model_name)
    return embedding_function


def get_docs():
    # Load documents locally as CSV
    loader = CSVLoader(f'{dname}/data/Customer-Support.csv')
    docs = loader.load()

    # Split document into text chunks
    text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=0)
    docs = text_splitter.split_documents(docs)

    return docs


def get_embeddings():
    print("Loading Document")
    docs = get_docs()

    print("Loading Embedding Function")
    embedding_function = get_embedding_method()
    
    print("Creating Vector DB")
    db = Chroma.from_documents(docs, embedding_function)

    return db