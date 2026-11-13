"""ai-joke-03 entry: writes exactly one joke to the output directory.

Determinism contract: standard library only, no network, no clock, no randomness,
so every run writes byte-identical UTF-8 bytes (no trailing newline).
"""

import os

__all__ = ["JOKE", "write_entry", "main"]

JOKE = "The agent said it would handle it, and now the repository is very quiet."


def write_entry(output_dir: str) -> str:
    """Write JOKE to <output_dir>/entry.txt and return the path written."""
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as entry:
        entry.write(JOKE)
    return path


def main() -> str:
    """Resolve the output directory from the environment and write the entry."""
    return write_entry(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))


if __name__ == "__main__":
    main()
