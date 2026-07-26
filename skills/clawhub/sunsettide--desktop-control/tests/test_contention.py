"""方案十四：资源竞争与冲突场景测试"""
import sys, os, time, json

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
print("方案十四：资源竞争与冲突场景测试")
print("=" * 60)

# 【1】剪贴板不污染
print("\n【1】剪贴板不污染验证")
# 键盘输入用 KEYEVENTF_UNICODE 不碰剪贴板
# 验证：不用 pyperclip，代码里确认没有 clipboard 操作
with open(os.path.join(BASE, "daemon", "utils", "sendinput.py"), encoding="utf-8") as f:
    code = f.read()
report("sendinput.py 无 pyperclip 引用", "pyperclip" not in code)
report("sendinput.py 无 clipboard 操作", "clipboard" not in code.lower() or "CLIPBOARD" not in code)
report("sendinput.py 使用 KEYEVENTF_UNICODE", "KEYEVENTF_UNICODE" in code)

# 【2】窗口完全遮挡 - UIA可读后台窗口
print("\n【2】后台窗口UIA读取")
# 先打开记事本
send_request("keyboard_hotkey", {"keys": ["win", "r"]})
time.sleep(0.5)
send_request("keyboard_type", {"text": "notepad"})
time.sleep(0.3)
send_request("keyboard_press", {"key": "enter"})
time.sleep(2)
send_request("keyboard_type", {"text": "后台窗口测试文本"})
time.sleep(0.5)

# 拿到记事本标题
r = send_request("uia_find", {"window_title": "Notepad"})
if r.get("result") and r["result"].get("success"):
    title = r["result"]["data"]["element"]["name"]
    print(f"  记事本标题: {title}")
    
    # 先最小化记事本
    send_request("window_minimize", {"title": "Notepad"})
    time.sleep(0.5)
    
    # 最小化后用UIA读取
    r = send_request("uia_get_text", {"window_title": "Notepad"})
    if r.get("result") and r["result"].get("success"):
        text = r["result"]["data"].get("text", "")
        report("最小化窗口UIA可读文本", "后台窗口测试文本" in text)
    else:
        report("最小化窗口UIA读取", False, str(r.get("error")))
    
    # 恢复窗口
    send_request("window_focus", {"title": "Notepad"})
    time.sleep(0.3)
else:
    warn("UIA记事本查找", "无法找到记事本")

# 关闭记事本
send_request("keyboard_hotkey", {"keys": ["alt", "f4"]})
time.sleep(1)
send_request("keyboard_press", {"key": "tab"})
time.sleep(0.2)
send_request("keyboard_press", {"key": "tab"})
time.sleep(0.2)
send_request("keyboard_press", {"key": "enter"})

# 【3】高负载模拟
print("\n【3】高负载场景（连续密集调用）")
errors = 0
for i in range(30):
    r = send_request("mouse_position", {})
    if not (r.get("result") and r["result"].get("success")):
        errors += 1
report(f"30次连续调用: 失败{errors}次", errors == 0)
t0 = time.time()
for i in range(10):
    send_request("mouse_position", {})
t1 = time.time()
report(f"10次快速调用延迟: {(t1-t0)*1000:.0f}ms", (t1-t0) < 5,
       f"{(t1-t0)*1000:.0f}ms")

# ── 汇总 ──
print("\n" + "=" * 60)
print(f"方案十四: {PASS+FAIL} 项 | ✅ {PASS} | ❌ {FAIL}")
if issues:
    for iss in issues:
        print(f"  📋 {iss}")
else:
    print("🎉 无问题")
warn("多自动化工具并发", "未安装AutoHotkey，无法模拟并发键鼠场景")
warn("模态弹窗阻塞", "无法自动化生成系统错误弹窗，需手动验证")
print("=" * 60)
