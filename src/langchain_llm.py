import os
from dotenv import load_dotenv

from langchain_google_genai import ChatGoogleGenerativeAI


def get_llm():

    print(f"Loading Environment Variables")
    load_dotenv()

    print(f"Loading LLM Module from Langchain")
    llm = ChatGoogleGenerativeAI(model="gemini-pro",google_api_key = os.environ["GOOGLE_API_KEY"],temperature = 0.1)
    return llm