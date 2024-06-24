import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI

# Function to load the language model
def get_llm():
    # Load environment variables
    print("Loading Environment Variables")
    load_dotenv()

    # Load the LLM module from Langchain
    print("Loading LLM Module from Langchain")
    llm = ChatGoogleGenerativeAI(
        model="gemini-pro",
        google_api_key=os.environ["GOOGLE_API_KEY"],
        temperature=0.1
    )
    
    return llm
