import os
from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_core.messages import HumanMessage
load_dotenv()

hf_api_key = os.getenv("HUGGING_FACE_API")

llm = HuggingFaceEndpoint(
    repo_id = "Qwen/Qwen2.5-7B-Instruct",
    huggingfacehub_api_token=hf_api_key,
    task = "conversational",
    max_new_tokens = 256,
    temperature = 0.6,
    top_k = 100,
    top_p = 0.9
)

chat_model = ChatHuggingFace(llm=llm)

messages = [HumanMessage(content="Can you explain at what you are expert at?")]
response = chat_model.invoke(messages)
print(response.content)