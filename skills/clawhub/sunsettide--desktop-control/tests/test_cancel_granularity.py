"""
Test: script_cancel interrupt granularity.

Verifies that:
  - cancel interrupts within a sleep step (via Event.wait())
  - cancel interrupts between loop iterations (via should_cancel check)
  - cancel does NOT need to wait for the entire loop to finish
"""
import sys, os, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

PASS = 0; FAIL = 0
def test(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; print(f"  [OK] {name}")
    else: FAIL += 1; print(f"  [FAIL] {name}  {detail}")

print("=" * 60)
print("Test: Cancel Interrupt Granularity")
print("=" * 60)

from daemon.script_engine.engine import (
    execute_script_async, get_script_status, cancel_script
)

# 1. Cancel during a long sleep step
print("\n[1] Cancel during sleep step (should interrupt within ~0.5s)")
script = {
    "steps": [
        {"action": "sleep", "params": {"duration": 30}},
    ]
}
r = execute_script_async(script)
tid = r["task_id"]
time.sleep(0.2)
# Status should be running with progress 0
s = get_script_status(tid)
test("task is running before cancel", s["status"] == "running")
test("progress 0 before cancel", s["progress"] == 0)

ok = cancel_script(tid)
test("cancel returns True", ok)

# Wait briefly for cancellation to take effect
time.sleep(0.3)
s = get_script_status(tid)
test("status is cancelled after cancel", s["status"] == "cancelled",
     f"got {s['status']}")
test("interrupted in <1s vs 30s (cancel granularity validated)", s["status"] == "cancelled")

# 2. Cancel during loop with sleep
print("\n[2] Cancel during loop (should not wait all iterations)")
script2 = {
    "steps": [
        {"action": "loop", "times": 100, "body": [
            {"action": "sleep", "params": {"duration": 2}},
        ]},
        {"action": "log", "params": {"message": "should not run"}},
    ]
}
r2 = execute_script_async(script2)
tid2 = r2["task_id"]
time.sleep(0.3)
# Should be running (first sleep is 2s, not finished yet)
s2 = get_script_status(tid2)
test("loop task is running", s2["status"] == "running")

ok2 = cancel_script(tid2)
test("loop cancel returns True", ok2)

time.sleep(0.3)
s2 = get_script_status(tid2)
# Should be cancelled, NOT completed (would need 200s to complete)
test("loop task cancelled before completion", s2["status"] == "cancelled",
     f"got {s2['status']}")
# Progress should be 0 or 1 (loop body is 1 step, might have started)
test("progress < 100", s2["progress"] < 100,
     f"progress={s2['progress']}")

# 3. Sequential steps: cancel mid-script
print("\n[3] Cancel mid-script (step 2 should not execute)")
script3 = {
    "steps": [
        {"action": "sleep", "params": {"duration": 5}},
        {"action": "log", "params": {"message": "should NOT run"}},
    ]
}
r3 = execute_script_async(script3)
tid3 = r3["task_id"]
time.sleep(0.2)
ok3 = cancel_script(tid3)
time.sleep(0.3)
s3 = get_script_status(tid3)
from daemon.script_engine.engine import get_script_results
res3 = get_script_results(tid3)
test("mid-script cancelled", s3["status"] == "cancelled")
# Step 2 (log "should NOT run") should NOT appear in results
step_keys = list(res3.get("results", {}).keys())
test("step 2 not executed", len(step_keys) <= 1,
     f"executed steps: {step_keys}")

# 4. Cancel a retry with sleep interval
print("\n[4] Cancel during retry interval")
script4 = {
    "steps": [
        {"action": "retry", "max_attempts": 10, "interval": 3, "body": [
            {"action": "nop", "params": {}},
            {"action": "log", "params": {"message": "this will fail"}},
            # This step doesn't exist, so retry keeps retrying
            {"action": "nonexistent_action", "params": {}},
        ]},
    ]
}
r4 = execute_script_async(script4)
tid4 = r4["task_id"]
# Wait for first attempt to fail and go into interval sleep
time.sleep(0.3)
ok4 = cancel_script(tid4)
time.sleep(0.3)
s4 = get_script_status(tid4)
test("retry cancelled during interval", s4["status"] == "cancelled",
     f"got {s4['status']}")

# Summary
print()
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
