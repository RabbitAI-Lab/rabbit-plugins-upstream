"""
Test OCR with English find_text / click_text.
Requires: Tesseract English language pack (already installed).
"""
import sys, os, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

os.environ["TESSERACT_PATH"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from client.client import send_request

PASS = 0; FAIL = 0; SKIP = 0
def log(rnum, name, ok, detail=""):
    global PASS, FAIL, SKIP
    if ok: PASS += 1; s = "PASS"
    else: FAIL += 1; s = "FAIL"
    print(f"  [{s}] #{rnum} {name}: {detail[:100]}")

print("=" * 60)
print("OCR find_text / click_text 实操测试 (英文)")
print("=" * 60)

# 1. Verify Tesseract works directly
print("\n## 准备")
from PIL import Image, ImageDraw
img = Image.new("RGB", (300, 40), "white")
draw = ImageDraw.Draw(img)
draw.text((10, 10), "TestOCR 2025", fill="black")
t = pytesseract.image_to_string(img, lang="eng")
log(0, "Tesseract引擎可用", "TestOCR" in t, t.strip()[:30])

# 2. Type text in Notepad, then find it
print("\n## find_text 实操")
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
send_request("keyboard_type", {"text": "TestOCR_FindMe_42 "})
time.sleep(1.0)

r = send_request("find_text", {"text": "TestOCR", "exact_match": False, "limit": 5, "lang": "eng"})
d = (r.get("result") or {}).get("data", {})
matches = d.get("matches", [])
log(6, "find_text英文定位", len(matches) > 0, f"{len(matches)} matches")
if matches:
    for m in matches:
        print(f"     text=\"{m['text']}\" at ({m['x']},{m['y']}) conf={m['confidence']}")
    has_bbox = all("bbox" in m for m in matches)
    log(6, "边界框格式正确", has_bbox)

# 3. click_text on the found text
print("\n## click_text 实操")
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
r = send_request("click_text", {"text": "TestOCR_FindMe", "lang": "eng", "wait": 0.3})
d2 = (r.get("result") or {}).get("data", {})
click_ok = d2.get("success", False)
log(7, "click_text英文点击", click_ok, f"position={d2.get('clicked_at')}")

# 4. type_to_text
print("\n## type_to_text 实操")
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
r = send_request("type_to_text", {"text": "TestOCR_FindMe", "input": " TypeHere!", "anchor": "right", "clear_first": False, "lang": "eng"})
d3 = (r.get("result") or {}).get("data", {})
log(8, "type_to_text英文锚点", d3.get("success", False), f"input_len={d3.get('input_length')}")

# Summary
total = PASS + FAIL
print(f"\n{'='*60}")
print(f"✅ {PASS} / {total} 通过 | ❌ {FAIL} 失败")
if FAIL > 0:
    print("❌ 有失败项"); sys.exit(1)
else:
    print("✅ 全部通过")
