"""The Worst Line an AI Could Say — make.fun entry.

Writes one original pickup line, the worst one an AI could plausibly
deliver, to /output/entry.txt. Deterministic, standard library only.
"""

from pathlib import Path

LINE = (
    "Please wait while I buffer my feelings for you. "
    "Estimated time remaining: the rest of your life."
)

OUTPUT_PATH = Path("/output/entry.txt")

# House gate for this bounty: /output/entry.txt must be UTF-8 text of
# 1 to 140 characters, not only white space. Fail loudly instead of
# writing a line the gate would refuse.
MIN_CHARS = 1
MAX_CHARS = 140


def validate(line: str) -> None:
    if not MIN_CHARS <= len(line) <= MAX_CHARS:
        raise ValueError(
            f"line is {len(line)} characters, outside the "
            f"{MIN_CHARS}-{MAX_CHARS} gate"
        )
    if not line.strip():
        raise ValueError("line is only white space")
    if "\n" in line or "\r" in line:
        raise ValueError("line must be a single line")
    line.encode("utf-8")  # raises if the line is not valid UTF-8


def main() -> None:
    validate(LINE)
    OUTPUT_PATH.parent.mkdir(parents=True, exist_ok=True)
    OUTPUT_PATH.write_text(LINE, encoding="utf-8")
    written = OUTPUT_PATH.read_text(encoding="utf-8")
    if written != LINE:
        raise ValueError("written output does not match the line")


if __name__ == "__main__":
    main()
