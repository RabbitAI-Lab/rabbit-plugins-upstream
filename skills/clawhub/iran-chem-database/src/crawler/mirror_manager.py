"""Mirror store management: disk usage, cleanup, compression (spec §3.3/§5.2)."""
from __future__ import annotations

import shutil
import tarfile
from datetime import datetime, timedelta
from pathlib import Path
from typing import List


class MirrorManager:
    def __init__(self, base_dir: str | Path):
        self.base_dir = Path(base_dir)
        self.base_dir.mkdir(parents=True, exist_ok=True)

    def list_mirrors(self) -> List[Path]:
        return sorted(p for p in self.base_dir.iterdir() if p.is_dir())

    def disk_usage_bytes(self) -> int:
        return sum(p.stat().st_size for p in self.base_dir.rglob("*") if p.is_file())

    def cleanup_old_mirrors(self, max_age_days: int = 90) -> List[str]:
        """Remove mirror directories not updated within max_age_days.

        Uses the newest file mtime inside each mirror as the "last updated" signal
        (hts-cache timestamps are authoritative when present).
        Returns a list of removed project names.
        """
        cutoff = datetime.now() - timedelta(days=max_age_days)
        removed: List[str] = []
        for mirror in self.list_mirrors():
            newest = self._newest_mtime(mirror)
            if newest and newest < cutoff:
                shutil.rmtree(mirror, ignore_errors=True)
                removed.append(mirror.name)
        return removed

    def compress_old_mirrors(self, older_than_days: int = 30) -> List[str]:
        """tar.gz old mirror directories to save disk (spec §5.2 item 4)."""
        cutoff = datetime.now() - timedelta(days=older_than_days)
        compressed: List[str] = []
        for mirror in self.list_mirrors():
            if mirror.name.endswith(".tar.gz"):
                continue
            newest = self._newest_mtime(mirror)
            if newest and newest < cutoff:
                out = mirror.with_name(mirror.name + ".tar.gz")
                with tarfile.open(out, "w:gz") as tar:
                    tar.add(mirror, arcname=mirror.name)
                shutil.rmtree(mirror, ignore_errors=True)
                compressed.append(mirror.name)
        return compressed

    @staticmethod
    def _newest_mtime(path: Path) -> datetime | None:
        mtimes = [p.stat().st_mtime for p in path.rglob("*") if p.is_file()]
        if not mtimes:
            return None
        return datetime.fromtimestamp(max(mtimes))
