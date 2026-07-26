"""方案十一：时序与操作精度专项测试"""
import sys, os, time, json, random

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0
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

def warn(name, detail):
    print(f"  ⚠️  {name}: {detail}")
    issues.append(f"{name}: {detail}")

print("=" * 60)
print("方案十一：时序与操作精度专项测试")
print("=" * 60)

# 【1】连续点击不丢失
print("\n【1】连续点击100次（100ms间隔）")
fail_count = 0
for i in range(100):
    r = send_request("mouse_click", {"button": "left"})
    if not (r.get("result") and r["result"].get("success")):
        fail_count += 1
    time.sleep(0.1)
report(f"100次点击: 失败{fail_count}次", fail_count == 0)

# 【2】拖拽落点精度
print("\n【2】拖拽落点精度（重复20次）")
for i in range(20):
    r = send_request("mouse_drag", {"start_x": 100, "start_y": 100, "end_x": 500, "end_y": 500})
    if not (r.get("result") and r["result"].get("success")):
        report(f"拖拽#{i+1}", False, str(r.get("error")))
        break
    time.sleep(0.2)
else:
    report("20次拖拽全部成功", True)

# 【3】快捷键时序正确性
print("\n【3】快捷键时序")
keys_tests = [
    (["ctrl", "c"], "Ctrl+C"),
    (["ctrl", "v"], "Ctrl+V"),
    (["ctrl", "a"], "Ctrl+A"),
    (["ctrl", "shift", "s"], "Ctrl+Shift+S"),
    (["alt", "tab"], "Alt+Tab"),
    (["win", "d"], "Win+D"),
    (["win", "e"], "Win+E"),
]
for keys, name in keys_tests:
    r = send_request("keyboard_hotkey", {"keys": keys})
    report(f"{name}", r.get("result") and r["result"].get("success"))
    time.sleep(0.5)

# 【4】双击一致性
print("\n【4】双击一致性（50次）")
for i in range(50):
    r = send_request("mouse_click", {"button": "left", "clicks": 2})
    if not (r.get("result") and r["result"].get("success")):
        report(f"双击#{i+1}", False, str(r.get("error")))
        break
    time.sleep(0.15)
else:
    report("50次双击全部成功", True)

# 【5】长按有效性（测试 SendInput 的 hold 能力不实际可见，验证接口正常）
print("\n【5】长按接口验证")
# SendInput 按下释放是成对的，没有问题
report("长按按下返回", send_request("keyboard_press", {"key": "shift"}).get("result"))
time.sleep(0.2)
report("长按释放返回", send_request("keyboard_press", {"key": "shift"}).get("result"))

# 【6】系统动画中操作
print("\n【6】动画中操作")
r = send_request("window_list", {})
if r.get("result") and r["result"].get("success"):
    wins = r["result"]["data"].get("windows", [])
    target = None
    for w in wins:
        t = w.get("title", "")
        if t.strip() and t not in ("Program Manager", "NVIDIA GeForce Overlay", "Windows 输入体验", "任务栏", "设置"):
            target = t
            break
    if target:
        # 先最大化窗口，在动画过程中立即发指令
        send_request("window_maximize", {"title": target})
        time.sleep(0.05)  # 立即发送，窗口动画可能还在播放
        r = send_request("mouse_click", {"button": "left"})
        report(f"最大化动画中点击 ({target[:30]}...)", r.get("result") and r["result"].get("success"))
        time.sleep(0.5)
        
        # 最小化过程中
        send_request("window_minimize", {"title": target})
        time.sleep(0.05)
        r = send_request("mouse_click", {"button": "left"})
        report("最小化动画中点击", r.get("result") and r["result"].get("success"))
        
        # 恢复窗口
        send_request("window_focus", {"title": target})
        time.sleep(0.3)

# ── 汇总 ──
print("\n" + "=" * 60)
print(f"方案十一: {PASS+FAIL} 项 | ✅ {PASS} | ❌ {FAIL}")
if issues:
    for iss in issues:
        print(f"  📋 {iss}")
else:
    print("🎉 无问题")
print("=" * 60)
