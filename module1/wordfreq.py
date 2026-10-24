import argparse
import re
from collections import Counter
from pathlib import Path


def count_words(text: str, top: int = 5) -> list[tuple[str, int]]:
    words = re.findall(r"[a-z']+", text.lower())
    return Counter(words).most_common(top)


def main() -> None:
    parser = argparse.ArgumentParser(description="Top words in a file.")
    parser.add_argument("file", type=Path)
    parser.add_argument("--top", type=int, default=5)
    args = parser.parse_args()

    try:
        text = args.file.read_text(encoding="utf-8")
    except FileNotFoundError:
        print(f"File not found: {args.file}")
        return

    for word, count in count_words(text, args.top):
        print(f"{word:<15}{count}")


if __name__ == "__main__":
    main()