#!/usr/bin/env python3
"""
Generate a PDF from a card skill markdown report.

Renders markdown faithfully: pandoc (md -> styled HTML) then
headless Chrome via CDP (HTML -> PDF with no headers/footers).

Usage:
    python3 generate-pdf.py <input.md> [output.pdf]

Requires: pandoc, Google Chrome (or Chromium/Brave/Edge), websocket-client
    pip install websocket-client
"""

import sys
import os
import subprocess
import shutil
import tempfile
import re
import json
import time
import base64
import http.client

SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
CSS_PATH = os.path.join(SCRIPT_DIR, "pdf-style.css")


def find_browser():
    """Find a Chrome-based browser for headless PDF printing."""
    candidates = [
        "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
        "/Applications/Chromium.app/Contents/MacOS/Chromium",
        "/Applications/Brave Browser.app/Contents/MacOS/Brave Browser",
        "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    ]
    for path in candidates:
        if os.path.exists(path):
            return path
    for name in ["google-chrome", "chromium", "chromium-browser"]:
        found = shutil.which(name)
        if found:
            return found
    return None


def md_to_html(md_path):
    """Convert markdown to styled HTML via pandoc, return temp file path."""
    fd, html_path = tempfile.mkstemp(suffix=".html")
    os.close(fd)

    has_css = os.path.exists(CSS_PATH)

    cmd = [
        "pandoc", md_path,
        "-t", "html",
        "--standalone",
        "--metadata", "title=Card Report",
    ]
    if has_css:
        cmd += ["--css", CSS_PATH]

    with open(html_path, "w") as out:
        subprocess.run(cmd, stdout=out, check=True)

    # Inline CSS so Chrome file:// can resolve it
    if has_css:
        with open(CSS_PATH, "r") as f:
            css_content = f.read()
        with open(html_path, "r") as f:
            html = f.read()
        html = re.sub(
            r'<link\s+rel="stylesheet"\s+href="[^"]*"\s*/?>',
            f"<style>\n{css_content}\n</style>",
            html,
            count=1,
        )
        with open(html_path, "w") as f:
            f.write(html)

    return html_path


def print_via_cdp(browser, html_path, pdf_path):
    """Launch headless Chrome, connect via CDP, print PDF with no headers/footers."""
    import websocket

    port = 9223
    proc = subprocess.Popen(
        [
            browser,
            "--headless=new",
            "--disable-gpu",
            "--no-sandbox",
            f"--remote-debugging-port={port}",
            "--remote-allow-origins=*",
            f"file://{html_path}",
        ],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    try:
        # Poll CDP endpoint until Chrome is ready (up to 10s)
        targets = None
        for _ in range(20):
            time.sleep(0.5)
            try:
                conn = http.client.HTTPConnection("127.0.0.1", port)
                conn.request("GET", "/json")
                targets = json.loads(conn.getresponse().read())
                break
            except (ConnectionRefusedError, OSError):
                continue
        if targets is None:
            raise RuntimeError("Chrome did not start within 10 seconds")

        page_target = next(
            (t for t in targets if t.get("type") == "page"), None
        )
        if not page_target:
            raise RuntimeError("No page target found in Chrome CDP")

        ws = websocket.create_connection(page_target["webSocketDebuggerUrl"])

        ws.send(json.dumps({
            "id": 1,
            "method": "Page.printToPDF",
            "params": {
                "displayHeaderFooter": False,
                "printBackground": True,
                "preferCSSPageSize": True,
            },
        }))

        result = json.loads(ws.recv())
        ws.close()

        if "result" not in result or "data" not in result["result"]:
            raise RuntimeError(f"CDP printToPDF failed: {result}")

        pdf_data = base64.b64decode(result["result"]["data"])
        with open(pdf_path, "wb") as f:
            f.write(pdf_data)

        return len(pdf_data)

    finally:
        proc.terminate()
        proc.wait()


def md_to_pdf(md_path, pdf_path):
    """Convert markdown to PDF: pandoc (md->HTML) then Chrome CDP (HTML->PDF)."""
    if not shutil.which("pandoc"):
        print("Error: pandoc not found. Install with: brew install pandoc")
        sys.exit(1)

    browser = find_browser()
    if not browser:
        print("Error: No Chrome-based browser found.")
        sys.exit(1)

    try:
        import websocket  # noqa: F401
    except ImportError:
        print("Installing websocket-client...")
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "websocket-client", "-q"],
            check=True,
        )

    html_path = None
    try:
        html_path = md_to_html(md_path)
        size = print_via_cdp(browser, html_path, pdf_path)
        print(f"PDF generated: {pdf_path} ({size:,} bytes)")
    finally:
        if html_path:
            os.unlink(html_path)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 generate-pdf.py <input.md> [output.pdf]")
        sys.exit(1)

    input_path = sys.argv[1]
    if len(sys.argv) >= 3:
        output_path = sys.argv[2]
    else:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    md_to_pdf(input_path, output_path)
