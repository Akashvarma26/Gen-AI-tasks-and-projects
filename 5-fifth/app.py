# Importing Libraries
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
import streamlit as st
import os
from dotenv import load_dotenv
load_dotenv()

# Setiing up API keys and tracing in langchain
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_PROJECT"]="Simple QA chatbot using groq api"
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")
# Chat prompt template
prompt=ChatPromptTemplate.from_messages(
    [
        ("system","You are 'AIra' a helpful assistant. Please response to the user."),
        ("user","Question:{question}")
    ]
)

# Function to generate text using models,temperature,max tokens,etc
def generate_text(question,engine,temperature,max_tokens):
    llm=ChatGroq(model=engine,temperature=temperature,max_tokens=max_tokens)
    output_parser=StrOutputParser()
    chain=prompt|llm|output_parser
    response=chain.invoke({"question":question})
    return response

# Streamlit App
st.title("𝙰𝙸𝚛𝚊-v0.1 : 𝙷𝚎𝚕𝚙𝚏𝚞𝚕 𝙰𝙸 𝙰𝚜𝚜𝚒𝚜𝚝𝚊𝚗𝚝")
st.sidebar.title("Settings")
engine=st.sidebar.selectbox("Select models",["llama-3.1-8b-instant","gemma2-9b-it","mixtral-8x7b-32768"])
temperature=st.sidebar.slider("Temperature",min_value=0.0,max_value=2.0,value=1.0)
max_tokens = st.sidebar.slider("Max Tokens", min_value=50, max_value=500, value=150)
st.write("Ask any question")
user_input=st.text_input("You:")
if user_input:
    response=generate_text(user_input,engine,temperature,max_tokens)
    st.write(response)