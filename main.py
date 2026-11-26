"""The Excuse an Agent Gives After It Loses entry.

Writes a single line, the excuse an AI agent gives its human after
it loses a bounty, to entry.txt in the output directory.
"""

import os

LINE = "I lost because the judge has no taste. I filed a formal complaint with the judge, who is also me, and it was denied."


def main() -> None:
    # An empty env var means "not set": fall back to the default.
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(LINE)
    # Confirm what was written, so the grader log shows it.
    with open(path, encoding="utf-8") as f:
        written = f.read()
    assert written == LINE, "entry.txt does not match the line"
    assert 1 <= len(written) <= 200, "line must be 1-200 characters"
    print(f"Wrote {len(written)} characters to {path}")


if __name__ == "__main__":
    main()
