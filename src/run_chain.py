import langchain
from langchain.chains import RetrievalQA
from src.langchain_llm import get_llm
from src.vectorDB_retriever import get_embeddings
from src.prompt_template import get_prompt

# Function to create and return the RetrievalQA chain
def get_chain():
    # Get the language model
    llm = get_llm()
    
    # Get the embeddings and convert them to a retriever
    embeddings = get_embeddings()
    retriever = embeddings.as_retriever(search_kwargs={"k": 1})
    
    # Get the prompt template
    prompt = get_prompt()
    
    # Create the RetrievalQA chain
    chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        input_key="query",
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt}
    )
    
    return chain
