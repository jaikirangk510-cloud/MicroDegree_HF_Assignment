import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint

load_dotenv()

hf_api_key = os.getenv("HUGGING_FACE_API")

llm = HuggingFaceEndpoint(
  repo_id="lmsys/vicuna-7b-v1.5",
  huggingfacehub_api_token=hf_api_key,
  task = "text-generation",
  max_new_tokens = 512,
  temperature = 0.7,
  top_k = 40,
  top_p = 0.7
)

response = llm.invoke("tell me why rust language is used in embedded systems")

print(response)