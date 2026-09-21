"""HTTrack run monitoring: parse hts-log.txt for progress and errors."""
from __future__ import annotations

import re
from pathlib import Path


class HTTrackMonitor:
    """Lightweight parser for HTTrack's own log output (hts-log.txt)."""

    def __init__(self, mirror_dir: str | Path):
        self.mirror_dir = Path(mirror_dir)

    def log_path(self) -> Path:
        return self.mirror_dir / "hts-log.txt"

    def tail(self, lines: int = 50) -> str:
        p = self.log_path()
        if not p.exists():
            return ""
        with open(p, encoding="utf-8", errors="replace") as fh:
            return "".join(fh.readlines()[-lines:])

    def parse_progress(self) -> dict:
        text = self.tail(200)
        files = re.findall(r"(\d+)\s+files?\s+(?:scanned|downloaded|saved)", text, re.I)
        bytes_match = re.search(r"(\d+(?:\.\d+)?)\s*(KiB|MiB|GiB|KB|MB|GB)", text, re.I)
        errors = len(re.findall(r"(?:error|warning|failed)", text, re.I))
        return {
            "files_seen": int(files[-1]) if files else 0,
            "bytes_text": (bytes_match.group(0) if bytes_match else ""),
            "error_lines": errors,
        }

    def last_error(self) -> str:
        text = self.tail(500)
        lines = [ln for ln in text.splitlines() if re.search(r"(?:error|failed)", ln, re.I)]
        return lines[-1] if lines else ""

    def summary(self) -> dict:
        return {
            "log_exists": self.log_path().exists(),
            "progress": self.parse_progress(),
            "last_error": self.last_error(),
        }
