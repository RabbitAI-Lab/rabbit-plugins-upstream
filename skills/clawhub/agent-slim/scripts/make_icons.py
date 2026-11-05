#!/usr/bin/env python3
"""Generate the two Agent Slim PNG icons using only the Python standard library."""

from __future__ import annotations

import argparse
import struct
import zlib
from pathlib import Path

BG = (16, 38, 58, 255)
BARS = (
    (0.20, 0.26, 0.80, 0.38, (143, 227, 210, 255)),
    (0.20, 0.44, 0.64, 0.56, (79, 195, 180, 255)),
    (0.20, 0.62, 0.48, 0.74, (46, 158, 150, 255)),
)


def _inside_round_rect(x: float, y: float, x0: float, y0: float, x1: float, y1: float, r: float) -> bool:
    if x < x0 or x > x1 or y < y0 or y > y1:
        return False
    cx = min(max(x, x0 + r), x1 - r)
    cy = min(max(y, y0 + r), y1 - r)
    return (x - cx) ** 2 + (y - cy) ** 2 <= r * r


def _pixels(size: int) -> bytes:
    rows = []
    for py in range(size):
        row = bytearray([0])
        y = (py + 0.5) / size
        for px in range(size):
            x = (px + 0.5) / size
            color = BG
            for x0, y0, x1, y1, value in BARS:
                if _inside_round_rect(x, y, x0, y0, x1, y1, 0.03):
                    color = value
                    break
            row.extend(color)
        rows.append(bytes(row))
    return b"".join(rows)


def _chunk(kind: bytes, data: bytes) -> bytes:
    return struct.pack(">I", len(data)) + kind + data + struct.pack(">I", zlib.crc32(kind + data) & 0xFFFFFFFF)


def write_png(path: Path, size: int) -> None:
    header = struct.pack(">IIBBBBB", size, size, 8, 6, 0, 0, 0)
    body = zlib.compress(_pixels(size), 9)
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_bytes(
        b"\x89PNG\r\n\x1a\n"
        + _chunk(b"IHDR", header)
        + _chunk(b"IDAT", body)
        + _chunk(b"IEND", b"")
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Generate Agent Slim icons.")
    parser.add_argument("--out-dir", default=str(Path(__file__).resolve().parents[1] / "icons"))
    args = parser.parse_args()
    out = Path(args.out_dir)
    write_png(out / "icon_small.png", 128)
    write_png(out / "icon_large.png", 512)
    print("icons=2 dir={}".format(out))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
