'''
Simple Chat Bot - Q-n-A ChatBot
'''

from langchain.llms import OpenAI
from langchain_community.chat_models import ChatOpenAI
from langchain.schema import AIMessage, HumanMessage

from dotenv import load_dotenv
import os

load_dotenv() # Taking Environment Variables from .env

import streamlit as st


# Function to load OpenAI model and get responses
def get_openai_response(question):
    llm = ChatOpenAI(
        openai_api_key=os.getenv("OPENAI_API_KEY"),
        model="gpt-3.5-turbo",  # Specifying the model
        temperature=0.5
    )

    # Passing the input as a list of BaseMessages
    messages = [HumanMessage(content=question)]
    response = llm(messages)

    return response.content


# Initializing Streamlit Application
st.set_page_config(
    page_title = "Q-n-A Demo"
)

st.header("LangChain Application")

# Streamlit input handling
input_text = st.text_input("Input:", key="input")
submit = st.button("Ask a Question") # Submit button

if submit:
    if input_text.strip():  # Ensuring the input isn't empty
        try:
            response = get_openai_response(input_text)
            st.subheader("The Response is :")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.error("Please enter a question.")

