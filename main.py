"""Write the one line that could have replaced an entire pointless meeting.

Deterministic: the program writes one fixed sentence to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt). It reads no
clock, no randomness, no network and no files, so every run produces
byte-identical output. The file holds the sentence plus one trailing
newline (73 bytes, 72 characters of sentence text).
"""

import os

ENTRY = "We just held an hour-long meeting to agree that we need another meeting."


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
