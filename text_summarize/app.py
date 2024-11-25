# Importing required libraries
import validators, streamlit as st
from langchain.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
from langchain_community.document_loaders import YoutubeLoader,WebBaseLoader
import os
from dotenv import load_dotenv
load_dotenv()
os.environ["GROQ_API_KEY"]=os.getenv("GROQ_API_KEY")

# Streamlit App
st.set_page_config("Any Link Summarizer","🤖")
st.title("Any Link Summarizer")
st.subheader("Summarize URL")
llm=ChatGroq(model="llama-3.1-70b-versatile")
prompt_template="""
Provide the summary of the following content in 500 words.\n\n
content:{text}
"""
prompt=PromptTemplate(template=prompt_template,input_variables=["text"])
gen_url=st.text_input("URL",label_visibility="collapsed").strip()
if st.button("Summarize"):
    if not gen_url:
        st.error("Please enter the URL in the text box")
    elif not validators.url(gen_url):
        st.error("Please enter correct URL (Any Youtube/websites links)")
    else:
        try:
            with st.spinner("Summarizing..."):
                if "youtube.com" in gen_url:
                    loader=YoutubeLoader.from_youtube_url(gen_url,add_video_info=False)
                else:
                    loader=WebBaseLoader(gen_url,verify_ssl=True)
                docs=loader.load()
                # Chain
                chain=load_summarize_chain(llm,chain_type="stuff",prompt=prompt)
                output=chain.run(docs)
                st.success(output)
        except Exception as e:
            st.exception(f"Exception:{e}")