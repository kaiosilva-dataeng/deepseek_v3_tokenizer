import os
from pathlib import Path
from typing import Optional

os.environ["TRANSFORMERS_VERBOSITY"] = "error"

import transformers

chat_tokenizer_dir = "./deepseek_v3_tokenizer"


def load_prompt_files(dir_path, files: Optional[list[str]] = None) -> dict[str, str]:
    dir_path = Path(dir_path)
    prompt_files = {}
    if files:
        for file_name in files:
            file_path = dir_path.joinpath(file_name)
            with file_path.open("r") as f:
                prompt_files[file_name] = f.read()
        return prompt_files

    for file_path in dir_path.glob("*.txt"):
        with file_path.open("r") as f:
            prompt_files[file_path.stem] = f.read()
    return prompt_files


tokenizer = transformers.AutoTokenizer.from_pretrained(
    chat_tokenizer_dir, model_type="deepseek", trust_remote_code=True
)

if __name__ == "__main__":
    result = tokenizer.encode("Hello, world!")
    print("Token quantity:", len(result))
    print("Tokens:", result)
