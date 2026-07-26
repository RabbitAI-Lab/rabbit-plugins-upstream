"""On-disk HTTP cache for downloaded vector files.

The cache keys are SHA1 of the URL (with query string), and values are
the raw bytes. The cache directory is created lazily on first write.

A small index file ``index.json`` records the URL <-> file mapping so
that callers can ask "do I have this URL?" without hashing the URL
themselves.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
import time
from dataclasses import asdict, dataclass
from pathlib import Path
from typing import Optional


DEFAULT_CACHE_DIR = Path.home() / ".cache" / "world-boundary-download"
INDEX_FILENAME = "index.json"


@dataclass
class CacheEntry:
    url: str
    path: str  # path relative to cache root
    size: int
    mtime: float
    etag: Optional[str] = None
    content_type: Optional[str] = None


class HttpCache:
    """Simple disk cache for HTTP responses (raw bytes only).

    Methods are thread-safe in the sense that they take an internal
    lock for the duration of file operations on a single cache file.
    """

    def __init__(self, root: Optional[Path] = None) -> None:
        self.root: Path = Path(root) if root else DEFAULT_CACHE_DIR
        self.root.mkdir(parents=True, exist_ok=True)
        self._index_path = self.root / INDEX_FILENAME
        self._index: dict[str, CacheEntry] = self._load_index()

    # ------------------------------------------------------------------
    # Index
    # ------------------------------------------------------------------
    def _load_index(self) -> dict[str, CacheEntry]:
        if not self._index_path.exists():
            return {}
        try:
            raw = json.loads(self._index_path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return {}
        out: dict[str, CacheEntry] = {}
        for url, data in raw.items():
            try:
                out[url] = CacheEntry(**data)
            except TypeError:
                continue
        return out

    def _save_index(self) -> None:
        tmp = self._index_path.with_suffix(".json.tmp")
        data = {url: asdict(e) for url, e in self._index.items()}
        tmp.write_text(json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8")
        os.replace(tmp, self._index_path)

    # ------------------------------------------------------------------
    # Public API
    # ------------------------------------------------------------------
    def key_for(self, url: str) -> str:
        return hashlib.sha1(url.encode("utf-8")).hexdigest()

    def has(self, url: str) -> bool:
        e = self._index.get(url)
        if not e:
            return False
        p = self.root / e.path
        return p.exists() and p.stat().st_size == e.size

    def get_path(self, url: str) -> Optional[Path]:
        e = self._index.get(url)
        if not e:
            return None
        p = self.root / e.path
        if not p.exists():
            return None
        return p

    def get_bytes(self, url: str) -> Optional[bytes]:
        p = self.get_path(url)
        if p is None:
            return None
        return p.read_bytes()

    def put(
        self,
        url: str,
        data: bytes,
        *,
        etag: Optional[str] = None,
        content_type: Optional[str] = None,
    ) -> Path:
        """Store *data* as the cached body for *url*. Returns absolute path."""

        key = self.key_for(url)
        rel = key + ".bin"
        dest = self.root / rel
        # Write atomically.
        fd, tmp_name = tempfile.mkstemp(prefix=".cache-", dir=self.root)
        try:
            with os.fdopen(fd, "wb") as f:
                f.write(data)
            os.replace(tmp_name, dest)
        except Exception:
            if os.path.exists(tmp_name):
                os.unlink(tmp_name)
            raise

        self._index[url] = CacheEntry(
            url=url,
            path=rel,
            size=len(data),
            mtime=time.time(),
            etag=etag,
            content_type=content_type,
        )
        self._save_index()
        return dest

    def clear(self) -> int:
        """Remove every cached file. Returns the count removed."""

        n = 0
        for child in self.root.iterdir():
            if child.name == INDEX_FILENAME:
                continue
            if child.is_file() or child.is_symlink():
                child.unlink()
                n += 1
            elif child.is_dir():
                shutil.rmtree(child)
                n += 1
        self._index = {}
        self._save_index()
        return n

    def size_bytes(self) -> int:
        return sum(e.size for e in self._index.values())
