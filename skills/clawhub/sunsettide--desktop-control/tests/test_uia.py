"""Integration test for UIA module: find, click, read text."""
import sys, os, json

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if base not in sys.path:
    sys.path.insert(0, base)

from client.client import send_request


def test(desc, method, params):
    print(f"\n=== {desc} ===")
    r = send_request(method, params)
    if r.get("result") and r["result"].get("success"):
        d = r["result"]["data"]
        if isinstance(d, dict) and "text" in d:
            print(f"  text ({d.get('element_count', '?')} lines): {d.get('text', '')[:200]}")
        elif isinstance(d, dict) and "element" in d:
            elem = d["element"]
            print(f"  name: {elem.get('name', '')}")
            print(f"  type: {elem.get('control_type', '')}")
            print(f"  center: {elem.get('center', {})}")
        else:
            print(f"  result: {json.dumps(d, ensure_ascii=False)[:200]}")
    else:
        print(f"  ERROR: {r.get('error', r)}")
    return r


# Step 1: Launch Notepad (via keyboard hotkey)
print("=== STEP 1: Launch Notepad ===")
r = send_request("keyboard_hotkey", {"keys": ["win", "r"]})
print(f"  Win+R: {r}")
import time
time.sleep(0.5)
r = send_request("keyboard_type", {"text": "notepad"})
print(f"  Type 'notepad': {r}")
time.sleep(0.3)
r = send_request("keyboard_press", {"key": "enter"})
print(f"  Enter: {r}")
time.sleep(2)  # Wait for Notepad to open

# Step 2: Find Notepad window
test("UIA Find Notepad", "uia_find", {"window_title": "Notepad"})

# Step 3: Read Notepad text (should be empty)
test("UIA Read Notepad text", "uia_get_text", {"window_title": "Notepad"})

# Step 4: Type something in Notepad
r = send_request("keyboard_type", {"text": "Hello from UIA test!"})
print(f"\n  Type text: {r}")
time.sleep(0.5)

# Step 5: Read text again (should have our text)
test("UIA Read Notepad text (after typing)", "uia_get_text", {"window_title": "Notepad"})

# Step 6: Close Notepad
r = send_request("keyboard_hotkey", {"keys": ["alt", "f4"]})
print(f"\n  Close Notepad (Alt+F4): {r}")
time.sleep(1)
# Press "Don't Save"
r = send_request("keyboard_press", {"key": "tab"})
print(f"  Tab: {r}")
r = send_request("keyboard_press", {"key": "tab"})
print(f"  Tab: {r}")
r = send_request("keyboard_press", {"key": "enter"})
print(f"  Enter (Don't Save): {r}")

print("\n=== UIA MODULE TESTS COMPLETE ===")
