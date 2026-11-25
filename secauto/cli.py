"""CLI for the offline local security-automation toolkit.

Author: Y_774 | Telegram: @Y_774 | Instagram: @Y.77.4 | GitHub: 774Yk
Contact: yassenalhajere@gmail.com
"""
import argparse
import json
from pathlib import Path
from .engine import report

def main() -> None:
    parser = argparse.ArgumentParser(description="Scan only an explicitly supplied local directory")
    parser.add_argument("root", nargs="?", default="sample-data")
    parser.add_argument("--output", default="-")
    args = parser.parse_args()
    root = Path(args.root).resolve()
    if not root.exists() or not root.is_dir():
        raise SystemExit("root must be an existing local directory")
    result = report(root)
    rendered = json.dumps(result, indent=2)
    if args.output == "-":
        print(rendered)
    else:
        Path(args.output).write_text(rendered + "\n")
        print(f"wrote report to {args.output}")

if __name__ == "__main__":
    main()
