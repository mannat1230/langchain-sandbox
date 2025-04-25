## Integrate code with OpenAI API
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv

import streamlit as st

os.getenv("OPENAI_API_KEY")

# Streamlit app

st.title('Langchain Demo with OpenAI API')
input_text = st.text_input("Search for a topic")

## OpenAI LLMs

llm=OpenAI(temperature=0.8) #temperature is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 0.8) makes the output more random, while a lower temperature (e.g., 0.2) makes it more focused and deterministic.


if input_text:
    st.write(llm(input_text))

