#!/usr/bin/env python3
"""
Cover image generation script
Generates a dedicated cover image (1920x1080) for the 3-Minute Book Digest
video, with book title, author, and brand text. (English version)

Design:
- Background: optional blurred storyboard image (darkened), or deep-blue gradient
- Top: "3-MINUTE BOOK DIGEST" brand text + orange divider line
- Middle: book title (large, auto-wrapped, centered)
- Lower-middle: author name
- Bottom: account-name watermark (optional, hidden if not provided)

Dependencies: Pillow (PIL)

Usage:
  # Use first storyboard image as background
  python generate_cover.py --book-name "Atomic Habits" --author "James Clear" --output cover.png --bg scene_000.png

  # No background image, use gradient
  python generate_cover.py --book-name "Atomic Habits" --author "James Clear" --output cover.png

  # Portrait size
  python generate_cover.py --book-name "Atomic Habits" --author "James Clear" --output cover.png --width 1080 --height 1920
"""

import argparse
import os
import platform
import sys

from PIL import Image, ImageDraw, ImageFilter, ImageFont


# ── Font detection ──────────────────────────────────────────────

def detect_font_path():
    """Auto-detect a system English font file path, returns (path, is_bold)."""
    system = platform.system().lower()
    candidates = []

    if system == "windows":
        candidates = [
            ("C:/Windows/Fonts/arialbd.ttf", True),     # Arial Bold
            ("C:/Windows/Fonts/arial.ttf", False),      # Arial
            ("C:/Windows/Fonts/calibrib.ttf", True),    # Calibri Bold
            ("C:/Windows/Fonts/segoeuib.ttf", True),    # Segoe UI Bold
        ]
    elif system == "darwin":
        candidates = [
            ("/System/Library/Fonts/Supplemental/Arial.ttf", True),
            ("/Library/Fonts/Arial.ttf", True),
            ("/System/Library/Fonts/Helvetica.ttc", False),
            ("/System/Library/Fonts/Supplemental/Calibri.ttf", False),
        ]
    else:
        candidates = [
            ("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", True),
            ("/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf", False),
            ("/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf", True),
            ("/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf", False),
        ]

    for path, is_bold in candidates:
        if os.path.exists(path):
            return path, is_bold

    return None, False


def load_font(size):
    """Load an English font of the given size."""
    font_path, _ = detect_font_path()
    if font_path:
        return ImageFont.truetype(font_path, size)
    print("Warning: no English font found, using default (may not render well)",
          file=sys.stderr)
    return ImageFont.load_default()


# ── Drawing helpers ──────────────────────────────────────────────

def draw_text_centered(draw, text, y, font, img_width, fill=(255, 255, 255, 255), shadow=True):
    """Draw centered text with optional shadow."""
    bbox = draw.textbbox((0, 0), text, font=font)
    text_width = bbox[2] - bbox[0]
    x = (img_width - text_width) // 2

    if shadow:
        draw.text((x + 3, y + 3), text, font=font, fill=(0, 0, 0, 160))

    draw.text((x, y), text, font=font, fill=fill)


def wrap_text(draw, text, font, max_width):
    """Word-based text wrapping. Returns a list of lines."""
    words = text.split()
    lines = []
    current = ""
    for word in words:
        test = (current + " " + word).strip()
        bbox = draw.textbbox((0, 0), test, font=font)
        if bbox[2] - bbox[0] > max_width and current:
            lines.append(current)
            current = word
        else:
            current = test
    if current:
        lines.append(current)
    return lines


# ── Background generation ───────────────────────────────────────

def make_gradient_bg(width, height):
    """Generate a deep-blue gradient background."""
    img = Image.new("RGBA", (width, height))
    draw = ImageDraw.Draw(img)
    for y in range(height):
        ratio = y / height
        r = int(15 + (35 - 15) * ratio)
        g = int(25 + (45 - 25) * ratio)
        b = int(55 + (75 - 55) * ratio)
        draw.line([(0, y), (width, y)], fill=(r, g, b, 255))
    return img


