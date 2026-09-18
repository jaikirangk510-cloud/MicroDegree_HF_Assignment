"""
HuggingFace Inference Module
============================
Provides a clean interface for running inference using the
HuggingFace Inference API with proper error handling.
"""

import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

from config import get_api_key, get_model_config, logger

load_dotenv()


def create_client() -> InferenceClient:
    """Create and return an authenticated InferenceClient.

    Returns:
        Configured InferenceClient instance.

    Raises:
        ValueError: If the API key is not configured.
    """
    api_key = get_api_key()
    return InferenceClient(api_key=api_key)


def run_inference(
    prompt: str,
    model: str = None,
    client: InferenceClient = None,
) -> str:
    """Run inference using the HuggingFace Inference API.

    Args:
        prompt: The user prompt to send to the model.
        model: Optional model ID. Defaults to the configured inference model.
        client: Optional pre-configured client. Creates one if not provided.

    Returns:
        The model response as a string.

    Raises:
        ValueError: If the API key is not configured.
        RuntimeError: If the inference request fails.
    """
    if model is None:
        model = get_model_config("inference")["model_id"]

    if client is None:
        client = create_client()

    logger.info("Running inference with model: %s", model)

    try:
        completion = client.chat.completions.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
        )
        response = completion.choices[0].message.content
        logger.info("Inference completed successfully")
        return response

    except Exception as e:
        logger.error("Inference failed: %s", str(e))
        raise RuntimeError(f"Inference request failed: {e}") from e


if __name__ == "__main__":
    result = run_inference("How many Gs in huggingface?")
    logger.info("Result: %s", result)
