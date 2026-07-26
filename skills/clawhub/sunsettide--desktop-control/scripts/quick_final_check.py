"""
Final quick check for remaining 3 deep_audit failures.
"""
import sys, os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)
from client.client import send_request

# 15.1 CJK unicode input
r = send_request("keyboard_type", {"text": "测试Test123", "ime_safe": False, "input_method": "unicode"})
d = (r.get("result") or {}).get("data", {})
c1 = d.get("chars", 0) if d else 0
print(f"15.1 CJK: chars={c1} method={d.get('method') if d else '?'} {'PASS' if c1 > 0 else 'FAIL'}")

# 15.2 emoji
r = send_request("keyboard_type", {"text": "🌟🔥", "ime_safe": False})
d = (r.get("result") or {}).get("data", {})
c2 = d.get("chars", 0) if d else 0
print(f"15.2 Emoji: chars={c2} method={d.get('method') if d else '?'} {'PASS' if c2 > 0 else 'FAIL'}")

# 13.5 mouse_click special
r = send_request("mouse_click", {"x": 0, "y": 0})
print(f"13.5 Click 0,0: {r.get('result',{}).get('success')} {'PASS' if r.get('result',{}).get('success') else 'FAIL'}")
