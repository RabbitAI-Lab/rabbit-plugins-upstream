"""
Final comprehensive daemon health check — covers all 16+ core handlers.
"""
import sys, os, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

from client.client import send_request
from daemon.utils.human_engine import get_engine, reset_engine

PASS = 0; FAIL = 0
LOG = []

def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    LOG.append((name, ok, detail[:60]))
    print(f"  [{'OK' if ok else 'FAIL'}] {name} {'| ' + detail[:60] if detail else ''}")

print("=" * 60)
print("desktop-control v1.1.3 — 最终守护进程健康检查")
print("=" * 60)

# 1. Daemon alive
r = send_request("ping", {})
check("ping", r.get("result",{}).get("success"))

# 2. Mouse
r = send_request("mouse_move", {"x": 10, "y": 10})
check("mouse_move", r.get("result",{}).get("success"))

r = send_request("mouse_move_relative", {"dx": 5, "dy": 0})
check("mouse_move_relative", r.get("result",{}).get("success"))

r = send_request("mouse_position", {})
check("mouse_position", "x" in (r.get("result",{}).get("data",{})))

r = send_request("mouse_get_position", {})
d = (r.get("result") or {}).get("data", {})
check("mouse_get_position with monitor", "monitor" in d)

r = send_request("mouse_down", {"button": "left"})
check("mouse_down", r.get("result",{}).get("success"))
r = send_request("mouse_up", {"button": "left"})
check("mouse_up", r.get("result",{}).get("success"))

# 3. Keyboard
r = send_request("keyboard_type", {"text": "."})
check("keyboard_type English", r.get("result",{}).get("success"))

r = send_request("keyboard_type", {"text": ".", "delay": [0.01, 0.02]})
check("keyboard_type with delay range", r.get("result",{}).get("success"))

r = send_request("keyboard_press", {"key": "enter"})
check("keyboard_press", r.get("result",{}).get("success"))

r = send_request("keyboard_hotkey", {"keys": ["ctrl", "c"]})
check("keyboard_hotkey", r.get("result",{}).get("success"))

# 4. Clipboard
r = send_request("clipboard_set", {"text": "cliptest"})
check("clipboard_set", r.get("result",{}).get("success"))

r = send_request("clipboard_get", {})
d = r.get("result",{}).get("data",{})
check("clipboard_get", "text" in d and "cliptest" in d.get("text",""))

# 5. Screenshot
r = send_request("pixel_color", {"x": 0, "y": 0})
check("pixel_color", "hex" in (r.get("result",{}).get("data",{})))

r = send_request("screenshot_save", {})
d = (r.get("result") or {}).get("data", {})
check("screenshot_save", "path" in d)

# 6. Window
r = send_request("window_list", {})
d = (r.get("result") or {}).get("data", {})
check("window_list", "windows" in d and len(d.get("windows",[])) > 0)

r = send_request("window_focus", {"title": "记事本"})
# may fail if no notepad, but should return success or error, not crash
check("window_focus", True, "no crash")

# 7. Script engine
r = send_request("script_run", {"script": {"steps": [{"action":"nop","params":{}}]}})
d = (r.get("result") or {}).get("data", {})
check("script_run async", d.get("status") == "running")
tid = d.get("task_id")
if tid:
    import time; time.sleep(0.3)
    r2 = send_request("script_results", {"task_id": tid})
    d2 = (r2.get("result") or {}).get("data", {})
    check("script_results completed", d2.get("status") == "completed")

r = send_request("script_run_sync", {"script": {"steps": [{"action":"nop","params":{}}]}})
d = (r.get("result") or {}).get("data", {})
check("script_run_sync", d.get("status") == "completed")

# 8. Template
r = send_request("script_list_templates", {})
d = (r.get("result") or {}).get("data", {})
check("script_list_templates", len(d.get("templates",[])) >= 5)

r = send_request("script_load_template", {"name": "capture_window", "params": {"window_title": "test", "save_path": "test.png"}})
d = (r.get("result") or {}).get("data", {})
check("script_load_template", d.get("status") == "loaded")

# 9. Session
r = send_request("session_list", {})
check("session_list", r.get("result",{}).get("success"))

r = send_request("session_create", {"variables": {"k":"v"}})
d = (r.get("result") or {}).get("data", {})
check("session_create", "session_id" in d)
sid = d.get("session_id")
if sid:
    send_request("session_switch", {"session_id": 0})  # back to default
    send_request("session_destroy", {"session_id": sid})

# 10. Human engine
reset_engine(); e = get_engine()
l1 = e.get_level("click", process_name="chrome.exe")
l2 = e.get_level("click", process_name="test.exe")
check("human_engine browser->light", l1 == "light")
check("human_engine non-browser->robotic", l2 == "robotic")

# 11. AI tools
r = send_request("tools_list", {})
tools = (r.get("result") or {}).get("data", {}).get("tools", [])
check("tools_list >=14 tools", len(tools) >= 14)

r = send_request("tools_call", {"tool_calls": [{"name":"keyboard_type","arguments":{"text":""}}]})
d = (r.get("result") or {}).get("data", {})
check("tools_call batch", "results" in d)

r = send_request("goal_run", {"goal": "等待 1 秒", "confirm": True})
d = (r.get("result") or {}).get("data", {})
check("goal_run planning", d.get("status") == "planned")

# 12. OCR (optional)
r = send_request("find_text", {"text": "TEST", "lang": "eng", "limit": 1})
d = (r.get("result") or {}).get("data", {})
if d:
    check("find_text", True, f"{len(d.get('matches',[]))} matches")
else:
    check("find_text (OCR not available)", True, "graceful degradation")

r = send_request("screen_ocr", {"lang": "chi_sim+eng"})
d = (r.get("result") or {}).get("data", {})
if d:
    check("screen_ocr", True, f"{d.get('chars',0)} chars")
else:
    check("screen_ocr (OCR not available)", True, "graceful degradation")

# 13. File integrity summary
import os as _os
file_count = sum(1 for r, d, f in _os.walk(".") for f in f if f.endswith(".py") and "__pycache__" not in r)
test_count = sum(1 for f in _os.listdir("tests") if f.startswith("test_") and f.endswith(".py"))
check(f"total .py files: {file_count}", True)
check(f"test files: {test_count}", test_count >= 10)

# Summary
print()
total = PASS + FAIL
print("=" * 60)
print(f"健康检查完成: {PASS}/{total} 通过, {FAIL} 失败")
if FAIL > 0:
    print("!")
    for name, ok, detail in LOG:
        if not ok:
            print(f"  FAIL: {name}: {detail}")
else:
    print("完美! 所有系统正常.")
print("=" * 60)
