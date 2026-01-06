# 🧠 Enhanced Q&A Chatbot (OpenAI & Ollama)

An interactive **Question–Answer Chatbot** built using **Streamlit + LangChain** that supports:

- ☁️ **Cloud-based LLMs (OpenAI GPT models)**
- 🖥️ **Local open-source LLMs (Ollama – Mistral)**
- 🔍 **LangSmith tracing & monitoring**
- 🎛️ Model & generation parameter controls

This project is ideal for learning **Generative AI application development** and can be extended to document QA, agents, and RAG systems.

---

## 🚀 Features

- Streamlit-based web UI
- Switch between **OpenAI** and **Ollama** models
- Adjustable temperature & max tokens
- Secure API key handling
- LangChain Expression Language (LCEL)
- LangSmith tracking enabled
- Fully modular & beginner-friendly

---

## 🧰 Tech Stack

- **Python**
- **Streamlit**
- **LangChain**
- **OpenAI API**
- **Ollama (local LLMs)**
- **LangSmith**
- **dotenv**

---

## 📂 Project Structure

1-QA-chatbot/
│
├── main.py # Main Streamlit application
├── requirements.txt
├── .env # API keys (not pushed to GitHub)
├── README.md
├── venv/
└── screenshots/ # Output screenshots (optional)


---

## 🔑 Environment Variables

Create a `.env` file in the root directory:

```env
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxxxx
LANGCHAIN_API_KEY=lsv2_xxxxxxxxxxxxx


How to Run (OpenAI Mode)
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run main.py

How to Run (Ollama Mode – Local)
1. Install Ollama

👉 https://ollama.com

2. Start Ollama server
ollama serve

3. Pull model
ollama pull mistral

4. Run the app
streamlit run main.py


