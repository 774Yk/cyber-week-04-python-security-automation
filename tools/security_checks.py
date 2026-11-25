"""Repository safety checks; no network activity is performed.

Author: Y_774 | Telegram: @Y_774 | Instagram: @Y.77.4 | GitHub: 774Yk
Contact: yassenalhajere@gmail.com
"""
from pathlib import Path
import re
import sys
ROOT = Path(__file__).resolve().parents[1]

def main():
    failures = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts or "__pycache__" in path.parts or path == Path(__file__):
            continue
        text = path.read_text(errors="ignore")
        if re.search(r"(?i)https?://(?!127\.0\.0\.1|localhost|github\.com)", text):
            failures.append(f"external URL in controlled file: {path}")
        if "BEGIN RSA PRIVATE KEY" in text or "ghp_" in text:
            failures.append(f"credential marker in file: {path}")
    if failures:
        raise SystemExit("\n".join(failures))
    print("repository safety checks passed: offline scope and credential scan")

if __name__ == "__main__":
    main()
