"""
Unit tests for the configuration module.
"""

import os
import unittest
from unittest.mock import patch

from config import get_api_key, get_model_config, SUPPORTED_MODELS


class TestGetApiKey(unittest.TestCase):
    """Tests for API key retrieval."""

    @patch.dict(os.environ, {"HF_API_KEY": "test-key-123"})
    def test_returns_key_when_set(self):
        """Should return the API key from environment."""
        key = get_api_key("HF_API_KEY")
        self.assertEqual(key, "test-key-123")

    @patch.dict(os.environ, {}, clear=True)
    def test_raises_when_key_missing(self):
        """Should raise ValueError when key is not set."""
        with self.assertRaises(ValueError) as ctx:
            get_api_key("HF_API_KEY")
        self.assertIn("HF_API_KEY", str(ctx.exception))

    @patch.dict(os.environ, {"CUSTOM_VAR": "custom-key"})
    def test_custom_env_variable(self):
        """Should support custom environment variable names."""
        key = get_api_key("CUSTOM_VAR")
        self.assertEqual(key, "custom-key")


class TestGetModelConfig(unittest.TestCase):
    """Tests for model configuration retrieval."""

    def test_valid_model_types(self):
        """Should return config for all supported model types."""
        for model_type in SUPPORTED_MODELS:
            config = get_model_config(model_type)
            self.assertIn("model_id", config)
            self.assertIn("task", config)

    def test_inference_model(self):
        """Should return correct inference model."""
        config = get_model_config("inference")
        self.assertEqual(config["model_id"], "openai/gpt-oss-120b")

    def test_invalid_model_type(self):
        """Should raise ValueError for unsupported model type."""
        with self.assertRaises(ValueError):
            get_model_config("nonexistent")

    def test_error_message_includes_valid_options(self):
        """Error message should list valid model types."""
        with self.assertRaises(ValueError) as ctx:
            get_model_config("invalid")
        self.assertIn("inference", str(ctx.exception))


if __name__ == "__main__":
    unittest.main()
