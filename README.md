# Gen-AI-tasks-and-projects              

Welcome to the Gen-AI Tasks and Projects repository! This collection highlights various tasks and           
projects centered around generative AI that I have learned and practiced by exploring different techniques.         

### Overview   
This repository contains several tasks and projects that explore different aspects of generative AI (mainly LLMs).      
The projects vary in scope and aim to showcase practical applications. Key projects and tasks include AIra-v0.1,        
Lemansbot, Languagebot, and many more.          

### API/Tools used          
- LangChain     
- Hugging Face      
- OpenAI            
- Groq          
- Ollama  
- Check requirements.txt for libraries used for python          

### langchain_intro
In this directory, all files shows practical implementations of Document loading, Text Splitting, Embeddings and        
Vector Store Databases. I used open source and paid embeddings of Hugging face, Ollama and OpenAI.                  

### simple_chatbot_rag
All techniques such as prompting, Retrieval-augmented generation(RAG) and using Open Source/paid models. I also traced the         
responses in LangSmith for experimental tracking.            

### LCEL_langbot
Prompted the model using more parameters for getting response in targetted language. I also used StrOutputParser for better             
parsing the response of the model.          

### chat_history
Added chat history to the chain for improved context handling and maintaining a more coherent conversation flow in the AI's         
responses, allowing the assistant to better understand and reference previous interactions during a session.        

### AIra_and_lemansbot
Built AIra-v0.1 which is assistant which many open source collection of LLMs. Developed a streamlit app for UI and changeable       
parameters like temperature and max tokens. Also developed lemansbot which uses chat history and rag for answering simple lemans        
questions.