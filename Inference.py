import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

hf_api_key = os.getenv("HF_API_KEY")

client = InferenceClient(api_key=hf_api_key)

completion = client.chat.completions.create(
    model="openai/gpt-oss-120b",
    messages=[
        {
            "role": "user",
            "content": "How many 'G's in 'huggingface'?"
        }
    ],
)

print(completion.choices[0].message.content)
