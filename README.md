# 🤖 Gen-AI-tasks-and-projects              

Welcome to the Gen-AI Tasks and Projects repository! This collection highlights various tasks and projects centered around generative AI that I have learned and practiced by exploring different techniques.         
        
### 🔍 Overview   
This repository contains several tasks and projects that explore different aspects of generative AI (mainly LLMs). The projects vary in scope and aim to showcase practical applications. Key projects and tasks include AIra-v0.1, Lemansbot, Languagebot, and many more.          

### ⚒️ API/Tools used          
- LangChain     
- Hugging Face      
- OpenAI            
- Groq          
- Ollama  
- Check requirements.txt for libraries used for python          

### 📁 : langchain_intro
In this directory, all files shows practical implementations of Document loading, Text Splitting, Embeddings and Vector Store Databases. I used open source and paid embeddings of Hugging face, Ollama and OpenAI.                  

### 📁 : simple_chatbot_rag
All techniques such as prompting, Retrieval-augmented generation(RAG) and using Open Source/paid models. I also traced the responses in LangSmith for experimental tracking.            

### 📁 : LCEL_langbot
Prompted the model using more parameters for getting response in targetted language. I also used StrOutputParser for better parsing the response of the model.          

### 📁 : chat_history
Added chat history to the chain for improved context handling and maintaining a more coherent conversation flow in the AI's responses, allowing the assistant to better understand and reference previous interactions during a session.        

### 📁 : AIra_and_lemansbot
Built AIra-v0.1 which is assistant which many open source collection of LLMs. Developed a streamlit app for UI and changeable parameters like temperature and max tokens. Also developed lemansbot which uses chat history and rag for answering simple lemans questions.          

### 📁 : Tools_and_agents
Used different types of tools like SQL, Arxiv, wikipedia and custom ones and intialized Agents to use them.                 

### 📁 : text_summarize
Used load_summarize_chain function to use different types of summarizing techniques for bigger text/pdf contents. Also created a project to summarize youtube links using youtube tool.            
                
### 📁 : mathgpt_and_codegpt
Developed MathGPT using tools, agents and LLMMath chains to solve mathematical problems. Also developed CodeGPT using Qwen2.5-Coder-32B-Instruct to solve coding problems.  

### 📁 : multi_agents_crewai
Developed multi agent app to get info from youtube content and create it into a blog using yt tool using crewai library. It uses two agents one for researching and one for writing the blog.

### 📁 : hybrid_serach_rag
Used pinecone Vector DB(Cloud service db) to perform hybrid search (Sparse and Dense). Used TFIDF(Sparse) and HF Embeddings(Dense) for Keyword and Semantic search techniques. Ranked them using Reciprocal Rank Fusion.