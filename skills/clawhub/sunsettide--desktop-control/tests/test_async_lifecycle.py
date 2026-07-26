"""
Test: async script lifecycle (status, cancel, results)
"""
import sys, os, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

PASS = 0; FAIL = 0
def test(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; print(f"  [OK] {name}")
    else: FAIL += 1; print(f"  [FAIL] {name}  {detail}")

print("=" * 60)
print("Test: Async Script Lifecycle")
print("=" * 60)

from daemon.script_engine.engine import (
    execute_script_async, get_script_status,
    get_script_results, cancel_script
)

# 1. Basic async run
r = execute_script_async({
    "steps": [
        {"action": "nop", "params": {}},
        {"action": "nop", "params": {}},
        {"action": "nop", "params": {}},
    ]
})
tid = r["task_id"]
test("script_run returns task_id", bool(tid))
test("script_run status is running", r["status"] == "running")
test("total_steps is 3", r["total_steps"] == 3)

# 2. Progress tracking
time.sleep(0.5)
s = get_script_status(tid)
test("script_status returns dict", isinstance(s, dict))
test("  status completed", s["status"] == "completed")
test("  progress 3/3", s["progress"] == 3 and s["total"] == 3)

# 3. Get results
res = get_script_results(tid)
test("script_results status", res["status"] == "completed")
test("  has 3 results", len(res["results"]) == 3)
test("  all success", all(v["success"] for v in res["results"].values()))

# 4. Cancel a running script
r2 = execute_script_async({
    "steps": [
        {"action": "sleep", "params": {"duration": 5}},
        {"action": "log", "params": {"message": "should not run"}},
    ]
})
tid2 = r2["task_id"]
ok = cancel_script(tid2)
test("cancel returns True", ok)
time.sleep(0.3)
s2 = get_script_status(tid2)
test("cancelled status", s2["status"] == "cancelled")

# 5. Cancel non-existent returns False
ok = cancel_script("nonexistent_task_id")
test("cancel non-existent returns False", not ok)

# 6. Status non-existent returns None
s3 = get_script_status("nonexistent_task_id")
test("status non-existent returns None", s3 is None)

# 7. Sync path still works
from daemon.script_engine.engine import execute_script
result = execute_script({"steps": [{"action": "nop", "params": {}}]})
test("sync execute_script", result["status"] == "completed")

# Summary
print()
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
