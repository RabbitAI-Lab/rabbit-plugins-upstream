"""
Force-set TESSERACT_PATH in registry, clear cache, restart daemon.
"""
import sys, os, time, ctypes, winreg, shutil

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

# 1. Set registry
key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment", 0, winreg.KEY_SET_VALUE)
winreg.SetValueEx(key, "TESSERACT_PATH", 0, winreg.REG_SZ, r"C:\Program Files\Tesseract-OCR\tesseract.exe")
winreg.CloseKey(key)
print("Registry updated")

# 2. Broadcast environment change
ctypes.windll.user32.SendMessageW(0xffff, 0x001A, 0, "Environment")
time.sleep(0.5)

# 3. Set in current process
os.environ["TESSERACT_PATH"] = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# 4. Clear all __pycache__
for root, dirs, files in os.walk("."):
    for d in list(dirs):
        if d == "__pycache__":
            try:
                shutil.rmtree(os.path.join(root, d))
            except:
                pass
print("Cleared __pycache__")

# 5. Kill daemon
from client.client import send_request
try:
    send_request("daemon_shutdown", {})
    print("Daemon shutdown")
except:
    pass
time.sleep(2)

# 6. Restart - should get TESSERACT_PATH from registry
r = send_request("ping", {})
pid = r.get("result", {}).get("data", {}).get("pid")
print(f"Daemon restarted: pid={pid}")

# 7. Test OCR
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
send_request("mouse_click", {"x": 100, "y": 200})
time.sleep(0.2)
send_request("keyboard_type", {"text": " OCR_FinalTest42 "})
time.sleep(1)

r = send_request("find_text", {"text": "FinalTest", "lang": "eng", "exact_match": False, "limit": 5})
d = (r.get("result") or {}).get("data", {})
matches = d.get("matches", [])
print(f"find_text: {len(matches)} matches")
for m in matches:
    print(f"  text={m['text']!r} at ({m['x']},{m['y']})")

if matches:
    r2 = send_request("click_text", {"text": "FinalTest", "lang": "eng", "exact_match": False, "wait": 0.2})
    d2 = (r2.get("result") or {}).get("data", {})
    print(f"click_text: success={d2.get('success')} at={d2.get('clicked_at')}")
else:
    # Check inside the daemon process
    print("Still no OCR. Checking daemon's actual env...")
    print(f"  os.environ.get('TESSERACT_PATH') = {os.environ.get('TESSERACT_PATH')}")
    print(f"  File exists: {os.path.isfile(r'C:\Program Files\Tesseract-OCR\tesseract.exe')}")
