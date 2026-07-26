"""方案一：底层接口全量遍历测试（不依赖 OpenClaw）"""
import os, sys, json, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0
TOTAL = 0

def test(name, method, params=None, check=None):
    global PASS, FAIL, TOTAL
    TOTAL += 1
    params = params or {}
    try:
        r = send_request(method, params)
        ok = r.get("result") and r["result"].get("success")
        if check:
            ok = ok and check(r["result"]["data"])
        status = "✅ PASS" if ok else "❌ FAIL"
        if ok:
            PASS += 1
        else:
            FAIL += 1
            err = r.get("error", r)
            print(f"  {status} {name}: {err}")
            return
        print(f"  {status} {name}")
    except Exception as e:
        FAIL += 1
        print(f"  ❌ FAIL {name}: {e}")


print("=" * 60)
print("方案一：底层接口全量遍历测试")
print("=" * 60)

# ── 1. 守护进程启动 ──
print("\n【守护进程启停】")
test("ping (自动拉起)", "ping")
test("daemon_status", "daemon_status",
     check=lambda d: "pid" in d and "uptime_seconds" in d)

# ── 2. 鼠标功能 ──
print("\n【鼠标功能】")
test("mouse_move (500,300)", "mouse_move", {"x": 500, "y": 300})
time.sleep(0.3)
test("mouse_click left", "mouse_click", {"button": "left"})
time.sleep(0.3)
test("mouse_click right", "mouse_click", {"x": 700, "y": 400, "button": "right"})
time.sleep(0.3)
test("mouse_drag", "mouse_drag", {"start_x": 100, "start_y": 100, "end_x": 300, "end_y": 300})
time.sleep(0.3)
test("mouse_scroll", "mouse_scroll", {"clicks": -3})
time.sleep(0.3)
test("mouse_position", "mouse_position",
     check=lambda d: "x" in d and "y" in d)

# ── 3. 键盘功能 ──
print("\n【键盘功能】")
test("keyboard_type ASCII", "keyboard_type", {"text": "hello openclaw"})
time.sleep(0.3)
test("keyboard_type Unicode", "keyboard_type", {"text": "你好世界"})
time.sleep(0.3)
test("keyboard_hotkey ctrl+a", "keyboard_hotkey", {"keys": ["ctrl", "a"]})
time.sleep(0.3)
test("keyboard_press enter", "keyboard_press", {"key": "enter"})
time.sleep(0.3)
test("keyboard_press tab 3x", "keyboard_press", {"key": "tab", "times": 3})
time.sleep(0.3)

# ── 4. 截图功能 ──
print("\n【截图功能】")
test("screenshot b64", "screenshot", {"format": "b64"},
     check=lambda d: "data" in d and len(d["data"]) > 1000)
time.sleep(0.3)
tmp = os.path.join(os.environ["TEMP"], "oc_test_screenshot.png")
test("screenshot_save", "screenshot_save", {"path": tmp},
     check=lambda d: os.path.exists(d.get("path", "")))
time.sleep(0.3)

# ── 5. 窗口管理 ──
print("\n【窗口管理】")
test("window_list", "window_list",
     check=lambda d: "windows" in d and len(d["windows"]) > 0)
time.sleep(0.3)

# 获取第一个有标题的窗口来测试 focus/minimize
r = send_request("window_list", {})
if r.get("result") and r["result"].get("success"):
    wins = r["result"]["data"].get("windows", [])
    target = None
    for w in wins:
        t = w.get("title", "")
        if t.strip() and t not in ("Program Manager", "NVIDIA GeForce Overlay", "Windows 输入体验"):
            target = t
            break
    if target:
        print(f"  [选用窗口: {target[:40]}]")
        test("window_focus", "window_focus", {"title": target})
        time.sleep(0.3)
        test("window_info", "window_info", {"title": target},
             check=lambda d: "hwnd" in d)
        time.sleep(0.3)
        test("window_minimize", "window_minimize", {"title": target})
        time.sleep(0.5)
        test("window_maximize", "window_maximize", {"title": target})
        time.sleep(0.5)
        test("window_focus (restore)", "window_focus", {"title": target})
        time.sleep(0.3)
    else:
        print("  ⏭️ 跳过窗口操作（无可操作窗口）")
else:
    print("  ⏭️ 跳过窗口操作（window_list 失败）")

# ── 6. UIA 测试 ──
print("\n【UIA 自动化】")
# 先用快捷键打开记事本
send_request("keyboard_hotkey", {"keys": ["win", "r"]})
time.sleep(0.5)
send_request("keyboard_type", {"text": "notepad"})
time.sleep(0.3)
send_request("keyboard_press", {"key": "enter"})
time.sleep(2)  # 等待记事本打开

test("uia_find Notepad", "uia_find", {"window_title": "Notepad"},
     check=lambda d: d.get("element", {}).get("name", "").find("Notepad") >= 0 or d.get("element", {}).get("name", "").find("记事本") >= 0)
time.sleep(0.3)

test("uia_get_text Notepad", "uia_get_text", {"window_title": "Notepad"},
     check=lambda d: "text" in d)
time.sleep(0.3)

# 在记事本里输入文字
send_request("keyboard_type", {"text": "OpenClaw 桌面控制测试"})
time.sleep(0.5)

test("uia_get_text (after typing)", "uia_get_text", {"window_title": "Notepad"},
     check=lambda d: len(d.get("text", "")) > 20)
time.sleep(0.3)

# 关闭记事本
send_request("keyboard_hotkey", {"keys": ["alt", "f4"]})
time.sleep(1)
send_request("keyboard_press", {"key": "tab"})
time.sleep(0.2)
send_request("keyboard_press", {"key": "tab"})
time.sleep(0.2)
send_request("keyboard_press", {"key": "enter"})
time.sleep(0.5)

# ── 7. 守护进程停止 ──
print("\n【守护进程停止】")
test("daemon_shutdown", "daemon_shutdown")
time.sleep(1)

# 验证进程已消失
r = send_request("ping", {})
if not (r.get("result") and r["result"].get("success")):
    PASS += 1
    print(f"  ✅ PASS ping after shutdown (expected failure)")
else:
    FAIL += 1
    print(f"  ❌ FAIL ping after shutdown (should fail)")
TOTAL += 1

# ── 最终统计 ──
print("\n" + "=" * 60)
print(f"总测试: {TOTAL} | ✅ 通过: {PASS} | ❌ 失败: {FAIL}")
if FAIL == 0:
    print("🎉 方案一全部通过！")
else:
    print(f"⚠️  有 {FAIL} 项失败，需要排查")
print("=" * 60)
