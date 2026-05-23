# 🤗 Introduction to HuggingFace

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?logo=python&logoColor=white)
![LangChain](https://img.shields.io/badge/LangChain-HuggingFace-orange?logo=chainlink&logoColor=white)
![HuggingFace](https://img.shields.io/badge/HuggingFace-Inference%20API-yellow?logo=huggingface&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 About the Project

This project introduces the fundamentals of working with **Large Language Models (LLMs)** using the **HuggingFace ecosystem** and **LangChain framework**. Unlike traditional programming exercises, this project focuses on how to **access**, **configure**, and **interact** with AI models using industry-standard tools.

Students will explore the following approach to LLM inference:

- ☁️ **Cloud Inference** — Send prompts to models hosted on remote servers via the HuggingFace Inference API

---

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| `langchain-huggingface` | `HuggingFaceEndpoint`, `ChatHuggingFace`, `HuggingFacePipeline` |
| `HuggingFace Hub` | Cloud-based model access via Inference API |
| `python-dotenv` | Secure API key management |

---

## 📁 Project Structure

```
Huggingface_proj/
├── .env          # HuggingFace API key
├── cloud.py      # Cloud-based inference with HuggingFaceEndpoint
└── README.md
```

---

## 🚀 Setup & Installation

### 1. Create Virtual Environment

```bash
python -m venv .venv
```

### 2. Activate Virtual Environment

**Windows (PowerShell):**
```bash
.venv\Scripts\Activate.ps1
```

**Windows (Git Bash):**
```bash
source .venv/Scripts/activate
```

**Linux / macOS:**
```bash
source .venv/bin/activate
```

### 3. Install Dependencies

```bash
pip install langchain-huggingface langchain-core transformers torch python-dotenv
```

### 4. Configure API Key

Create a `.env` file in the project root directory:

```env
HUGGING_FACE_API = "your_huggingface_api_token_here"
```

> 🔑 Get your token from [huggingface.co/settings/tokens](https://huggingface.co/settings/tokens)

### 5. Run the Script

```bash
python cloud.py
```

---

## 📄 License

This project is licensed under the [MIT License](LICENSE).
