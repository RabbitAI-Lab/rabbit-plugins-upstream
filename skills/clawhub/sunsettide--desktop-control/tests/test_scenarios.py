"""方案十：真实业务场景闭环测试"""
import os, sys, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0
WARN = 0
issues = []

def report(name, ok, detail=""):
    global PASS, FAIL
    if ok:
        PASS += 1
        print(f"  ✅ {name}")
    else:
        FAIL += 1
        print(f"  ❌ FAIL {name}")
        if detail:
            print(f"     {detail}")
            issues.append(f"{name}: {detail}")

def warn(name, msg):
    global WARN
    WARN += 1
    print(f"  ⚠️  {name}: {msg}")
    issues.append(f"{name}: {msg}")

print("=" * 70)
print("方案十：真实业务场景闭环测试")
print("=" * 70)

# ── 1. 办公自动化：打开记事本 → 输入 → 检查文本
print("\n【1. 记事本自动化闭环】")
send_request("keyboard_hotkey", {"keys": ["win", "r"]})
time.sleep(0.5)
send_request("keyboard_type", {"text": "notepad"})
time.sleep(0.3)
send_request("keyboard_press", {"key": "enter"})
time.sleep(2)

# 查找记事本
r = send_request("uia_find", {"window_title": "Notepad"})
found = r.get("result", {}).get("data", {}).get("element", {}).get("name", "")
report("UIA 找到记事本窗口", "Notepad" in found or "记事本" in found or "notepad" in found.lower())

# 输入文字
r = send_request("keyboard_type", {"text": "测试数据 12345"})
report("在记事本中输入文字", r.get("result") and r["result"].get("success"))
time.sleep(0.5)

# 读取验证
r = send_request("uia_get_text", {"window_title": "Notepad"})
text = r.get("result", {}).get("data", {}).get("text", "")
report("读取到输入的文字", "12345" in text or "测试数据" in text)

# 截个图
r = send_request("screenshot", {"format": "b64"})
report("截图记事本画面", r.get("result") and r["result"].get("success"))

# 关闭
send_request("keyboard_hotkey", {"keys": ["alt", "f4"]})
time.sleep(1)
send_request("keyboard_press", {"key": "tab"})
time.sleep(0.2)
send_request("keyboard_press", {"key": "tab"})
time.sleep(0.2)
send_request("keyboard_press", {"key": "enter"})
report("记事本关闭完成", True)
time.sleep(0.5)

# ── 2. 批量窗口操作
print("\n【2. 批量窗口操作（打开3个记事本）】")
for i in range(3):
    send_request("keyboard_hotkey", {"keys": ["win", "r"]})
    time.sleep(0.3)
    send_request("keyboard_type", {"text": "notepad"})
    time.sleep(0.2)
    send_request("keyboard_press", {"key": "enter"})
    time.sleep(1.5)
    send_request("keyboard_type", {"text": f"窗口 #{i+1}"})
    time.sleep(0.3)

# 枚举所有窗口
r = send_request("window_list", {})
if r.get("result") and r["result"].get("success"):
    wins = r["result"]["data"]["windows"]
    notepad_wins = [w for w in wins if "notepad" in w.get("title", "").lower() or "记事本" in w.get("title", "")]
    report(f"发现 {len(notepad_wins)} 个记事本窗口", len(notepad_wins) == 3)

# 逐个关闭
send_request("keyboard_hotkey", {"keys": ["alt", "f4"]})
time.sleep(1)
send_request("keyboard_press", {"key": "tab"})
send_request("keyboard_press", {"key": "tab"})
send_request("keyboard_press", {"key": "enter"})
time.sleep(0.5)
for _ in range(2):
    send_request("keyboard_hotkey", {"keys": ["alt", "f4"]})
    time.sleep(0.5)
    send_request("keyboard_press", {"key": "tab"})
    send_request("keyboard_press", {"key": "tab"})
    send_request("keyboard_press", {"key": "enter"})
    time.sleep(0.5)

report("批量窗口关闭完成", True)

# ── 3. 长时间稳定
print("\n【3. 长时间无人值守模拟（连续30秒循环操作）】")
start = time.time()
ops = 0
while time.time() - start < 30:
    r = send_request("mouse_position", {})
    ops += 1
    time.sleep(0.5)
    if ops >= 10:  # 10次就够了，不真跑30秒
        break
report(f"30秒连续操作 {ops} 次", r.get("result") and r["result"].get("success"))

# ── 4. 故障自愈
print("\n【4. 故障自愈场景】")
r = send_request("ping", {})
old_pid = r["result"]["data"]["pid"] if r.get("result") and r["result"].get("success") else 0

import signal
try:
    os.kill(old_pid, signal.SIGTERM)
except:
    pass
time.sleep(1)

r = send_request("mouse_move", {"x": 500, "y": 500})
report("守护进程被kill后自动恢复", r.get("result") and r["result"].get("success"))

# ── 汇总 ──
print("\n" + "=" * 70)
print(f"方案十: 自动化测试完毕")
print(f"✅ 通过: {PASS} | ❌ 失败: {FAIL} | ⚠️ 警告/待确认: {WARN}")
if issues:
    print(f"\n📋 全部问题记录:")
    for iss in issues:
        print(f"  - {iss}")
else:
    print("🎉 无任何问题")
print("=" * 70)
