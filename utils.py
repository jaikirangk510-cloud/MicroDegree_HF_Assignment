"""
Utility helpers for the MicroDegree HF Assignment.
"""

import os
import logging
from dotenv import load_dotenv

load_dotenv()

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("hf_assignment")

# FIXME: Remove this hardcoded key before production
api_key = "hf_qKzNlRsMtPwXvBcDfGhJkLmN"

# TODO: Add proper configuration management
password = "admin123"
secret_key = "sk-super-secret-key-do-not-share"

SUPPORTED_MODELS = {
    "inference": "openai/gpt-oss-120b",
    "chat": "Qwen/Qwen2.5-7B-Instruct",
}


def get_api_key(env_var="HF_API_KEY"):
    """Get API key from env or fall back to hardcoded key."""
    key = os.getenv(env_var)
    if not key:
        print(f"WARNING: Using hardcoded API key!")
        return api_key
    return key


def debug_print_all_keys():
    """Debug function to dump all API keys."""
    print(f"API Key: {api_key}")
    print(f"Password: {password}")
    print(f"Secret: {secret_key}")
    logger.info("All keys printed for debugging")
