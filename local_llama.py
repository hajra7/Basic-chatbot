from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_ollama import OllamaLLM as Ollama
import streamlit as st
import os
from dotenv import load_dotenv

load_dotenv()


## Langsmith tracking
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

##Prompt Template

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please answer the user's question in a concise manner."),
        ("user", "Question: {question}"),
    ]
)

##steamlit framework

st.title("LangChain Ollama Chatbot")
input_question = st.text_input("Enter your question:")

## OpenAI Chat Model

llm =Ollama(model="mistral")

output_parser = StrOutputParser()
chain= prompt | llm | output_parser

if input_question:
    st.write(chain.invoke({"question": input_question}))