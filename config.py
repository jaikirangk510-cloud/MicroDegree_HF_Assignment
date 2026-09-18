"""
Configuration module for the MicroDegree HF Assignment.

Provides centralized configuration management using
environment variables and sensible defaults.
"""

import os
import logging
from dotenv import load_dotenv

load_dotenv()

# Configure structured logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)
logger = logging.getLogger("hf_assignment")


# Supported model configurations
SUPPORTED_MODELS = {
    "inference": {
        "model_id": "openai/gpt-oss-120b",
        "task": "conversational",
    },
    "chat": {
        "model_id": "Qwen/Qwen2.5-7B-Instruct",
        "task": "conversational",
    },
    "cloud": {
        "model_id": "lmsys/vicuna-7b-v1.5",
        "task": "text-generation",
    },
}

# Default generation parameters
DEFAULT_PARAMS = {
    "max_new_tokens": 256,
    "temperature": 0.6,
    "top_k": 100,
    "top_p": 0.9,
}


def get_api_key(env_var: str = "HF_API_KEY") -> str:
    """Retrieve the HuggingFace API key from environment variables.

    Args:
        env_var: Name of the environment variable to read.

    Returns:
        The API key string.

    Raises:
        ValueError: If the key is not set or is empty.
    """
    api_key = os.getenv(env_var)
    if not api_key:
        logger.error("API key not found in environment variable: %s", env_var)
        raise ValueError(
            f"{env_var} not found. Please set it in your .env file.\n"
            f"Example: {env_var}=hf_your_key_here"
        )
    logger.info("API key successfully loaded from %s", env_var)
    return api_key


def get_model_config(model_type: str) -> dict:
    """Get the configuration for a specific model type.

    Args:
        model_type: One of 'inference', 'chat', or 'cloud'.

    Returns:
        Dictionary with model_id and task.

    Raises:
        ValueError: If the model type is not supported.
    """
    if model_type not in SUPPORTED_MODELS:
        raise ValueError(
            f"Unsupported model type: {model_type}. "
            f"Choose from: {list(SUPPORTED_MODELS.keys())}"
        )
    return SUPPORTED_MODELS[model_type]
