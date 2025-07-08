# Basic Chatbot with LangChain, OpenAI & Ollama (Mistral)

This repository contains two chatbot applications powered by LangChain:

1. `app.py`: Uses **OpenAI** GPT models via LangChain
2. `local_llama.py`: Uses **local Mistral model** via **Ollama** and LangChain

Both apps feature a simple Streamlit interface and demonstrate how to work with LLMs using LangChain's modular API.


##  Tech Stack

- [LangChain](https://github.com/langchain-ai/langchain)
- [Streamlit](https://streamlit.io/)
- [OpenAI API](https://platform.openai.com/)
- [Ollama](https://ollama.com/) for local LLMs like Mistral, LLaMA, DeepSeek, etc.
- `.env` file management using `python-dotenv`


##  Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/hajra7/Basic-chatbot.git
cd Basic-chatbot
```

#### 2. Create & Activate Virtual Environment

```bash
python -m venv .myvenv
# Windows
.myvenv\Scripts\activate
```

### 3. Install Required Packages

```bash
pip install -r requirements.txt
 ```

### 4. Setup .env File
Create a .env file in the root directory:

 ```env
 OPENAI_API_KEY=your_openai_key_here
LANGCHAIN_API_KEY=your_langsmith_key_here
```
##  How to run the app

### Run app.py (OpenAI-based Chatbot)

```bash
streamlit run app.py
```
### Run local_llama.py (Ollama + Mistral-based Chatbot)

### Step 1: Install Ollama

### Step 2: Pull the model

```cmd
ollama run mistral
```
### Step 3: Run the app 

```bash
streamlit run local_llama.py
```
## Project structure

```bash
Basic-chatbot/
│
├── app.py                  # OpenAI chatbot
├── local_llama.py          # Ollama (Mistral) chatbot
├── requirements.txt
├── .env                    # Environment variables
├── .gitignore
└── README.md
```





