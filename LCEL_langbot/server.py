# Importing Libraries
from fastapi import FastAPI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langserve import add_routes
import os
from dotenv import load_dotenv

load_dotenv()

# Groq Api key and loading the model
groq_api_key=os.getenv("GROQ_API_KEY")
llm=ChatGroq(model="Gemma2-9b-It",groq_api_key=groq_api_key)

# Chat prompt
generic_tempt="Answer the question in {language} Language."
prompt=ChatPromptTemplate.from_messages(
    [
        ("system",generic_tempt), ("user","{text}")
    ]
)

# Output parser
parser=StrOutputParser()

# Chain
chain=prompt|llm|parser

# App
app=FastAPI(title="All Language Model",version="1.0",description="A API server for All Language Model")
add_routes(
    app,
    chain,
    path="/chain"
)

if __name__== "__main__":
    import uvicorn
    uvicorn.run(app,host="127.0.0.1",port=8000)