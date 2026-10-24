import os

from dotenv import load_dotenv


def estimate_tokens(text: str) -> int:
    """Rough LLM token estimate: about 4 characters per token."""
    if not text:
        return 0
    return max(1, len(text) // 4)


def get_api_key(name: str = "ANTHROPIC_API_KEY") -> str:
    """Read a secret from the environment (loaded from .env)."""
    load_dotenv()
    key = os.getenv(name)
    if not key:
        raise RuntimeError(f"{name} is not set. Add it to your .env file.")
    return key


if __name__ == "__main__":
    sample = "Hello from my AI zero-to-hero repo!"
    print(f"'{sample}' is about {estimate_tokens(sample)} tokens")
