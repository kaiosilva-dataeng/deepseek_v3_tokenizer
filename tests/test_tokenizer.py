import pytest
from deepseek_v3_tokenizer.deepseek_tokenizer import tokenize_text, get_tokenizer


def test_get_tokenizer():
    tokenizer = get_tokenizer()
    assert tokenizer is not None
    # Check if it has encode method
    assert hasattr(tokenizer, "encode")


def test_tokenize_text():
    text = "Hello, world!"
    tokens = tokenize_text(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0
    # Basic check: "Hello, world!" should produce some tokens


def test_tokenize_empty_text():
    text = ""
    tokens = tokenize_text(text)
    assert isinstance(tokens, list)
    assert len(tokens) == 0


def test_tokenize_special_chars():
    text = "你好"
    tokens = tokenize_text(text)
    assert isinstance(tokens, list)
    assert len(tokens) > 0
