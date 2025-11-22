# DeepSeek V3 Tokenizer

This project provides tools to tokenize text using the DeepSeek V3 tokenizer.

## Installation

This project uses `uv` for package management.

```bash
# Install uv if you haven't already
curl -LsSf https://astral.sh/uv/install.sh | sh

# Install dependencies
uv sync
```

## Usage

### Check Tokens (CLI)

You can use the `check_tokens.py` script to check the tokens of a text.

**Command Line Argument:**

```bash
uv run check_tokens.py "Your text here"
```

**Interactive Mode:**

Run the script without arguments to enter interactive mode:

```bash
uv run check_tokens.py
```

### Python API

You can also use the tokenizer in your Python code:

```python
from deepseek_v3_tokenizer.deepseek_tokenizer import tokenize_text, load_text_files

# Tokenize text
text = "Hello, world!"
tokens = tokenize_text(text)
print(f"Tokens: {tokens}")

# Load text files
# Loads all .txt files from 'data' directory by default
texts = load_text_files("data")

# Load with specific extensions and recursive search
texts = load_text_files("data", extensions=[".txt", ".md"], recursive=True)
```

## Development

### Running Tests

This project uses `pytest` for testing.

```bash
uv run pytest
```
