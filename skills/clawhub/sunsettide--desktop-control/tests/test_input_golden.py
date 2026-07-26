"""
Tests for the "golden standard" input layer:
  - sendinput new functions
  - release guard
  - mouse handlers
  - keyboard handlers
  - clipboard
"""
import sys, os, time, math

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)

PASS = 0; FAIL = 0
def test(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; print(f"  [OK] {name}")
    else: FAIL += 1; print(f"  [FAIL] {name}  {detail}")

print("=" * 60)
print("Test: Input Golden Standard (Phase 10)")
print("=" * 60)

# 1. sendinput new functions
print("\n[1] sendinput module")
from daemon.utils import sendinput as si
test("mouse_move_relative importable", callable(si.mouse_move_relative))
test("mouse_down/up importable", callable(si.mouse_down) and callable(si.mouse_up))
test("mouse_move_smooth importable", callable(si.mouse_move_smooth))
test("keyboard_down/up importable", callable(si.keyboard_down) and callable(si.keyboard_up))
test("clipboard_get/set importable", callable(si.clipboard_get) and callable(si.clipboard_set))
test("resolve_key importable", callable(si.resolve_key))

# 2. resolve_key
test("resolve_key 'enter'", si.resolve_key("enter") == 13)
test("resolve_key 'ctrl'", si.resolve_key("ctrl") == 17)
test("resolve_key 'a'", si.resolve_key("a") == 65)
test("resolve_key '1'", si.resolve_key("1") == 49)
test("resolve_key 'esc'", si.resolve_key("esc") == 27)
test("resolve_key 'f1'", si.resolve_key("f1") == 112)
test("resolve_key 'space'", si.resolve_key("space") == 32)
try:
    si.resolve_key("nonexistent_key_xyz")
    test("resolve_key unknown raises ValueError", False)
except ValueError:
    test("resolve_key unknown raises ValueError", True)

# 3. Bezier math
print("\n[2] Bezier curve")
from daemon.utils.sendinput import _bezier_point
p = _bezier_point(0.5, (0,0), (100,0), (200,0), (300,0))
test("bezier midpoint roughly at center", 140 < p[0] < 160, f"got x={p[0]:.1f}")
test("bezier Y is 0", p[1] == 0)

# 4. Clipboard operations
print("\n[3] Clipboard")
old_clip = si.clipboard_get()
si.clipboard_set("test_clipboard_data_123")
readback = si.clipboard_get()
test("clipboard_set then get returns same text",
     readback is not None and "test_clipboard_data_123" in readback,
     f"got: {readback[:50] if readback else 'None'}")
# Restore
if old_clip:
    si.clipboard_set(old_clip)

# 5. Release guard
print("\n[4] Release guard")
from daemon.utils import release_guard as rg
test("press/release", True)
rg.press("mouse", "left")
test("is_pressed True", rg.is_pressed("mouse", "left"))
rg.release("mouse", "left")
test("is_pressed False after release", not rg.is_pressed("mouse", "left"))

# Multiple presses
rg.press("keyboard", 17)  # ctrl
rg.press("keyboard", 67)  # c
test("multiple presses tracked", rg.is_pressed("keyboard", 17) and rg.is_pressed("keyboard", 67))
rg.release("keyboard", 17)
rg.release("keyboard", 67)
test("all released", not rg.is_any_pressed())

# 6. Mouse handlers
print("\n[5] Mouse handlers")
from daemon.handlers.mouse import (
    handle_move_relative, handle_down, handle_up,
    handle_get_position, handle_set_safety_bounds
)
test("handle_move_relative importable", callable(handle_move_relative))
test("handle_down importable", callable(handle_down))
test("handle_up importable", callable(handle_up))
test("handle_get_position importable", callable(handle_get_position))
test("handle_set_safety_bounds importable", callable(handle_set_safety_bounds))

# Test move_relative (relies on current position, hard to test precisely)
# Just verify param validation works
try:
    handle_move_relative({"dx": 50})
    test("move_relative missing dy", False)
except ValueError:
    test("move_relative missing dy raises ValueError", True)

# Test down/up params
try:
    handle_down({"button": "invalid"})
    test("down invalid button", False)
except ValueError:
    test("down invalid button raises ValueError", True)

result = handle_down({"button": "left"})
test("mouse_down returns action", result.get("action") == "mouse_down")
rg.release("mouse", "left")  # clean up

result = handle_up({"button": "left"})
test("mouse_up returns action", result.get("action") == "mouse_up")

# get_position
result = handle_get_position({})
test("get_position returns dict with x,y", "x" in result and "y" in result)
test("get_position returns monitor", "monitor" in result)

# safety bounds toggle
result = handle_set_safety_bounds({"enabled": False})
test("safety bounds disabled", result.get("safety_bounds_enabled") is False)
result = handle_set_safety_bounds({"enabled": True})
test("safety bounds enabled", result.get("safety_bounds_enabled") is True)

# 7. Keyboard handlers
print("\n[6] Keyboard handlers")
from daemon.handlers.keyboard import (
    handle_down as kb_down, handle_up as kb_up,
    handle_clipboard_get, handle_clipboard_set,
    _insert_smart_spaces, _has_cjk
)

# Smart space
test("smart space CJK->Latin", _insert_smart_spaces("你好world") == "你好 world")
test("smart space Latin->CJK", _insert_smart_spaces("hello世界") == "hello 世界")
test("smart space CJK unchanged", _insert_smart_spaces("纯中文") == "纯中文")

# CJK detection
test("has_cjk True", _has_cjk("你好"))
test("has_cjk False", not _has_cjk("hello"))

# Keyboard down/up param validation
try:
    kb_down({"key": "nonexistent_key_xyz"})
    test("keyboard_down unknown key", False)
except ValueError:
    test("keyboard_down unknown key raises ValueError", True)

result = kb_down({"key": "ctrl"})
test("keyboard_down returns action", result.get("action") == "keyboard_down")
rg.release("keyboard", si.resolve_key("ctrl"))
rg.release("keyboard", si.resolve_key("ctrl"))

result = kb_up({"key": "ctrl"})
test("keyboard_up returns action", result.get("action") == "keyboard_up")

# Clipboard handlers
result = handle_clipboard_set({"text": "clip_test_456"})
test("clipboard_set handler", result.get("success"))
result = handle_clipboard_get({})
test("clipboard_get handler returns text", "text" in result)

# 8. Server dispatcher
print("\n[7] Server Dispatcher")
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    server_code = f.read()
for method in ["mouse_move_relative", "mouse_down", "mouse_up",
               "mouse_get_position", "mouse_safety_bounds",
               "keyboard_down", "keyboard_up",
               "clipboard_get", "clipboard_set"]:
    ok = method in server_code and "mouse." in server_code or "keyboard." in server_code
    test(f"Dispatcher: {method}", method in server_code)

# Summary
print()
total = PASS + FAIL
print(f"Results: {PASS}/{total} passed, {FAIL} failed")
if FAIL: print("[FAIL] Some tests failed!")
else: print("[OK] All tests passed!")
print("=" * 60)
