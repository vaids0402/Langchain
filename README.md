# 📄 PDF Question Answering using RAG (LangChain + Groq)

## 📌 Overview
This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using **LangChain** that allows users to ask questions based on the content of **PDF documents**.  
The system retrieves relevant context from uploaded PDFs and uses a **Groq-hosted LLM** to generate accurate, context-aware answers.

---

## 🚀 Features
- Ingests and processes **PDF documents**
- Retrieves relevant chunks using **vector similarity search**
- Uses **Retrieval-Augmented Generation (RAG)** for grounded answers
- Powered by **Groq LLMs (LLaMA 3)**
- Modular and extensible **LangChain-based architecture**
- Secure API key handling using **environment variables**

---

## 🛠️ Tech Stack
- **Python**
- **LangChain**
- **Groq LLM (LLaMA 3)**
- **Vector Store** (FAISS / Chroma – configurable)
- **PyPDFLoader**
- **dotenv**

---

## 🔧 Installation & Setup

### 1️⃣ Clone the repository
```bash
git clone https://github.com/vaids_0402/Langchain.git
cd Langchain
```

### 2️⃣ Create a virtual environment
```bash
python -m venv .venv
source .venv/bin/activate  ## Mac/Linux
.venv\Scripts\activate   ## Windows
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Set environment variables
```bash
## Create an .env file in the project root
GROQ_API_KEY=your_groq_api_key_here
```

---

## 🎯 Use Cases
- Academic research assistance
- Document-based Q&A systems
- Internal knowledge bases
- Legal / business document analysis

---

## 🚧 Future Enhancements
- Web UI using **Streamlit** / **FastAPI**
- Source citation for answers
- Multi-document comparison
- Conversational memory
- Deployment on cloud platforms
