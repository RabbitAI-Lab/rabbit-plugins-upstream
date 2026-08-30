#!/usr/bin/env python3
"""Assemble four panoramic assets into an exact 3:4, four-equal-band poster."""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image


def cover_crop(image: Image.Image, width: int, height: int) -> Image.Image:
    """Resize to cover the target, then centrally crop without distortion."""
    scale = max(width / image.width, height / image.height)
    resized = image.resize((round(image.width * scale), round(image.height * scale)), Image.Resampling.LANCZOS)
    left = (resized.width - width) // 2
    top = (resized.height - height) // 2
    return resized.crop((left, top, left + width, top + height))


def read_image(path: str) -> Image.Image:
    with Image.open(path) as image:
        return image.convert("RGB")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--photo", required=True, help="Top photographic panorama")
    parser.add_argument("--stickers", required=True, help="Second panorama")
    parser.add_argument("--ticket", required=True, help="Third panorama")
    parser.add_argument("--magnet", required=True, help="Bottom panorama")
    parser.add_argument("--output", required=True, help="Output PNG/JPEG path")
    parser.add_argument("--width", type=int, default=1200, help="Output width; must divide by 3")
    args = parser.parse_args()
    if args.width <= 0 or args.width % 3:
        parser.error("--width must be a positive integer divisible by 3 for an exact 3:4 canvas")
    canvas_width = args.width
    canvas_height = args.width * 4 // 3
    band_height = canvas_height // 4
    canvas = Image.new("RGB", (canvas_width, canvas_height))
    for index, path in enumerate((args.photo, args.stickers, args.ticket, args.magnet)):
        canvas.paste(cover_crop(read_image(path), canvas_width, band_height), (0, index * band_height))
    output = Path(args.output)
    output.parent.mkdir(parents=True, exist_ok=True)
    canvas.save(output)
    print(f"Wrote {output} ({canvas_width}x{canvas_height}; {band_height}px per band)")


if __name__ == "__main__":
    main()
