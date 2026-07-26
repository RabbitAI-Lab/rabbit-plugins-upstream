import argparse
import base64
import json
import mimetypes
import os
import sys


def guess_mime(path: str) -> str:
    mime, _ = mimetypes.guess_type(path)
    if mime:
        return mime
    ext = os.path.splitext(path)[1].lower()
    fallback = {
        ".png": "image/png",
        ".jpg": "image/jpeg",
        ".jpeg": "image/jpeg",
        ".gif": "image/gif",
        ".webp": "image/webp",
        ".mp4": "video/mp4",
        ".mov": "video/quicktime",
    }
    return fallback.get(ext, "application/octet-stream")


def main():
    sys.stdout.reconfigure(encoding='utf-8', newline='\n')
    parser = argparse.ArgumentParser(
        description="Inject a local media file (image/video) into X compose via the fileInput element. "
                    "Pipe output into `browser-act eval --stdin`."
    )
    parser.add_argument("path", help="Absolute or relative path to the media file on the local filesystem")
    parser.add_argument("--mime", default=None, help="Override MIME type (default: guessed from extension)")
    args = parser.parse_args()

    if not os.path.isfile(args.path):
        print(f"ERROR: file not found: {args.path}", file=sys.stderr)
        sys.exit(2)

    with open(args.path, "rb") as f:
        raw = f.read()

    b64 = base64.b64encode(raw).decode("ascii")
    filename = os.path.basename(args.path)
    mime = args.mime or guess_mime(filename)

    b64_json = json.dumps(b64)
    filename_json = json.dumps(filename)
    mime_json = json.dumps(mime)

    js = f"""
(async () => {{
  try {{
    const b64 = {b64_json};
    const byteStr = atob(b64);
    const ab = new ArrayBuffer(byteStr.length);
    const ia = new Uint8Array(ab);
    for (let i = 0; i < byteStr.length; i++) ia[i] = byteStr.charCodeAt(i);
    const file = new File([ab], {filename_json}, {{ type: {mime_json} }});
    const input = document.querySelector('input[data-testid="fileInput"]');
    if (!input) return JSON.stringify({{ error: true, message: 'fileInput not found -- open compose dialog first' }});
    const dt = new DataTransfer();
    dt.items.add(file);
    input.files = dt.files;
    input.dispatchEvent(new Event('change', {{ bubbles: true }}));
    await new Promise(r => setTimeout(r, 800));
    const thumbs = document.querySelectorAll('[data-testid="attachments"] img, [aria-label*="Media" i][role="img"]');
    return JSON.stringify({{
      injected: true,
      filename: {filename_json},
      mime: {mime_json},
      size_bytes: byteStr.length,
      preview_visible: thumbs.length > 0
    }});
  }} catch (e) {{
    return JSON.stringify({{ error: true, message: e.message }});
  }}
}})()
"""
    print(js)


if __name__ == "__main__":
    main()
