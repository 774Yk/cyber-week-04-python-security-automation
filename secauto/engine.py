"""Safe, offline security automation for owned sample data.

Author: Y_774 | Telegram: @Y_774 | Instagram: @Y.77.4 | GitHub: 774Yk
Contact: yassenalhajere@gmail.com
"""
from __future__ import annotations
from dataclasses import asdict, dataclass
from pathlib import Path
import hashlib
import json
import re

SECRET_PATTERNS = [
    re.compile(r"AKIA[0-9A-Z]{16}"),
    re.compile(r"(?i)(password|api[_-]?key|secret)\s*[:=]\s*['\"]?[^\s'\"]+"),
]

@dataclass(frozen=True)
class Finding:
    rule_id: str
    severity: str
    path: str
    message: str


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as handle:
        for chunk in iter(lambda: handle.read(8192), b""):
            digest.update(chunk)
    return digest.hexdigest()


def scan_file(path: Path) -> list[Finding]:
    findings: list[Finding] = []
    text = path.read_text(errors="replace")
    for pattern in SECRET_PATTERNS:
        if pattern.search(text):
            findings.append(Finding("SEC-001", "high", str(path), "possible secret pattern detected"))
            break
    if path.suffix == ".json":
        try:
            payload = json.loads(text)
            if isinstance(payload, dict) and payload.get("debug") is True:
                findings.append(Finding("CFG-001", "medium", str(path), "debug mode enabled in configuration"))
        except json.JSONDecodeError:
            findings.append(Finding("DATA-001", "medium", str(path), "invalid JSON sample"))
    return findings


def scan_tree(root: Path) -> list[Finding]:
    findings: list[Finding] = []
    for path in sorted(root.rglob("*")):
        if path.is_file() and ".git" not in path.parts and path.name not in {"engine.py", "cli.py"}:
            findings.extend(scan_file(path))
    return findings


def inventory(root: Path) -> list[dict[str, str]]:
    return [{"path": str(path.relative_to(root)), "sha256": sha256_file(path)}
            for path in sorted(root.rglob("*")) if path.is_file() and ".git" not in path.parts]


def report(root: Path) -> dict:
    findings = scan_tree(root)
    return {"scope": str(root), "files": inventory(root), "findings": [asdict(item) for item in findings]}
