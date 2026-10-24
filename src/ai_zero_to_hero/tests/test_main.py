import pytest

from main import estimate_tokens, get_api_key


def test_empty_text_is_zero_tokens():
    assert estimate_tokens("") == 0


def test_short_text_is_at_least_one_token():
    assert estimate_tokens("hi") == 1


def test_estimate_is_chars_divided_by_four():
    assert estimate_tokens("a" * 40) == 10


def test_get_api_key_reads_env(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "test-key")
    assert get_api_key() == "test-key"


def test_get_api_key_missing_raises(monkeypatch):
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    monkeypatch.setattr("main.load_dotenv", lambda: None)
    with pytest.raises(RuntimeError):
        get_api_key()
