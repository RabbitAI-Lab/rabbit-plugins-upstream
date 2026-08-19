# -*- coding: utf-8 -*-
"""
Toutiao Publisher Module
=========================
Publishes articles to Toutiao (今日头条) via playwright-cli automation.

This module generates the JavaScript injection scripts and provides
a CLI interface. The actual playwright-cli execution is handled by
the AI agent.

Usage:
    python toutiao_publish.py prepare article.md --output prep/
    python toutiao_publish.py publish --title "标题" --content content.html --images img/
"""
import argparse
import json
import os
import sys
from pathlib import Path


def prepare_content(md_path: str, output_dir: str) -> dict:
    """Prepare content for Toutiao publishing.
    Reads Markdown, extracts images, generates HTML and JS scripts.
    """
    os.makedirs(output_dir, exist_ok=True)

    with open(md_path, encoding="utf-8") as f:
        md_content = f.read()

    # Extract title from first H1
    title = "Untitled"
    lines = md_content.split("\n")
    for line in lines:
        if line.strip().startswith("# "):
            title = line.strip()[2:].strip()
            break

    # Extract image references
    images = []
    for line in lines:
        if line.strip().startswith("!["):
            alt_start = line.find("[") + 1
            alt_end = line.find("]")
            src_start = line.find("(") + 1
            src_end = line.find(")")
            if alt_start > 0 and alt_end > 0 and src_start > 0 and src_end > 0:
                images.append({
                    "alt": line[alt_start:alt_end],
                    "src": line[src_start:src_end],
                    "placeholder": f"[IMG:{len(images)+1}]",
                })

    # Generate ProseMirror injection script
    inject_js = generate_inject_script(md_content, images)

    # Save files
    inject_path = os.path.join(output_dir, "inject_content.js")
    with open(inject_path, "w", encoding="utf-8") as f:
        f.write(inject_js)

    images_json = os.path.join(output_dir, "images.json")
    with open(images_json, "w", encoding="utf-8") as f:
        json.dump({"title": title, "images": images}, f, ensure_ascii=False, indent=2)

    return {
        "title": title,
        "inject_script": inject_path,
        "images_json": images_json,
        "image_count": len(images),
    }


def generate_inject_script(md_content: str, images: list) -> str:
    """Generate ProseMirror paste injection script."""
    # Replace image references with placeholders
    html_content = md_content
    for img in images:
        html_content = html_content.replace(
            f"![{img['alt']}]({img['src']})", img["placeholder"]
        )

    # Convert basic Markdown to HTML
    import re
    html_content = re.sub(r'^### (.+)$', r'<h3>\1</h3>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^## (.+)$', r'<h2>\1</h2>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'^# (.+)$', r'<h1>\1</h1>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'\*\*(.+?)\*\*', r'<strong>\1</strong>', html_content)
    html_content = re.sub(r'^- (.+)$', r'<p>\1</p>', html_content, flags=re.MULTILINE)
    html_content = re.sub(r'\n\n', '</p><p>', html_content)

    # Escape for JS
    html_content = html_content.replace("\\", "\\\\").replace("'", "\\'").replace("\n", "\\n")

    return f"""// Toutiao ProseMirror content injection
(function() {{
  var html = '{html_content}';
  var editor = document.querySelector('.ProseMirror');
  if (!editor) {{ console.error('ProseMirror editor not found'); return; }}

  // Simulate paste event
  var dt = new DataTransfer();
  dt.setData('text/html', html);

  var pasteEvent = new ClipboardEvent('paste', {{
    clipboardData: dt,
    bubbles: true,
    cancelable: true,
  }});

  editor.dispatchEvent(pasteEvent);
  console.log('Content injected successfully');
}})();
"""


def generate_publish_instructions(prepared: dict) -> str:
    """Generate step-by-step publish instructions for AI agent."""
    return f"""# Toutiao Publishing Instructions

## Prepared Files
- Title: {prepared['title']}
- Inject script: {prepared['inject_script']}
- Images config: {prepared['images_json']}
- Image count: {prepared['image_count']}

## Steps (playwright-cli headed mode)

1. Launch playwright-cli in headed mode:
   ```
   playwright-cli open "https://mp.toutiao.com/core/video/edit?from=publish"
   ```

2. Wait for user to scan QR code and login (if needed)

3. Close AI assistant popup:
   ```js
   document.querySelector('.byte-drawer-mask')?.remove();
   document.querySelector('.byte-drawer')?.remove();
   ```

4. Fill title:
   ```js
   var titleInput = document.querySelector('input[placeholder*="标题"]');
   if (titleInput) {{ titleInput.value = '{prepared['title']}'; titleInput.dispatchEvent(new Event('input', {{bubbles:true}})); }}
   ```

5. Inject content (run inject_content.js)

6. Upload images one by one, replacing placeholders

7. Set cover image

8. Click "预览并发布" then "确认发布"

9. Verify success: check URL contains published article ID
"""


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Toutiao publisher")
    subparsers = parser.add_subparsers(dest="command")

    prep = subparsers.add_parser("prepare", help="Prepare article for publishing")
    prep.add_argument("input", help="Markdown article path")
    prep.add_argument("--output", "-o", default="./toutiao-prep", help="Output directory")

    pub = subparsers.add_parser("publish", help="Generate publish instructions")
    pub.add_argument("--title", required=True, help="Article title")
    pub.add_argument("--inject", required=True, help="Inject script path")
    pub.add_argument("--images", required=True, help="Images JSON path")

    args = parser.parse_args()

    if args.command == "prepare":
        result = prepare_content(args.input, args.output)
        print(f"Title: {result['title']}")
        print(f"Inject script: {result['inject_script']}")
        print(f"Images: {result['image_count']}")
        print(f"Images config: {result['images_json']}")
        print(f"\nNext: Use playwright-cli to publish. See instructions in {args.output}/")
    elif args.command == "publish":
        prepared = {"title": args.title, "inject_script": args.inject, "images_json": args.images, "image_count": 0}
        instructions = generate_publish_instructions(prepared)
        print(instructions)
    else:
        parser.print_help()
