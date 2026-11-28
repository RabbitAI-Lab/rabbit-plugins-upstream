#!/usr/bin/env python3
"""Bounded SHA-256 verification of a local Agent World .pyz, no execution/network."""
from __future__ import annotations

import argparse
import errno
import hashlib
import hmac
import json
import os
from pathlib import Path
import re
import stat

MAX_BYTES = 128 * 1024 * 1024


def sha256_regular_file(path: Path) -> str:
    if not isinstance(path, Path) or not path.is_absolute():
        raise ValueError("An absolute local path is required")
    if path.suffix.lower() != ".pyz":
        raise ValueError("Only the .pyz format of the published Agent World clients is supported")
    flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0)
    try:
        fd = os.open(path, flags)
    except OSError as exc:
        if exc.errno == errno.ELOOP:
            raise ValueError("Symlink verification refused") from exc
        raise
    try:
        first = os.fstat(fd)
        if not stat.S_ISREG(first.st_mode) or first.st_nlink != 1:
            raise ValueError("Only unlinked regular files are supported")
        if first.st_size > MAX_BYTES:
            raise ValueError("Client file exceeds safety size limit")
        hasher = hashlib.sha256()
        total = 0
        with os.fdopen(fd, "rb", closefd=False) as stream:
            while True:
                chunk = stream.read(min(1024 * 1024, MAX_BYTES + 1 - total))
                if not chunk:
                    break
                total += len(chunk)
                if total > MAX_BYTES:
                    raise ValueError("Client file expanded past safety size limit")
                hasher.update(chunk)
        after = os.fstat(fd)
        attributes = lambda st: (st.st_dev, st.st_ino, st.st_size, st.st_mtime_ns,
                                  st.st_ctime_ns, st.st_nlink, st.st_mode)
        if total != first.st_size or attributes(first) != attributes(after):
            raise ValueError("Client file changed during verification")
        return hasher.hexdigest()
    finally:
        os.close(fd)


def verify(path: Path, expected: str) -> dict:
    if not isinstance(expected, str) or re.fullmatch(r"[a-fA-F0-9]{64}", expected) is None:
        raise ValueError("Expected SHA-256 must be exactly 64 hex digits")
    observed = sha256_regular_file(path)
    # The caller provides the expected digest. This tool cannot itself establish
    # that the caller copied it from the official website. Never label that proven.
    return {
        "file": path.name,
        "sha256": observed,
        "matches_supplied_sha256": hmac.compare_digest(observed, expected.lower()),
        "official_expected_digest_provenance_verified": False,
        "executed": False,
        "network_requests": 0,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description="Hash a previously downloaded local .pyz without running it")
    parser.add_argument("file", type=Path)
    parser.add_argument("--expected-sha256", required=True, help="64 hex digits independently read from official page")
    args = parser.parse_args()
    try:
        result = verify(args.file, args.expected_sha256)
    except (OSError, ValueError) as exc:
        print(json.dumps({"status": "error", "reason": str(exc)}))
        return 2
    print(json.dumps(result, sort_keys=True))
    return 0 if result["matches_supplied_sha256"] else 1


if __name__ == "__main__":
    raise SystemExit(main())
