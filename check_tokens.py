import sys
import argparse
from deepseek_v3_tokenizer.deepseek_tokenizer import tokenize_text


def main():
    parser = argparse.ArgumentParser(
        description="Check tokens of a text using DeepSeek V3 tokenizer."
    )
    parser.add_argument(
        "text",
        nargs="?",
        help="The text to tokenize. If not provided, interactive mode is started.",
    )
    args = parser.parse_args()

    if args.text:
        text = args.text
        tokens = tokenize_text(text)
        print(f"Token quantity: {len(tokens)}")
        print(f"Tokens: {tokens}")
    else:
        print("Enter text to tokenize (Press Ctrl+C to exit):")
        try:
            while True:
                text = input("> ")
                if not text:
                    continue
                tokens = tokenize_text(text)
                print(f"Token quantity: {len(tokens)}")
                print(f"Tokens: {tokens}")
        except KeyboardInterrupt:
            print("\nExiting...")


if __name__ == "__main__":
    main()
