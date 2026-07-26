"""
Final OCR test: type text, find it via IPC, click on it.
"""
import sys, os, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

os.environ["TESSERACT_PATH"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

from client.client import send_request

send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
send_request("mouse_click", {"x": 100, "y": 200})
time.sleep(0.3)
send_request("keyboard_type", {"text": " FinalFindMe42 "})
time.sleep(1)

r = send_request("find_text", {"text": "FinalFindMe", "lang": "eng", "exact_match": False, "limit": 5})
d = (r.get("result") or {}).get("data", {})
matches = d.get("matches", [])
print(f"find_text: {len(matches)} matches")
for m in matches:
    print(f"  text={m['text']!r} at ({m['x']},{m['y']})")

if matches:
    r2 = send_request("click_text", {"text": "FinalFindMe", "lang": "eng", "exact_match": False, "wait": 0.2})
    d2 = (r2.get("result") or {}).get("data", {})
    print(f"click_text: success={d2.get('success')} at={d2.get('clicked_at')}")
else:
    print("No matches found.")
