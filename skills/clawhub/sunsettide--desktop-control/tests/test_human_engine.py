"""
Tests for context-aware humanization engine (replaces manual profile switch).
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
print("Test: Context-Aware Human Engine")
print("=" * 60)

# 1. Human engine basic
print("\n[1] Engine defaults")
from daemon.utils.human_engine import HumanEngine, reset_engine
# Create isolated instance (not singleton) so _detect_active_process doesn't interfere
h = HumanEngine()
test("engine creation", isinstance(h, HumanEngine))
# With explicit process_name=empty and no counter, should be robotic
# Bypass window-class detection by faking a non-browser PID
# (HumanEngine._detect_browser_from_class picks up real browser windows)
h._current_window_pid = 12345
h._last_active_time = 0.0
level = h.get_level("click", process_name="test.exe")
test("non-browser, no context -> robotic", level == "robotic", f"got {level}")

# With browser process name, should be light even on first call
level = h.get_level("click", process_name="chrome.exe")
test("browser first op -> light", level == "light", f"got {level}")

# 2. User override
print("\n[2] User override")
# Create a fresh instance directly (not singleton) for isolation
e2 = HumanEngine()
level = e2.get_level("click", user_override="off")
test("user override 'off' -> robotic", level == "robotic")
level = e2.get_level("click", user_override="light")
test("user override 'light' -> light", level == "light")
level = e2.get_level("click", user_override="heavy")
test("user override 'heavy' -> heavy", level == "heavy")

# 3. Browser detection
print("\n[3] Browser detection")
b = HumanEngine()
level = b.get_level("click", process_name="chrome.exe")
test("browser -> light on first op", level == "light", f"got {level}")

level = b.get_level("click", process_name="msedge.exe")
test("edge -> light", level == "light", f"got {level}")

# 4. Op counter escalation (direct state manipulation)
print("\n[4] Op counter")
from daemon.utils.humanize import apply_human_params
p = apply_human_params({"x": 0, "y": 0}, "light")
test("light preset has tremor", p.get("tremor", 0) > 0)

# 5. apply_human_params
print("\n[5] apply_human_params")

params = apply_human_params({"x": 100, "y": 200}, "robotic")
test("robotic: no extra keys", "tremor" not in params, f"keys={list(params.keys())}")

params = apply_human_params({"x": 100, "y": 200}, "light")
test("light: tremor added", "tremor" in params, f"extra={params.get('tremor')}")
test("light: drift enabled", params.get("drift") is True)
test("light: drift_radius present", params.get("drift_radius") == 2)

params = apply_human_params({"x": 100, "y": 200}, "heavy")
test("heavy: pre_move enabled", params.get("pre_move") is True)
test("heavy: delay added", "delay" in params)

# Caller params override profile
params = apply_human_params({"x": 100, "y": 200, "tremor": 0.0}, "light")
test("caller tremor=0 overrides profile", params.get("tremor") == 0.0)

# 6. Injection in handlers
print("\n[6] Handler injection")
import inspect
from daemon.handlers.mouse import (handle_move, handle_click, handle_scroll,
    handle_move_relative, handle_drag, handle_down, handle_up)
from daemon.handlers.keyboard import (handle_type, handle_press, handle_hotkey,
    handle_down as kb_down, handle_up as kb_up)

handlers = [handle_move, handle_click, handle_scroll, handle_move_relative,
            handle_drag, handle_down, handle_up,
            handle_type, handle_press, handle_hotkey, kb_down, kb_up]

for h in handlers:
    src = inspect.getsource(h)
    has_human = "_inject_human" in src or "params = _inject_human" in src
    test(f"{h.__name__} injects human params", has_human,
         "missing _inject_human call")

# 7. Server dispatcher (no human_profile_set/get)
print("\n[7] Server dispatcher (no manual profile handlers)")
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    server_code = f.read()
test("no human_profile_set in dispatcher", "human_profile_set" not in server_code)
test("no human_profile_get in dispatcher", "human_profile_get" not in server_code)
test("human import removed", "human_profile" not in server_code)

# Summary
print()
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
print("=" * 60)
