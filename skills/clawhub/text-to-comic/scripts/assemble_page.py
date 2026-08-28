#!/usr/bin/env python3
"""Assemble rendered panel images into a final page/canvas.

Reads a panel plan's `assembly` config and a list of panel image files,
crops to a common cell ratio, and lays them out (grid or vertical stack).
Optionally overlays Chinese captions below each panel.

Usage:
  python3 scripts/assemble_page.py <panel_plan.json> <image1> [image2 ...]
    --cell-w 600       target cell width in px (default 600)
    --caption-h 180    caption band height in px (default 180)
    --out out.png      output path (default assembled.png)
    --font <path>      path to a CJK-capable TTF/TTC font
    --title <text>     optional top title text
"""

from __future__ import annotations

import argparse
import json
import os
import sys
from pathlib import Path
from typing import Any, Dict, List

from PIL import Image, ImageDraw, ImageFont


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def layout_from_plan(assembly: Dict[str, Any], n: int) -> tuple[int, int]:
    """Return (cols, rows) for a layout string and panel count."""
    layout = (assembly or {}).get("layout", "2x2")
    mapping = {
        "single": (1, max(n, 1)),
        "2x2": (2, 2),
        "2x3": (2, 3),
        "2x4": (2, 4),
        "vertical-stack": (1, n),
    }
    if layout in mapping:
        cols, rows = mapping[layout]
    elif "x" in layout:
        parts = layout.split("x")
        cols = int(parts[0])
        rows = int(parts[1])
    else:
        cols, rows = 2, max(1, (n + 1) // 2)

    # For grid layouts, ensure rows fit the panel count (last row may be partial)
    if layout not in ("single", "vertical-stack"):
        rows = (n + cols - 1) // cols
    return cols, rows


def load_cjk_font(size: int, user_font: str | None) -> ImageFont.FreeTypeFont | None:
    candidates = []
    if user_font:
        candidates.append(user_font)
    candidates += [
        "/usr/share/fonts/truetype/wqy/wqy-zenhei.ttc",
        "/usr/share/fonts/truetype/wqy/wqy-microhei.ttc",
        "/usr/share/fonts/opentype/noto/NotoSansCJK-Regular.ttc",
        "/System/Library/Fonts/PingFang.ttc",
        "C:/Windows/Fonts/msyh.ttc",
    ]
    for c in candidates:
        if c and os.path.exists(c):
            try:
                return ImageFont.truetype(c, size)
            except Exception:
                continue
    return None


def center_text(draw: ImageDraw.ImageDraw, xy: tuple[int, int], text: str, font: ImageFont.FreeTypeFont, fill: Any, box_w: int):
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    x = xy[0] + (box_w - tw) // 2
    draw.text((x, xy[1]), text, font=font, fill=fill)


def main() -> int:
    parser = argparse.ArgumentParser(description="Assemble panels into a comic page.")
    parser.add_argument("panel_plan", help="Path to panel plan JSON")
    parser.add_argument("images", nargs="+", help="Path(s) to panel images, in order")
    parser.add_argument("--cell-w", type=int, default=600, help="Target cell width in px")
    parser.add_argument("--caption-h", type=int, default=180, help="Caption band height in px")
    parser.add_argument("--gutter", type=int, default=24, help="Gutter width in px")
    parser.add_argument("--out", default="assembled.png", help="Output path")
    parser.add_argument("--font", default=None, help="Path to a CJK font file")
    parser.add_argument("--title", default=None, help="Optional top title text")
    args = parser.parse_args()

    plan = load_json(Path(args.panel_plan))
    panels = plan.get("panels", [])
    assembly = plan.get("assembly", {})
    n = len(args.images)

    if n == 0 or len(panels) == 0:
        print("No panels or images provided.", file=sys.stderr)
        return 2
    if n != len(panels):
        print(f"Warning: {n} images but {len(panels)} panels in plan", file=sys.stderr)

    cols, rows = layout_from_plan(assembly, n)
    gutter = args.gutter
    cap_h = args.caption_h if assembly.get("caption_mode") != "none" else 0

    cell_h = args.cell_w  # assume square cells after crop
    top_title_h = 200 if args.title else 0

    total_w = cols * args.cell_w + (cols + 1) * gutter
    total_h = top_title_h + rows * (cell_h + cap_h) + (rows + 1) * gutter

    print(f"Layout {cols}x{rows}, canvas {total_w}x{total_h}")

    canvas = Image.new("RGB", (total_w, total_h), (250, 248, 245))
    draw = ImageDraw.Draw(canvas)

    font_title = load_cjk_font(56, args.font)
    font_caption = load_cjk_font(28, args.font)

    if args.title and font_title:
        center_text(draw, (0, 40), args.title, font_title, (60, 80, 110), total_w)

    for idx, img_path in enumerate(args.images):
        if idx >= cols * rows:
            break
        row = idx // cols
        col = idx % cols
        x = gutter + col * (args.cell_w + gutter)
        y = top_title_h + gutter + row * (cell_h + cap_h + gutter)

        img = Image.open(img_path)
        w, h = img.size
        # center-crop to square (target ratio 1:1)
        min_dim = min(w, h)
        left = (w - min_dim) // 2
        top = (h - min_dim) // 2
        img = img.crop((left, top, left + min_dim, top + min_dim))
        img = img.resize((args.cell_w, cell_h), Image.LANCZOS)
        canvas.paste(img, (x, y))

        # caption band
        if cap_h > 0 and idx < len(panels):
            caption = (panels[idx].get("caption") or "").strip()
            cy = y + cell_h
            draw.rectangle([(x, cy), (x + args.cell_w, cy + cap_h)], fill=(255, 252, 248), outline=(220, 215, 210), width=2)
            if caption and font_caption:
                lines = [caption[i:i+20] for i in range(0, len(caption), 20)]
                line_h = int(cap_h / len(lines)) if lines else cap_h
                ty = cy + (cap_h - line_h * len(lines)) // 2
                for line in lines:
                    center_text(draw, (x, ty), line, font_caption, (50, 50, 60), args.cell_w)
                    ty += line_h

    canvas.save(args.out, "PNG")
    print(f"Saved: {args.out} ({round(os.path.getsize(args.out)/1e6,2)} MB)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
