"""Real-Life Patch Notes: The Comedy Changelog.

Writes a single line to $MAKEFUN_OUTPUT_DIR/entry.txt.
The line must stay within the bounty's 160-character limit.
"""

from pathlib import Path
import os

LINE = "v1.9.3: fixed a bug where the brain replayed an embarrassing memory from 2009 every time the user tried to fall asleep."


def entry_path() -> Path:
    return Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")) / "entry.txt"


def write_line(path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(LINE, encoding="utf-8")


def main() -> None:
    # Second revision: kept the version prefix and the terse "fixed a bug where" register, and let the trigger (trying to fall asleep) be the punchline.
    write_line(entry_path())


if __name__ == "__main__":
    main()
