"""Fortune Cookie Wisdom for Developers — make.fun entry.

Writes one original fortune-cookie line for a software developer to
/output/entry.txt. Standard library only, no arguments, no network,
deterministic: every run writes the same line.
"""

import os

LINE = "You will name a variable 'temp', and it will outlive every 'final' thing you ever built."

OUTPUT_PATH = "/output/entry.txt"


def main() -> int:
    directory = os.path.dirname(OUTPUT_PATH)
    os.makedirs(directory, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(LINE)
    print(LINE)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
