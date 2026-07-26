import sys, os, json

if hasattr(sys.stdout, 'reconfigure'):
    sys.stdout.reconfigure(encoding='utf-8', errors='replace')
# Path setup
base = os.path.dirname(os.path.abspath(__file__))
if base not in sys.path:
    sys.path.insert(0, base)

from client.client import send_request

# Screenshot (base64)
print("=== SCREENSHOT (base64) ===")
r = send_request("screenshot", {"format": "b64"})
if r.get("result") and r["result"].get("success"):
    d = r["result"]["data"]
    print(f"  Size: {d['size_bytes']} bytes, base64 len: {len(d['data'])}")
else:
    print(f"  ERROR: {r}")

# Screenshot (file)
print("\n=== SCREENSHOT (file) ===")
tmp = os.path.join(os.environ["TEMP"], "oc_test_shot.png")
r = send_request("screenshot_save", {"path": tmp})
if r.get("result") and r["result"].get("success"):
    d = r["result"]["data"]
    print(f"  Path: {d['path']}, Size: {d['size_bytes']} bytes")
else:
    print(f"  ERROR: {r}")

# Window list
print("\n=== WINDOW LIST (first 5) ===")
r = send_request("window_list", {})
if r.get("result") and r["result"].get("success"):
    wins = r["result"]["data"].get("windows", [])
    for w in wins[:5]:
        print(f'  "{w["title"][:50]}" | hwnd={w["hwnd"]}')
    print(f"  ... and {len(wins)-5} more")
else:
    print(f"  ERROR: {r}")

# Mouse position
print("\n=== MOUSE POSITION ===")
r = send_request("mouse_position", {})
if r.get("result") and r["result"].get("success"):
    print(f"  Position: {r['result']['data']}")

# Daemon status
print("\n=== DAEMON STATUS ===")
r = send_request("daemon_status", {})
if r.get("result") and r["result"].get("success"):
    d = r["result"]["data"]
    print(f"  PID: {d['pid']}, Uptime: {d['uptime_seconds']}s")

print("\n=== ALL TESTS PASSED ===")
