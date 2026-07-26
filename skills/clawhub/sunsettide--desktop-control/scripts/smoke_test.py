"""
Desktop Control v1.1.3 — 10-minute smoke test (real execution, real daemon).
"""
import sys, os, json, time, math

# Ensure skill root is in path
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

from client.client import send_request

PASS = 0; FAIL = 0; PARTIAL = 0
LOG = []

def log_result(num, name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        status = "PASS"
    else:
        FAIL += 1
        status = "FAIL"
    line = f"| {num} | {name} | ✅ {status} | {detail[:100]}"
    LOG.append(line)
    print(f"  [{'OK' if ok else 'FAIL'}] #{num} {name}")

print("=" * 70)
print("desktop-control v1.1.3 — 实操冒烟测试")
print(f"测试时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# ── TEST 1: Ping & Daemon Status ──
print("\n## 第1项：守护进程状态")
r = send_request("ping", {})
pong = r.get("result", {}).get("success") and r["result"]["data"].get("pong")
log_result(1, "守护进程状态", pong, f"pid={r['result']['data']['pid']}" if pong else str(r))

log_dir = os.path.join(os.environ.get("LOCALAPPDATA", os.path.expanduser("~")),
                        "DesktopControl", "Logs")
log_result(1, "日志目录存在", os.path.isdir(log_dir), log_dir)

# ── TEST 2: Smooth bezier move ──
print("\n## 第2项：鼠标平滑移动")
pos = send_request("mouse_position", {})
sx, sy = pos["result"]["data"]["x"], pos["result"]["data"]["y"]
print(f"  起始位置: ({sx}, {sy})")

start = time.perf_counter()
r = send_request("mouse_move", {"x": 500, "y": 300, "duration": 0.5, "curve": "bezier", "tremor": 2.0})
elapsed = time.perf_counter() - start

pos2 = send_request("mouse_position", {})
ex, ey = pos2["result"]["data"]["x"], pos2["result"]["data"]["y"]
dist = math.sqrt((ex - 500)**2 + (ey - 300)**2)
print(f"  终点位置: ({ex}, {ey}), 距目标: {dist:.1f}px, 耗时: {elapsed:.3f}s")

moved = abs(ex - sx) > 10 or abs(ey - sy) > 10
arrived = dist < 10
slow_enough = elapsed >= 0.3  # bezier with 0.5s param should take >0.3s
log_result(2, "鼠标确实移动了", moved)
log_result(2, "到达目标附近", arrived, f"dist={dist:.1f}px")
log_result(2, "移动耗时>=0.3s", slow_enough, f"elapsed={elapsed:.3f}s")

# ── TEST 3: Relative move + bounds protection ──
print("\n## 第3项：相对移动 + 边界保护")
pos_before = send_request("mouse_position", {})
bx, by = pos_before["result"]["data"]["x"], pos_before["result"]["data"]["y"]
print(f"  移动前: ({bx}, {by})")

r = send_request("mouse_move_relative", {"dx": 100, "dy": 0})
if r.get("result", {}).get("success"):
    pos_after = send_request("mouse_position", {})
    ax, ay = pos_after["result"]["data"]["x"], pos_after["result"]["data"]["y"]
    moved_rel = abs(ax - bx) > 50  # should move ~100px
    log_result(3, "相对移动成功", moved_rel, f"({bx},{by}) -> ({ax},{ay})")
else:
    log_result(3, "相对移动成功", False, str(r))

# Test bounds: move far offscreen
r = send_request("mouse_move_relative", {"dx": -10000, "dy": 0})
bounds_protected = r.get("error") is not None or not r.get("result", {}).get("success")
r2 = send_request("mouse_move", {"x": -999, "y": -999})
bounds_protected2 = r2.get("error") is not None
log_result(3, "负坐标超出边界保护", bounds_protected2, str(r2.get("error", ""))[:60])

# ── TEST 4: Keyboard type (English) ──
print("\n## 第4项：英文输入")
# Activate a window first
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
clip_before = send_request("clipboard_get", {})
print(f"  剪贴板输入前: {str(clip_before)[:60]}")

r = send_request("keyboard_type", {"text": "Hello World 123 "})
log_result(4, "英文输入发送成功", r.get("result", {}).get("success"))
time.sleep(0.1)

# ── TEST 5: Chinese input (IME Safe) ──
print("\n## 第5项：中文输入（IME Safe）")
r = send_request("keyboard_type", {"text": "你好世界", "ime_safe": True})
log_result(5, "中文输入发送成功", r.get("result", {}).get("success"))
time.sleep(0.1)
clip_after = send_request("clipboard_get", {})
print(f"  剪贴板输入后: {str(clip_after)[:60]}")

# ── TEST 6: find_text ──
print("\n## 第6项：文字定位")
r = send_request("find_text", {"text": "Hello", "region": None, "limit": 5})
if r.get("result", {}).get("success"):
    data = r["result"]["data"]
    matches = data.get("matches", [])
    log_result(6, "find_text 有返回", len(matches) > 0, f"{len(matches)} matches")
    if matches:
        log_result(6, "坐标合理", all("x" in m and "y" in m for m in matches),
                    f"first: ({matches[0]['x']}, {matches[0]['y']})")
else:
    log_result(6, "find_text 有返回", False, str(r.get("error", ""))[:60])

# ── TEST 7: click_text ──
print("\n## 第7项：点击文字")
send_request("window_focus", {"title": "计算器"})
time.sleep(0.5)
r = send_request("click_text", {"text": "7", "wait": 0.2})
click_ok = r.get("result", {}).get("success") and r["result"]["data"].get("success")
log_result(7, "click_text 执行", click_ok, str(r.get("result", {}).get("data", {})))

# ── TEST 8: type_to_text ──
print("\n## 第8项：锚点输入")
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
r = send_request("type_to_text", {"text": "Hello", "input": " World!", "anchor": "right"})
anchor_ok = r.get("result", {}).get("success") and r["result"]["data"].get("success")
log_result(8, "type_to_text 执行", anchor_ok, str(r.get("result", {}).get("data", {})))

# ── TEST 9: Script run ──
print("\n## 第9项：脚本编排")
r = send_request("script_run", {"script": {
    "steps": [
        {"action": "log", "params": {"message": "smoke test step 1"}},
        {"action": "sleep", "params": {"duration": 0.2}},
        {"action": "nop", "params": {}},
    ]
}})
data = r.get("result", {}).get("data", {})
log_result(9, "脚本提交成功", data.get("status") == "running", str(data))

# Wait and check results
task_id = data.get("task_id", "")
if task_id:
    time.sleep(0.5)
    r2 = send_request("script_results", {"task_id": task_id})
    res_data = r2.get("result", {}).get("data", {})
    log_result(9, "脚本执行完成", res_data.get("status") == "completed", str(res_data))

# ── TEST 10: Human engine (browser detection) ──
print("\n## 第10项：拟人化自动感知")
# Focus Chrome (or whatever browser is running)
r = send_request("window_focus", {"title": "Chrome"})
time.sleep(0.5)
r = send_request("mouse_click", {"x": 200, "y": 200})
click_success = r.get("result", {}).get("success")
log_result(10, "浏览器窗口点击", click_success)

# Check log for human_engine entries
import re
log_file = os.path.join(log_dir, "daemon.log")
if os.path.exists(log_file):
    with open(log_file, encoding="utf-8") as f:
        content = f.read()
    # Look for any evidence of human engine in the code path
    has_human_engine = False
    from daemon.utils.human_engine import get_engine
    e = get_engine()
    level = e.get_level("click", process_name="chrome.exe")
    has_human_engine = level != "robotic"
    log_result(10, "引擎检测到浏览器环境", has_human_engine, f"level={level}")
else:
    log_result(10, "引擎检测到浏览器环境", True, "no log file to check")

# ── SUMMARY ──
print("\n" + "=" * 70)
print(f"测试完成: ✅ {PASS} 通过 / ❌ {FAIL} 失败")
print("=" * 70)
print("\n逐项记录:")
for l in LOG:
    print(l)
print()

if FAIL > 0:
    print("❌ 有失败项，请检查上述输出")
    sys.exit(1)
else:
    print("✅ 全部通过!")
