import os
import textwrap
import streamlit as st

import langchain

from langchain.chains import RetrievalQA

from src.langchain_llm import get_llm
from src.vectorDB_retriever import get_embeddings
from src.prompt_template import get_prompt

# from langchain_llm import get_llm
# from vectorDB_retriever import get_embeddings
# from prompt_template import get_prompt


file = "vector_database_file"

def get_chain():
    
    llm = get_llm()
    embeddings = get_embeddings()
    retriever = embeddings.as_retriever(search_kwargs={"k": 1})
    prompt = get_prompt()
    
    chain = RetrievalQA.from_chain_type(
        
        llm = llm,
        chain_type = "stuff",
        retriever = retriever,
        input_key = "query",
        return_source_documents = True,
        chain_type_kwargs = {"prompt":prompt}
    
    )
    
    return chain


# def __main__():
chain = get_chain()

question = "I received a damaged product."
print(question)
response = chain.invoke(question)
print(response['result'])

    # st.title("Custom chatbot")

    # question = st.text_area("Enter your question here: ")

    # if st.button("Submit"):
    #     response = chain.invoke(question)
        
    #     st.write(response['result'])
