# -*- coding: utf-8 -*-
"""Render briefing.html -> A4 poster PDF using the locally cached Chromium.

Dependency:
    pip install playwright
    (no Chromium download needed; we reuse the already-cached chrome.exe under
     %LOCALAPPDATA%\\ms-playwright\\chromium-*\\chrome-win64\\chrome.exe)

Run AFTER build_*.py has produced briefing.html in OUT_DIR.
"""
import os, glob
from playwright.sync_api import sync_playwright

# ⚠️ Keep OUT_DIR pointed at the REAL working dir. Never bulk-sed the date into
#    this path — that silently rewrites the directory name and breaks everything.
OUT_DIR = r"C:\Users\Administrator\WorkBuddy\automation-2026-07-27-20-34-05\outputs"
HTML_PATH = os.path.join(OUT_DIR, "briefing.html")
# PDF filename MUST carry the date so daily runs don't overwrite each other.
PDF_PATH = os.path.join(OUT_DIR, "金融创新简报_财富管理_2026-07-28.pdf")

candidates = glob.glob(r"C:\Users\Administrator\AppData\Local\ms-playwright\chromium-*\chrome-win64\chrome.exe")
EXE = sorted(candidates)[-1] if candidates else None
if not EXE:
    raise SystemExit("No cached chrome.exe found under %LOCALAPPDATA%\\ms-playwright")
print("Using Chromium:", EXE)

with sync_playwright() as p:
    browser = p.chromium.launch(
        executable_path=EXE,
        headless=True,
        args=["--no-sandbox", "--disable-gpu", "--disable-dev-shm-usage"],
    )
    page = browser.new_page(viewport={"width": 1240, "height": 1754}, device_scale_factor=2)
    page.goto("file:///" + HTML_PATH.replace("\\", "/"), wait_until="networkidle")
    page.pdf(
        path=PDF_PATH,
        format="A4",
        print_background=True,
        margin={"top": "0mm", "bottom": "0mm", "left": "0mm", "right": "0mm"},
        prefer_css_page_size=True,   # respect @page { size: A4; margin: 0 }
        display_header_footer=False,
    )
    browser.close()
print("PDF generated:", PDF_PATH)
