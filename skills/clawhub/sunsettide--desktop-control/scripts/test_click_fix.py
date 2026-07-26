"""
Test click_text and type_to_text directly (not via IPC).
"""
import sys, os, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

os.environ["TESSERACT_PATH"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
os.environ["PATH"] += r";C:\Program Files\Tesseract-OCR"

import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

import importlib
import daemon.handlers.vision_click
importlib.reload(daemon.handlers.vision_click)
from daemon.handlers.vision_click import handle_find_text, handle_click_text, handle_type_to_text

# 1. find_text should work
r = handle_find_text({"text": "TestOcr", "lang": "eng", "exact_match": False, "limit": 5})
print("find_text:", r.get("count"), "matches")
for m in r.get("matches", []):
    print(f"  \"{m['text']}\" at ({m['x']},{m['y']}) conf={m['confidence']}")

# 2. click_text
r2 = handle_click_text({"text": "TestOcr", "lang": "eng", "exact_match": False, "wait": 0.2})
print("click_text:", r2.get("success"), "| clicked_at:", r2.get("clicked_at"))

# 3. type_to_text
r3 = handle_type_to_text({"text": "TestOcr", "input": " Works!", "anchor": "right", "clear_first": False, "lang": "eng"})
print("type_to_text:", r3.get("success"), "| input_pos:", r3.get("input_position"))
