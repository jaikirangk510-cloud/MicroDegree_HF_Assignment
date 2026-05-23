# Introduction to HuggingFace

About the Project
This project introduces to the fundamentals of working with Large Language Models using the HuggingFace ecosystem and LangChain framework. Unlike traditional programming exercises, this project focuses on how to access, configure, and interact with AI models using industry-standard tools.
Students will explore two primary approaches to LLM inference:
Cloud Inference — Send prompts to models hosted on remote servers via the HuggingFace Inference API

Technologies Used

LangChain-HuggingFace
HuggingFaceEndpoint, ChatHuggingFace, HuggingFacePipeline
HuggingFace Hub
Cloud-based model access via Inference API

Python-dotenv
Secure API key management

Project Structure
Huggingface_proj/
├── .env                # HuggingFace API key
├── cloud.py            # Cloud-based inference with HuggingFaceEndpoint
└── README.md

Setup & Installation
1. Create virtual environment
python -m venv .venv

2. Activate virtual environment
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

# Windows (Git Bash)
source .venv/Scripts/activate

# Linux/macOS
source .venv/bin/activate

3. Install dependencies
pip install langchain-huggingface langchain-core transformers torch python-dotenv

4. Configure API key
Create a .env file in the project directory:
HUGGING_FACE_API = "your_huggingface_api_token_here"

Get your token from huggingface.co/settings/tokens
5. Run the scripts
python cloud.py    # Cloud inference
