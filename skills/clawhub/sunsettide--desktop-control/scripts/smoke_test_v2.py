"""
Desktop Control v1.1.3 — 实操冒烟测试 v2 (fixed response handling)
"""
import sys, os, json, time, math

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

from client.client import send_request

PASS = 0; FAIL = 0
LOG = []

def get_data(r):
    """Extract data from send_request response."""
    if r.get("result") and r["result"].get("success") and r["result"].get("data"):
        return r["result"]["data"]
    if r.get("error"):
        return {"_error": r["error"]}
    return r

def log_result(num, name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; status = "PASS"
    else: FAIL += 1; status = "FAIL"
    LOG.append(f"| {num} | {name} | {status} | {detail[:120]}")
    print(f"  [{'OK' if ok else 'FAIL'}] #{num} {name}")

print("=" * 70)
print("desktop-control v1.1.3 — 实操冒烟测试 v2")
print(f"时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# ── TEST 1 ──
print("\n## 第1项：守护进程状态")
r = send_request("ping", {})
d = get_data(r)
log_result(1, "守护进程在线", d.get("pong"), f"pid={d.get('pid')}")

log_dir = os.path.join(os.environ["LOCALAPPDATA"], "DesktopControl", "Logs") if "LOCALAPPDATA" in os.environ else os.path.join(os.path.expanduser("~"), "DesktopControl", "Logs")
log_result(1, "日志目录存在", os.path.isdir(log_dir), log_dir)

# ── TEST 2: Smooth move (check actual arrival) ──
print("\n## 第2项：鼠标贝塞尔移动")
r = send_request("mouse_move", {"x": 800, "y": 600, "duration": 0.5, "curve": "bezier", "tremor": 2.0})
d = get_data(r)
# Give the async move time to complete
time.sleep(0.7)
r2 = send_request("mouse_position", {})
pos = get_data(r2)
dx = abs(pos.get("x", 0) - 800) if "x" in pos else 999
dy = abs(pos.get("y", 0) - 600) if "y" in pos else 999
log_result(2, "鼠标移动到(800,600)", dx < 20 and dy < 20, f"actual=({pos.get('x')},{pos.get('y')}), dist={math.sqrt(dx*dx+dy*dy):.0f}px")

# ── TEST 3: Relative + bounds ──
print("\n## 第3项：相对移动 + 边界")
r = send_request("mouse_move_relative", {"dx": 100, "dy": 50})
d = get_data(r)
log_result(3, "相对移动返回成功", "from" in d, str(d.get("to", "")))
# Test bounds
r = send_request("mouse_move", {"x": -999, "y": -999})
log_result(3, "负坐标边界保护", "error" in r or not r.get("result", {}).get("success"),
            str(r.get("error", ""))[:60])

# ── TEST 4: English input ──
print("\n## 第4项：英文输入")
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
r = send_request("keyboard_type", {"text": "ManualTest OK "})
d = get_data(r)
log_result(4, "英文输入发送", d.get("chars", 0) > 0, f"chars={d.get('chars')}")
time.sleep(0.1)

# ── TEST 5: Chinese IME Safe ──
print("\n## 第5项：中文IME输入")
r = send_request("keyboard_type", {"text": "中文测试", "ime_safe": True})
d = get_data(r)
log_result(5, "中文输入发送", d.get("chars", 0) > 0, f"chars={d.get('chars')}, method={d.get('method')}")
time.sleep(0.1)

# ── TEST 6: find_text ──
print("\n## 第6项：文字定位")
r = send_request("find_text", {"text": "ManualTest", "exact_match": False, "limit": 5})
d = get_data(r)
matches = d.get("matches", [])
log_result(6, "find_text返回结果", len(matches) > 0, f"{len(matches)} matches")
if matches:
    log_result(6, "坐标格式正确", "x" in matches[0] and "y" in matches[0] and "bbox" in matches[0],
                f"first=({matches[0]['x']},{matches[0]['y']})")

# ── TEST 7: click_text ──
print("\n## 第7项：文字点击")
send_request("window_focus", {"title": "计算器"})
time.sleep(0.5)
r = send_request("click_text", {"text": "5", "wait": 0.2})
d = get_data(r)
log_result(7, "click_text执行", d.get("success"), f"clicked=({d.get('clicked_at',{}).get('x')},{d.get('clicked_at',{}).get('y')})")

# ── TEST 8: type_to_text ──
print("\n## 第8项：锚点输入")
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
r = send_request("type_to_text", {"text": "ManualTest", "input": " ExtraInput!", "anchor": "right", "clear_first": False})
d = get_data(r)
log_result(8, "type_to_text执行", d.get("success"), f"anchor='{d.get('anchor_text','')}' input_len={d.get('input_length')}")
time.sleep(0.2)

# ── TEST 9: Script run ──
print("\n## 第9项：脚本编排")
r = send_request("script_run", {"script": {"steps": [{"action": "nop", "params": {}}, {"action": "sleep", "params": {"duration": 0.2}}]}})
d = get_data(r)
log_result(9, "脚本异步提交", d.get("status") == "running", f"task_id={d.get('task_id','')[:10]}...")
if d.get("task_id"):
    time.sleep(0.5)
    r2 = send_request("script_results", {"task_id": d["task_id"]})
    d2 = get_data(r2)
    log_result(9, "脚本执行完成", d2.get("status") == "completed", f"status={d2.get('status')}")

# ── TEST 10: Human engine ──
print("\n## 第10项：拟人化检测")
from daemon.utils.human_engine import get_engine, reset_engine
reset_engine()
e = get_engine()
level = e.get_level("click", process_name="chrome.exe")
log_result(10, "浏览器拟人化触发", level != "robotic", f"level={level}")
level2 = e.get_level("click", process_name="test.exe")
log_result(10, "非浏览器不触发", level2 == "robotic", f"level={level2}")

# ── SUMMARY ──
print("\n" + "=" * 70)
print(f"✅ {PASS} 通过 / ❌ {FAIL} 失败")
print("=" * 70)
print("\n逐项记录:")
for l in LOG:
    print(l)
print()
if FAIL > 0:
    print("❌ 存在失败项")
    sys.exit(1)
else:
    print("✅ 全部通过!")
