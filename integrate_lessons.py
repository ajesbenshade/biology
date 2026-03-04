#!/usr/bin/env python3
"""Sanitize lesson markdown files.

- Remove VSCode cell wrapper tags
- Remove surrounding markdown fences
- Add default Jekyll front matter when missing
"""

import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent
LESSONS = ROOT / "lessons"


def ensure_front_matter(text: str, title: str) -> str:
    front_matter = f"---\nlayout: default\ntitle: {title}\n---\n\n"
    if text.lstrip().startswith("---"):
        return text
    return front_matter + text.lstrip()


def clean_file(path: pathlib.Path) -> None:
    text = path.read_text(encoding="utf-8")
    original = text

    text = re.sub(r"^\s*<VSCode\.Cell[^>]*>\s*\n?", "", text)
    text = re.sub(r"\n?\s*</VSCode\.Cell>\s*$", "\n", text)
    text = re.sub(r"^\s*```(?:markdown)?\s*\n", "", text)
    text = re.sub(r"\n\s*```\s*$", "", text)

    title_match = re.search(r"^#\s*(.+)$", text, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else path.stem
    short_title = title.split("—")[0].strip() if "—" in title else title
    text = ensure_front_matter(text, short_title)

    if text != original:
        path.write_text(text, encoding="utf-8")
        print(f"Updated {path.relative_to(ROOT)}")


def main() -> None:
    if not LESSONS.exists():
        print("No lessons directory found.")
        return
    for markdown_file in LESSONS.rglob("*.md"):
        clean_file(markdown_file)


if __name__ == "__main__":
    main()
