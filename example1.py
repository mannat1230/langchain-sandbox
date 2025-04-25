## Integrate code with OpenAI API
import os
from langchain.llms import OpenAI
from dotenv import load_dotenv
from langchain import PromptTemplate
from langchain.chains import LLMChain

from langchain.memory import ConversationBufferMemory

from langchain.chains import SequentialChain

import streamlit as st

os.getenv("OPENAI_API_KEY")

# Streamlit app

st.title('Celebrity Fun Facts Generator')
input_text = st.text_input("Search for a celebrity")

# Prompt templates

first_input_prompt=PromptTemplate(
    input_variables=["name"],
    template="Tell me an interesting and lesser-known fact about {name}."
)


## OpenAI LLMs

llm=OpenAI(temperature=0.8) #temperature is a parameter that controls the randomness of the model's output. A higher temperature (e.g., 0.8) makes the output more random, while a lower temperature (e.g., 0.2) makes it more focused and deterministic.
chain=LLMChain(llm=llm, prompt=first_input_prompt, verbose=True, output_key='fact')



# More prompt templates to create a chain of prompts

second_input_prompt=PromptTemplate(
    input_variables=["fact"],
    template="Tell me another person with a similar story to {fact}."
)

chain2=LLMChain(llm=llm, prompt=second_input_prompt, verbose=True, output_key='another_person')


third_input_prompt=PromptTemplate(
    input_variables=["another_person"],
    template="Name and short description of a book where the character has a similar story to {another_person}."
)

chain3=LLMChain(llm=llm, prompt=third_input_prompt, verbose=True, output_key='book')



chains=SequentialChain(chains=[chain, chain2, chain3], input_variables=['name'],
                             output_variables=['fact','another_person','book'],verbose=True)



if input_text:
    st.write(chains({'name':input_text}))