def make_blur_bg(bg_path, width, height):
    """Use a storyboard image as a blurred + darkened background."""
    bg = Image.open(bg_path).convert("RGB")
    bg = bg.resize((width, height), Image.LANCZOS)
    bg = bg.filter(ImageFilter.GaussianBlur(radius=20))
    bg = bg.convert("RGBA")
    overlay = Image.new("RGBA", (width, height), (0, 0, 0, 130))
    return Image.alpha_composite(bg, overlay)


# ── Main function ────────────────────────────────────────────────

ACCENT_COLOR = (255, 127, 114, 230)  # #FF7F72, matches the protagonist's top

def generate_cover(
    book_name,
    author_name,
    output_path,
    bg_image=None,
    width=1920,
    height=1080,
    ip_name=None,
):
    """
    Generate the cover image.

    Args:
    - book_name: book title
    - author_name: author name
    - output_path: output PNG path
    - bg_image: background image path (optional, uses first storyboard image)
    - width / height: cover dimensions
    - ip_name: bottom account name (optional, hidden if not provided)
    """

    # 1. Prepare background
    if bg_image and os.path.exists(bg_image):
        canvas = make_blur_bg(bg_image, width, height)
        print(f"Background: {bg_image} (blurred + darkened)")
    else:
        canvas = make_gradient_bg(width, height)
        print("Background: deep-blue gradient")

    draw = ImageDraw.Draw(canvas)

    # 2. Top brand text
    brand_font = load_font(38)
    draw_text_centered(draw, "3-MINUTE BOOK DIGEST", 70, brand_font, width,
                       fill=(255, 255, 255, 210))

    # Orange divider line
    line_y = 135
    line_w = min(420, width // 3)
    line_x = (width - line_w) // 2
    draw.line([(line_x, line_y), (line_x + line_w, line_y)],
              fill=ACCENT_COLOR, width=3)

    # 3. Book title (large, auto-wrapped)
    title_font_size = 80 if width >= 1920 else 56
    title_font = load_font(title_font_size)
    max_title_width = width - 200
    title_lines = wrap_text(draw, book_name, title_font, max_title_width)

    line_height = int(title_font_size * 1.25)
    # Vertically center the title in the 30%~65% area
    title_area_top = int(height * 0.30)
    title_area_bot = int(height * 0.65)
    total_h = len(title_lines) * line_height
    start_y = title_area_top + (title_area_bot - title_area_top - total_h) // 2

    for i, line in enumerate(title_lines):
        draw_text_centered(draw, line, start_y + i * line_height, title_font, width,
                           fill=(255, 255, 255, 255))

    # 4. Author name
    author_font = load_font(42 if width >= 1920 else 30)
    author_y = int(height * 0.68)
    draw_text_centered(draw, f"By {author_name}", author_y, author_font, width,
                       fill=(255, 255, 255, 230))

    # 5. Bottom divider + account name (only if ip_name is non-empty)
    if ip_name:
        bottom_y = height - 100
        bx = width // 2
        draw.line([(bx - 50, bottom_y), (bx + 50, bottom_y)],
                  fill=ACCENT_COLOR, width=2)

        ip_font = load_font(28 if width >= 1920 else 20)
        draw_text_centered(draw, ip_name, bottom_y + 15, ip_font, width,
                           fill=(255, 255, 255, 160))

    # 6. Save
    canvas.convert("RGB").save(output_path, "PNG", quality=95)
    print(f"Cover image generated: {output_path}  ({width}x{height})")
    return output_path


# ── CLI ──────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="Generate 3-Minute Book Digest cover image")
    parser.add_argument("--book-name", required=True, help="Book title")
    parser.add_argument("--author", required=True, help="Author name")
    parser.add_argument("--output", required=True, help="Output PNG path")
    parser.add_argument("--bg", help="Background image path (optional, uses first storyboard image)")
    parser.add_argument("--ip-name", default=None, help="Bottom account name (optional, hidden if omitted)")
    parser.add_argument("--width", type=int, default=1920, help="Width (default 1920)")
    parser.add_argument("--height", type=int, default=1080, help="Height (default 1080)")

    args = parser.parse_args()

    generate_cover(
        book_name=args.book_name,
        author_name=args.author,
        output_path=args.output,
        bg_image=args.bg,
        width=args.width,
        height=args.height,
        ip_name=args.ip_name,
    )


if __name__ == "__main__":
    main()
