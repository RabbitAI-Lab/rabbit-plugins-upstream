"""
Test: 20 rapid mixed IPC operations (ensuring no rate limit or connection loss).
"""
import sys, os, json
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE); os.chdir(BASE)
from client.client import send_request

failed = 0
for i in range(20):
    ops = [("mouse_move", {"x": i*10, "y": i*10}), ("keyboard_type", {"text": "."}), ("ping", {})]
    method, params = ops[i % 3]
    r = send_request(method, params)
    ok = r.get("result", {}).get("success") if r.get("result") else False
    if not ok:
        failed += 1
        if failed <= 3:
            err = r.get("error", {}).get("message", "unknown") if r.get("error") else "no result"
            print(f"FAIL #{i} {method}: {err}")

print(f"20 rapid mixed ops: {20 - failed}/20 passed")
if failed == 0: print("ALL OK")
