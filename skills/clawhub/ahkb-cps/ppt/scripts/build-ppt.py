#!/usr/bin/env python3
"""
build-ppt.py — Insert slides into master template, with auto base64 image embedding.

Usage:
    python scripts/build-ppt.py _slides.html -o output.html -t "Title"
    python scripts/build-ppt.py _slides.html -o output.html -t "Title" --open
    python scripts/build-ppt.py _slides.html -o output.html -t "Title" --images-dir "图片及其他资源/images"

Supports img:// placeholder syntax in slides HTML:
    <img src="img://filename.png" alt="">
    → auto-converted to <img src="data:image/png;base64,...">
"""

import os, re, sys, argparse, base64, mimetypes, webbrowser

SKILL_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER_HTML = os.path.join(SKILL_DIR, 'templates', 'master.html')

# MIME type fallback for extensions mimetypes may not know
MIME_FALLBACK = {
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.gif': 'image/gif',
    '.webp': 'image/webp',
    '.bmp': 'image/bmp',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.tiff': 'image/tiff',
    '.tif': 'image/tiff',
}


def get_mime(filename):
    """Get MIME type from filename, with fallback for common types."""
    mime, _ = mimetypes.guess_type(filename)
    if mime:
        return mime
    ext = os.path.splitext(filename)[1].lower()
    return MIME_FALLBACK.get(ext, 'application/octet-stream')


def embed_slide_images(slides_html, images_dir):
    """Replace all img://filename.ext placeholders with base64 data URIs.

    Scans slides_html for src="img://<filename>" patterns, finds each file
    in images_dir, converts to base64, and replaces the placeholder.
    If a file is not found, a warning is printed and placeholder stays unchanged.
    """
    def _replacer(match):
        full_src = match.group(2)          # e.g. img://photo.png
        if not full_src.startswith('img://'):
            return match.group(0)
        filename = full_src[6:]            # strip 'img://'
        if not filename:
            return match.group(0)

        # Search in images_dir directly
        img_path = os.path.join(images_dir, filename)
        if not os.path.isfile(img_path):
            print("  [WARN] image not found: %s" % img_path)
            return match.group(0)

        try:
            with open(img_path, 'rb') as f:
                b64_data = base64.b64encode(f.read()).decode('ascii')
            mime = get_mime(filename)
            data_uri = 'data:%s;base64,%s' % (mime, b64_data)
            size_kb = len(b64_data) * 3 // 4 // 1024
            print("  [IMG] %s -> %d KB (%s)" % (filename, size_kb, mime))
            return 'src="%s"' % data_uri
        except Exception as e:
            print("  [ERROR] failed to convert %s: %s" % (filename, e))
            return match.group(0)

    # Match src="img://..." (double quotes) or src='img://...' (single quotes)
    slides_html = re.sub(r'src=(["\'])(img://[^"\']+)\1', _replacer, slides_html)

    # Match CSS background(-image): url(img://...)
    def _css_replacer(match):
        filename = match.group(1)
        if not filename:
            return match.group(0)
        img_path = os.path.join(images_dir, filename)
        if not os.path.isfile(img_path):
            print("  [WARN] CSS image not found: %s" % img_path)
            return match.group(0)
        try:
            with open(img_path, 'rb') as f:
                b64_data = base64.b64encode(f.read()).decode('ascii')
            mime = get_mime(filename)
            data_uri = 'data:%s;base64,%s' % (mime, b64_data)
            size_kb = len(b64_data) * 3 // 4 // 1024
            print("  [IMG] %s -> %d KB (%s)" % (filename, size_kb, mime))
            return 'url(%s)' % data_uri
        except Exception as e:
            print("  [ERROR] failed to convert %s: %s" % (filename, e))
            return match.group(0)

    slides_html = re.sub(r'url\(["\']?img://([^"\')\s]+)["\']?\)', _css_replacer, slides_html)
    return slides_html


def main():
    parser = argparse.ArgumentParser(
        description='build-ppt — Insert slides into master template with auto base64 images'
    )
    parser.add_argument('slides_file', help='Path to the slides HTML file')
    parser.add_argument('-o', '--output', required=True, help='Output HTML file path')
    parser.add_argument('-t', '--title', default='Presentation', help='Page title')
    parser.add_argument('--open', action='store_true', help='Auto-open in browser after build')
    parser.add_argument('--images-dir', default=None,
                        help='Directory containing images for img:// placeholders. '
                             'If not set, img:// references are left as-is.')
    args = parser.parse_args()

    if not os.path.isfile(args.slides_file):
        print("Error: slides file not found: %s" % args.slides_file)
        sys.exit(1)

    if not os.path.isfile(MASTER_HTML):
        print("Error: template not found: %s" % MASTER_HTML)
        sys.exit(1)

    with open(args.slides_file, 'r', encoding='utf-8') as f:
        slides_html = f.read().strip()

    # ── Step 1: Embed images (replace img:// placeholders with base64) ──
    img_count = slides_html.count('img://')
    if img_count > 0 and args.images_dir:
        if not os.path.isdir(args.images_dir):
            print("Error: images-dir not found: %s" % args.images_dir)
            sys.exit(1)
        print("Embedding %d image(s) from: %s" % (img_count, args.images_dir))
        slides_html = embed_slide_images(slides_html, args.images_dir)
    elif img_count > 0 and not args.images_dir:
        print("Warning: %d img:// placeholder(s) found but --images-dir not set. Skipping." % img_count)

    # ── Step 2: Insert into template ──
    with open(MASTER_HTML, 'r', encoding='utf-8') as f:
        template_html = f.read()

    # Update title
    template_html = re.sub(
        r'<title>[^<]*</title>',
        f'<title>{args.title}</title>',
        template_html
    )

    # Replace slides between markers
    start_marker = '<!--SLIDES_START-->'
    end_marker = '<!--SLIDES_END-->'

    start_idx = template_html.find(start_marker)
    end_idx = template_html.find(end_marker)

    if start_idx == -1 or end_idx == -1:
        print("Error: Could not find SLIDES_START/SLIDES_END markers in template")
        sys.exit(1)

    before = template_html[:start_idx + len(start_marker)]
    after = template_html[end_idx:]

    output_html = before + '\n' + slides_html + '\n' + after

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write(output_html)

    print("OK Built: %s" % args.output)
    print("  Title: %s" % args.title)
    print("  Slides count: %d" % slides_html.count('<section class="slide'))

    if args.open:
        abs_path = os.path.abspath(args.output)
        webbrowser.open(abs_path)
        print("  Opened in browser: %s" % abs_path)


if __name__ == '__main__':
    main()
