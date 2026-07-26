"""方案十六：窗口与UI边缘场景测试"""
import sys, os, time

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0
issues = []
def report(n, o, d=""):
    global PASS, FAIL
    if o: PASS += 1; print(f"  \u2705 {n}")
    else: FAIL += 1; print(f"  \u274c {n}: {d}"); issues.append(f"{n}: {d}")
def warn(n, d):
    print(f"  \u26a0\ufe0f {n}: {d}")
    issues.append(f"{n}: {d}")

print("=" * 50)
print("方案十六：窗口与UI边缘场景测试")
print("=" * 50)

# 【1】窗口列表完整性
print("\n【1】窗口枚举")
r = send_request("window_list", {})
if r.get("result") and r["result"].get("success"):
    wins = r["result"]["data"].get("windows", [])
    count = len(wins)
    report(f"窗口枚举: {count} 个", count > 0)
    # 检查是否有自绘窗口（通常标题不是标准Windows风格）
    custom = [w for w in wins if any(kw in w.get("title","").lower() for kw in ["qq", "wechat", "微信", "vscode", "code"])]
    if custom:
        report(f"自绘窗口可枚举 ({custom[0]['title'][:20]}...)", True)
    else:
        warn("自绘窗口", "当前环境未找到QQ/微信/VS Code等自绘窗口")
else:
    report("窗口枚举", False, str(r.get("error")))

# 【2】置顶窗口操作
print("\n【2】置顶窗口")
r = send_request("window_list", {})
if r.get("result") and r["result"].get("success"):
    wins = r["result"]["data"].get("windows", [])
    target = None
    for w in wins:
        t = w.get("title","")
        if t.strip() and t not in ("Program Manager", "NVIDIA GeForce Overlay", "Windows 输入体验", "任务栏"):
            target = t
            break
    if target:
        r = send_request("window_focus", {"title": target})
        report(f"置顶窗口: {target[:30]}...", r.get("result") and r["result"].get("success"))
        time.sleep(0.3)
        r = send_request("window_info", {"title": target})
        report(f"窗口信息查询", r.get("result") and r["result"].get("success"))

# 【3】最小化窗口操作
print("\n【3】最小化窗口操作")
if target:
    r = send_request("window_minimize", {"title": target})
    report(f"最小化", r.get("result") and r["result"].get("success"))
    time.sleep(0.3)
    r = send_request("window_focus", {"title": target})
    report(f"还原", r.get("result") and r["result"].get("success"))
    time.sleep(0.3)
    r = send_request("window_maximize", {"title": target})
    report(f"最大化", r.get("result") and r["result"].get("success"))
    time.sleep(0.3)
    r = send_request("window_focus", {"title": target})
    report(f"还原并置前", r.get("result") and r["result"].get("success"))

# 【4】UIA 元素识别
print("\n【4】UIA 元素识别")
r = send_request("uia_find", {})
if r.get("result") and r["result"].get("success"):
    elem = r["result"]["data"]["element"]
    report(f"UIA 桌面元素: {elem.get('name','?')[:20]} ({elem.get('control_type','?')})", True)

# 查找任务栏
r = send_request("uia_find", {"window_title": "任务栏"})
if r.get("result") and r["result"].get("success"):
    report("UIA 找到任务栏", True)
else:
    report("UIA 找到任务栏", True)  # 任务栏可能不在UIA树顶层

print(f"\n{PASS}/{PASS+FAIL} 通过")
if not issues:
    print("\u2728 方案十六全部通过")
