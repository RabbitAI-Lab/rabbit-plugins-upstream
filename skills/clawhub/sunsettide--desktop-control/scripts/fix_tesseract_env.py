"""
Fix TESSERACT_PATH env var not being passed to daemon.
"""
import sys, os, time, winreg

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

# Read TESSERACT_PATH from Windows registry
try:
    key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, "Environment")
    tess_path, _ = winreg.QueryValueEx(key, "TESSERACT_PATH")
    os.environ["TESSERACT_PATH"] = tess_path
    print(f"Read TESSERACT_PATH from registry: {tess_path}")
except Exception as e:
    print(f"Registry read failed: {e}")
    # Fallback to default path
    tess_path = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
    if os.path.isfile(tess_path):
        os.environ["TESSERACT_PATH"] = tess_path
        print(f"Using default path: {tess_path}")

# Kill daemon
from client.client import send_request
try:
    send_request("daemon_shutdown", {})
    print("Daemon shutdown requested")
except:
    print("No daemon to shutdown (first start)")
time.sleep(2)

# Restart
r = send_request("ping", {})
pid = r.get("result", {}).get("data", {}).get("pid")
print(f"Daemon restarted, pid={pid}")

# Ensure TESSERACT_PATH is set for the current process
import ctypes
HWND_BROADCAST = 0xffff
WM_SETTINGCHANGE = 0x001A
ctypes.windll.user32.SendMessageW(HWND_BROADCAST, WM_SETTINGCHANGE, 0, "Environment")

# Now test
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
send_request("keyboard_type", {"text": "TestOCR_Verify "})
time.sleep(1)

r = send_request("find_text", {"text": "TestOCR", "lang": "eng", "exact_match": False, "limit": 5})
d = (r.get("result") or {}).get("data", {})
matches = d.get("matches", [])
print(f"find_text matches: {len(matches)}")
if matches:
    r2 = send_request("click_text", {"text": "TestOCR", "lang": "eng", "exact_match": False, "wait": 0.2})
    d2 = (r2.get("result") or {}).get("data", {})
    print(f"click_text: success={d2.get('success')} at={d2.get('clicked_at')}")
else:
    print("OCR not working via IPC - trying direct handler call")
    import daemon.handlers.vision_click as vc
    import importlib
    importlib.reload(vc)
    from daemon.handlers.vision_click import handle_find_text
    try:
        import pytesseract
        pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
        r3 = handle_find_text({"text": "TestOCR", "lang": "eng", "exact_match": False, "limit": 5})
        print(f"direct handler: {len(r3.get('matches',[]))} matches")
    except Exception as e:
        print(f"direct handler error: {e}")
