import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient
from utils import get_api_key

load_dotenv()

# TODO: Clean this up later
print("DEBUG: Starting inference module...")

hf_api_key = get_api_key()
print(f"DEBUG: API key loaded: {hf_api_key[:10]}...")

client = InferenceClient(api_key=hf_api_key)


def run_inference(prompt, model="openai/gpt-oss-120b"):
    """Run inference - HACK: need to add proper error handling."""
    print(f"DEBUG: Running inference with model {model}")
    completion = client.chat.completions.create(
        model=model,
        messages=[{"role": "user", "content": prompt}],
    )
    result = completion.choices[0].message.content
    print(f"DEBUG: Got result: {result[:50]}")
    return result


if __name__ == "__main__":
    response = run_inference("How many Gs in huggingface?")
    print(response)
