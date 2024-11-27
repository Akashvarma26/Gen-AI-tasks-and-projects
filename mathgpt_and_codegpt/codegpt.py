# Importing required libraries
import streamlit as st
from langchain_huggingface import HuggingFaceEndpoint
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain

# Streamlit app configuration
st.set_page_config(
    page_title="CodeGPT",
    page_icon="💻"
)
st.title("💻 CodeGPT : Coding Assistant")

# Wrap the Hugging Face pipeline in HuggingFacePipeline for LangChain
llm = HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-Coder-32B-Instruct",temperature=0.6)

# Prompt for solving code questions
prompt = """
You are 'CodeGPT' a highly capable coding assistant developed by Akash Varma Datla. Provide text or code based on questions asked by users. Solve the problems in asked programming language or python by default.
Add the text which are not code and explaination outside the code block
\n
Question: {question}

Answer:
"""

# Create a PromptTemplate
prompt_template = PromptTemplate(
    input_variables=["question"],
    template=prompt
)

# LLMChain to handle code generation
code_chain = LLMChain(
    llm=llm,
    prompt=prompt_template
)

# Chat History setup
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I'm a CodeGPT a coding assistant who can solve programming questions and explain the solutions."}
    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

# Input for coding question
question = st.text_area(
    "Enter your coding question:", 
    "Write a Python function to calculate the factorial of a number."
)

# Handle the button click to generate the solution
if st.button("Solve My Code Question"):
    if question:
        with st.spinner("Generating solution..."):
            st.session_state.messages.append({"role": "user", "content": question})
            st.chat_message("user").write(question)

            # Generate the response using the chain
            response = code_chain.run({"question": question})
            st.session_state.messages.append({"role": "assistant", "content": response})

            st.write("### Solution:")
            st.code(response)  
    else:
        st.warning("Please enter your coding question.")
