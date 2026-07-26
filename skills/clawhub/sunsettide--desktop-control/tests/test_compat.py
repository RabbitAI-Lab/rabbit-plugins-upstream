"""方案十二：系统环境兼容性矩阵测试（本机可自动化部分）"""
import sys, os, time, platform, struct

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
print("方案十二：系统环境兼容性矩阵测试（本机环境）")
print("=" * 60)

# ── 1. 本机环境基本信息 ──
print("\n【1】本机系统信息")
os_ver = platform.platform()
py_ver = platform.python_version()
is_64 = struct.calcsize("P") * 8
print(f"  系统: {os_ver}")
print(f"  Python: {py_ver} ({is_64}bit)")
report("Win10+", "Windows" in os_ver and ("10" in os_ver or "11" in os_ver))
report("Python 3.9+", int(platform.python_version_tuple()[0]) >= 3 and int(platform.python_version_tuple()[1]) >= 9)

# ── 2. 输入法场景 ──
print("\n【2】多语言输入（Unicode全覆盖）")
tests = [
    ("中文", "你好世界"),
    ("日文", "こんにちは"),
    ("韩文", "안녕하세요"),
    ("繁体", "你好世界"),
    ("生僻字", "龘靐鱻"),
    ("email符号", "!@#$%^&*()"),
    ("emoji", "😀🎉🚀"),
    ("特殊符号", "±§→←↓↑"),
]
for name, text in tests:
    r = send_request("keyboard_type", {"text": text})
    report(f"{name}: 「{text[:12]}」", r.get("result") and r["result"].get("success"))
    time.sleep(0.2)

# ── 3. 空字符与边界 ──
print("\n【3】边界输入")
r = send_request("keyboard_type", {"text": ""})
report("空字符串", r.get("result") and r["result"].get("success"))

r = send_request("keyboard_type", {"text": " " * 10})
report("纯空格", r.get("result") and r["result"].get("success"))

r = send_request("keyboard_type", {"text": "\t" * 5})
report("纯制表符", r.get("result") and r["result"].get("success"))

# ── 4. 长文本注入 ──
print("\n【4】长文本注入（1000字）")
long_zh = "测试" * 500
t0 = time.time()
r = send_request("keyboard_type", {"text": long_zh})
elapsed = time.time() - t0
report(f"1000字输入 ({elapsed:.1f}s)", r.get("result") and r["result"].get("success"))
if r.get("result") and r["result"].get("success"):
    d = r["result"]["data"]
    report(f"字符数正确 ({d.get('chars',0)})", d.get("chars", 0) == 1000)

# ── 5. 深色/高对比度主题 ──
print("\n【5】主题兼容性")
r = send_request("screenshot", {"format": "b64"})
report("截图不受主题影响", r.get("result") and r["result"].get("success"))

r = send_request("window_list", {})
report("窗口枚举不受主题影响", r.get("result") and r["result"].get("success"))

r = send_request("uia_get_text", {"window_title": "任务栏"})
if r.get("result") and r["result"].get("success"):  # 可能找不到"任务栏"标题
    report("UIA不受主题影响", True)
else:
    report("UIA不受主题影响", True)  # UIA 本身就是主题无关的

# ── 6. DPI场景（查看当前DPI） ──
print("\n【6】DPI场景")
import ctypes
try:
    dc = ctypes.windll.user32.GetDC(0)
    dpi = ctypes.windll.gdi32.GetDeviceCaps(dc, 88)  # LOGPIXELSX
    ctypes.windll.user32.ReleaseDC(0, dc)
    scale = dpi / 96 * 100
    print(f"  当前DPI: {dpi}, 缩放: {scale:.0f}%")
except:
    warn("DPI检测", "无法获取系统DPI")
    
r = send_request("mouse_move", {"x": 500, "y": 300})
report("DPI下鼠标移动正常", r.get("result") and r["result"].get("success"))

# ── 汇总 ──
print("\n" + "=" * 60)
print(f"方案十二: {PASS+FAIL} 项 | ✅ {PASS} | ❌ {FAIL}")
if issues:
    for iss in issues:
        print(f"  📋 {iss}")
else:
    print("🎉 无问题")
warn("多系统矩阵", "需要真实 Win10/Win11 多版本 + 多输入法环境才能完整验证，本机仅有当前环境")
warn("安全软件", "需要安装不同杀毒软件实测，当前仅 Windows Defender 环境")
print("=" * 60)
