"""
Final OCR test with module-level tesseract path resolution.
"""
import sys, os, time, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

# Clear all pycaches
for root, dirs, files in os.walk("."):
    for d in list(dirs):
        if d == "__pycache__":
            try: shutil.rmtree(os.path.join(root, d))
            except: pass
print("Cleared __pycache__")

from client.client import send_request

# Kill & restart
try: send_request("daemon_shutdown", {})
except: pass
import time; time.sleep(2)

r = send_request("ping", {})
pid = r.get("result", {}).get("data", {}).get("pid")
print(f"Daemon PID: {pid}")

# Type fresh text
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
send_request("mouse_click", {"x": 100, "y": 200})
time.sleep(0.2)
send_request("keyboard_type", {"text": " ZT_VerifyOCR "})
time.sleep(1)

# Direct find_text
r = send_request("find_text", {"text": "VerifyOCR", "lang": "eng", "exact_match": False, "limit": 5})
d = (r.get("result") or {}).get("data", {})
matches = d.get("matches", [])
print(f"find_text matches: {len(matches)}")
for m in matches:
    print(f'  text="{m.get("text","")}" at ({m.get("x","?")},{m.get("y","?")})')

if matches:
    r2 = send_request("click_text", {"text": "VerifyOCR", "lang": "eng", "exact_match": False, "wait": 0.2})
    d2 = (r2.get("result") or {}).get("data", {})
    print(f"click_text: success={d2.get('success')} at={d2.get('clicked_at')}")
else:
    # Try via ocr handler
    r = send_request("screen_ocr", {"lang": "eng"})
    d = (r.get("result") or {}).get("data", {})
    if d:
        text = d.get("text", "")
        has_text = "VerifyOCR" in text or "ZT_" in text
        print(f"screen_ocr returned {len(text)} chars, found target: {has_text}")
        if has_text:
            print("Tesseract IS actually working, find_text just didn't match!")
        else:
            err = r.get("error", {}).get("message", "unknown")
            print(f"Error: {err[:80]}")
    else:
        err = r.get("error", {}).get("message", "unknown")
        print(f"screen_ocr error: {err[:80]}")
