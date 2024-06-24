# Llama-2-chat

This repository contains the code for a customer service chatbot built using LangChain, Streamlit, and various other libraries. The chatbot uses a language model to generate responses based on provided source data, ensuring accurate and professional customer support.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Components](#components)
- [Contributors](#contributors)
- [License](#license)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/NaveenchandraR/RAG-ChatBot.git
    cd chatbot
    ```

2. Create and activate a virtual environment:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Set up environment variables:

    - Create a `.env` file in the root directory of the project.
    - Add your Google API key to the `.env` file:

        ```bash
        GOOGLE_API_KEY=your_google_api_key_here
        ```

5. Create a Google Gemini API key at [Gemini-API](https://ai.google.dev/gemini-api/docs/api-key)

## Usage

1. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

2. Open the provided URL in your web browser.

3. Enter your question in the text area and click the "Submit" button to get a response from the chatbot.

4. Alternatively, a Jupyter Notebook is provided where you can run all the functions to test.

## Project Structure

- `app.py`: Main file to run the Streamlit application.
- `src/`: Contains all source code for the project.
  - `run_chain.py`: Contains the `get_chain` function to create the RetrievalQA chain.
  - `langchain_llm.py`: Contains the `get_llm` function to load the language model.
  - `vectorDB_retriever.py`: Contains the `get_embeddings` function to retrieve document embeddings.
  - `prompt_template.py`: Contains the `get_prompt` function to create the prompt template.
- `data/`: Directory to store the data files (e.g., `Customer-Support.csv`).

## Components

### `chatbot.py`

Main file to run the Streamlit application. It initializes the chain and handles user input.

```python
import streamlit as st
from src.run_chain import get_chain

chain = None

if chain is None:
    chain = get_chain()

st.title("Hi, This is your friendly Chat-Bot")

question = st.text_area("Please Enter your question here:")

if st.button("Submit"):
    response = chain.invoke(question)
    st.write(response['result'])
```
## Contributors

- [Naveen Chandra](https://www.linkedin.com/in/naveen-chandra-r-7230aa192)

## License

This project is licensed under the [MIT License](link-to-license-file).
