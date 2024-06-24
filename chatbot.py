import streamlit as st
from src.run_chain import get_chain

# Initialize the chain variable
chain = None

# Load the chain if it is not already loaded
if chain is None:
    chain = get_chain()

# Set the title of the Streamlit app
st.title("Hi, This is your friendly Chat-Bot")

# Create a text area for user input
question = st.text_area("Please Enter your question here:")

# Create a submit button
if st.button("Submit"):
    # Invoke the chain with the user's question and get the response
    response = chain.invoke(question)
    
    # Display the response
    st.write(response['result'])
