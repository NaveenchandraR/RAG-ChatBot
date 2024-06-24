import streamlit as st
from src.run_chain import get_chain

chain = None

if chain == None:
    chain = get_chain()

st.title("Hi, This is your friendly Chat-Bot")

question = st.text_area("Please Enter your question here: ")

if st.button("Submit"):
    response = chain.invoke(question)
    
    st.write(response['result'])
