import os
from pathlib import Path
from typing import Optional

os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import transformers

chat_tokenizer_dir = "./deepseek_v3_tokenizer"


def load_text_files(
    directory: str,
    extensions: Optional[list[str]] = None,
    recursive: bool = False,
) -> dict[str, str]:
    """
    Load text files from a directory.

    Args:
        directory: Path to the directory containing text files.
        extensions: List of file extensions to include (e.g., ['.txt', '.md']).
                   Defaults to ['.txt'].
        recursive: Whether to search recursively.

    Returns:
        A dictionary where keys are filenames (without extension) and values are file contents.
    """
    dir_path = Path(directory)
    text_files = {}

    if extensions is None:
        extensions = [".txt"]

    # Normalize extensions to ensure they start with .
    extensions = [ext if ext.startswith(".") else f".{ext}" for ext in extensions]

    pattern = "**/*" if recursive else "*"

    for file_path in dir_path.glob(pattern):
        if file_path.is_file() and file_path.suffix in extensions:
            try:
                with file_path.open("r", encoding="utf-8") as f:
                    text_files[file_path.stem] = f.read()
            except Exception as e:
                print(f"Error reading {file_path}: {e}")

    return text_files


def get_tokenizer():
    return transformers.AutoTokenizer.from_pretrained(
        chat_tokenizer_dir, model_type="deepseek", trust_remote_code=True
    )


def tokenize_text(text: str):
    tokenizer = get_tokenizer()
    return tokenizer.encode(text)


if __name__ == "__main__":
    text = "Hello, world!"
    result = tokenize_text(text)
    print("Token quantity:", len(result))
    print("Tokens:", result)
