from langchain.prompts import PromptTemplate

# Function to create and return a prompt template
def get_prompt():
    # Define the prompt template
    prompt_templet = """
    You are a customer service chatbot

    {context}

    Answer the customer's questions only using the source data provided. 
    If you are unsure, say "I don't know, please call our customer support". 
    Use engaging, courteous, and professional language similar to a customer representative.
    Keep your answers concise.

    Generate the answer only for the given question. Do not generate extra text

    Question: {question}

    Answer:
    """

    # Create a PromptTemplate instance
    prompt = PromptTemplate(
    template = prompt_templet,
    input_variables = ["context","question"]
    )
    
    return prompt