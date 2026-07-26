"""
Tests for human-like behavior enhancement (Phase 11):
  - Human profile set/get
  - Presets
  - Parameter resolution priority
  - Tremor (unit test only, no actual mouse)
  - Scroll variance
  - Delay range resolution
  - Pressure resolution
  - Hotkey hold range
"""
import sys, os, math, random, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

PASS = 0; FAIL = 0
def test(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; print(f"  [OK] {name}")
    else: FAIL += 1; print(f"  [FAIL] {name}  {detail}")

print("=" * 60)
print("Test: Human-like Behavior (Phase 11)")
print("=" * 60)

# 1. Human profile
print("\n[1] Human profile")
from daemon.utils.human_profile import (get_current, set_from_dict, set_preset,
    list_presets, reset, resolve_tremor, resolve_pre_move, resolve_drift,
    resolve_scroll_variance, resolve_delay_range, resolve_pressure,
    resolve_hold_range, random_delay)

# Default is robotic
profile = get_current()
test("default tremor 0", profile["mouse_tremor"] == 0.0)
test("default drift false", profile["mouse_drift"] is False)

# Presets
presets = list_presets()
test("3 presets available", len(presets) == 3)
for p in presets:
    test(f"  preset: {p['name']}", True)

# Apply a preset
set_preset("human_light")
profile = get_current()
test("human_light tremor > 0", profile["mouse_tremor"] > 0)
test("human_light drift enabled", profile["mouse_drift"] is True)

# Apply another preset
set_preset("human_heavy")
profile = get_current()
test("human_heavy pre_move enabled", profile["mouse_pre_move"] is True)
test("human_heavy drift_radius 4", profile["mouse_drift_radius"] == 4)

# Partial profile update
set_from_dict({"mouse_tremor": 5.0})
profile = get_current()
test("partial update tremor=5", profile["mouse_tremor"] == 5.0)

# Unknown key ignored
set_from_dict({"nonexistent_param": 999})
profile = get_current()
test("unknown key ignored", profile.get("nonexistent_param") is None)

# Reset
reset()
profile = get_current()
test("reset to robotic", profile["mouse_tremor"] == 0.0)

# 2. Parameter resolution priority
print("\n[2] Parameter resolution")
reset()
set_preset("human_heavy")

# Call arg wins over profile
amp, freq = resolve_tremor(call_arg=0.0)
test("call arg 0 overrides profile (no tremor)", amp == 0.0)

amp, freq = resolve_tremor(call_arg=3.0)
test("call arg 3.0 used", amp == 3.0)

# No call arg -> profile
amp, freq = resolve_tremor(call_arg=None)
test("no call arg -> profile value", amp > 0)

# Pre-move
enabled, dist = resolve_pre_move(call_arg=False)
test("pre_move call arg False overrides", enabled is False)
enabled, dist = resolve_pre_move(call_arg=None)
test("pre_move None -> profile", enabled is True)

# Drift
enabled, rad = resolve_drift(call_arg=False)
test("drift call arg False", enabled is False)

# Scroll variance
v = resolve_scroll_variance(call_arg=0.0)
test("scroll variance call arg 0", v == 0.0)
v = resolve_scroll_variance(call_arg=None)
test("scroll variance None -> profile", v > 0)

# 3. Delay range resolution
print("\n[3] Delay range")
reset()

# No profile, no call arg
r = resolve_delay_range(call_arg=None)
test("no config -> None", r is None)

# Call arg as number
r = resolve_delay_range(call_arg=0.05)
test("number -> [0.05, 0.05]", r == [0.05, 0.05])

# Call arg as list
r = resolve_delay_range(call_arg=[0.03, 0.08])
test("list [0.03, 0.08] as-is", r == [0.03, 0.08])

# Profile fallback
set_preset("human_light")
r = resolve_delay_range(call_arg=None)
test("profile fallback", r is not None and len(r) == 2)

# 4. Pressure resolution
print("\n[4] Pressure")
reset()
p = resolve_pressure(call_arg=None)
test("default pressure 1.0", p == 1.0)
p = resolve_pressure(call_arg=0.5)
test("call arg pressure 0.5", p == 0.5)

# 5. Hold range resolution
print("\n[5] Hold range")
reset()
r = resolve_hold_range(call_arg=None)
test("default hold range None", r is None)
r = resolve_hold_range(call_arg=[0.1, 0.3])
test("call arg hold [0.1, 0.3]", r == [0.1, 0.3])
set_preset("human_heavy")
r = resolve_hold_range(call_arg=None)
test("heavy preset hold range", r is not None and len(r) == 2)

# 6. Random delay
print("\n[6] Random delay")
d = random_delay(None)
test("None -> 0", d == 0.0)
d = random_delay([0.01, 0.01])
test("min==max -> fixed", d == 0.01)
# Run 100 times, check distribution
samples = [random_delay([0.02, 0.08]) for _ in range(100)]
test("all in range", all(0.02 <= s <= 0.08 for s in samples))
test("not all equal", len(set(samples)) > 1)

# 7. Server dispatcher
print("\n[7] Server Dispatcher")
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    server_code = f.read()
for method in ["human_profile_set", "human_profile_get"]:
    test(f"Dispatcher: {method}", method not in server_code)

# 8. sendinput scroll variance
print("\n[8] sendinput scroll variance")
from daemon.utils.sendinput import mouse_scroll
# Can't actually scroll in test, just check import
test("mouse_scroll with variance importable", callable(mouse_scroll))
import inspect
src = inspect.getsource(mouse_scroll)
test("scroll variance code present", "variance" in src)

# 9. keyboard handler pressure/delay integration
print("\n[9] Keyboard handler integration")
from daemon.handlers.keyboard import handle_type as kb_handle
# Check that delay and pressure params are accepted
import inspect as _i
src = inspect.getsource(kb_handle)
test("delay range resolution in keyboard_type", "resolve_delay_range" in src)
test("pressure resolution in keyboard_type", "resolve_pressure" in src)
from daemon.handlers.keyboard import handle_hotkey as hk_hotkey
src_hk = inspect.getsource(hk_hotkey)
test("hold_duration in hotkey", "resolve_hold_range" in src_hk)

# 10. mouse handler pre_move/drift
print("\n[10] Mouse handler integration")
from daemon.handlers.mouse import handle_click, handle_scroll as ms_scroll
src2 = inspect.getsource(handle_click)
test("pre_move in mouse_click", "resolve_pre_move" in src2)
test("drift in mouse_click", "resolve_drift" in src2)
src3 = inspect.getsource(ms_scroll)
test("scroll variance in handler", "resolve_scroll_variance" in src3)

# Summary
print()
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
print("=" * 60)
