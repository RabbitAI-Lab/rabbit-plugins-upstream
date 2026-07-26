"""方案六：系统边界与特殊场景测试（可自动化部分）"""
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
    global PASS, FAIL, WARN
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
print("方案六：系统边界与特殊场景测试（可自动化部分）")
print("=" * 70)

# ── 1. 高DPI / 多显示器 ──
print("\n【1. 多显示器 / 高DPI 适配】")
# 获取实际显示器信息
r = send_request("screenshot", {"format": "b64"})
if r.get("result") and r["result"].get("success"):
    size = r["result"]["data"].get("size_bytes", 0)
    report("截图可以捕获画面", size > 10000)
else:
    report("截图正常", False, str(r.get("error")))

# 多显示器坐标测试
r = send_request("mouse_move", {"x": 2000, "y": 500})
report("副屏坐标移动（如有）", r.get("result") and r["result"].get("success"))

r = send_request("mouse_position", {})
if r.get("result") and r["result"].get("success"):
    pos = r["result"]["data"]
    warn(f"鼠标当前位置", f"({pos['x']}, {pos['y']}) — 请目视检查是否与副屏位置一致")

# ── 2. 全屏场景 ──
print("\n【2. 全屏场景适配】")
# 先将鼠标移到安全位置
send_request("mouse_move", {"x": 100, "y": 100})
r = send_request("screenshot", {"format": "b64"})
report("全屏截图正常", r.get("result") and r["result"].get("success"))

r = send_request("mouse_click", {"button": "left"})
report("全屏下鼠标点击正常", r.get("result") and r["result"].get("success"))
warn("全屏游戏场景", "无法自动化测试，需要手动在游戏/视频全屏下验证截图+点击是否生效，并在文档说明")

# ── 3. 远程桌面 ──
print("\n【3. 远程桌面场景】")
warn("RDP 场景", "无法自动化测试，需手动通过 mstsc 远程连接后验证截图非黑屏、键鼠正常")

# ── 4. 超长文本输入 ──
print("\n【4. 边界输入测试】")
long_text = "A" * 100000
r = send_request("keyboard_type", {"text": long_text})
report("10万字符输入", r.get("result") and r["result"].get("success"),
       "注意：实际输入可能被系统限制截断")
# 清理：按几次退格
for _ in range(3):
    send_request("keyboard_press", {"key": "backspace"})

# ── 5. 特殊字符 ──
print("\n【5. 特殊字符输入】")
special = "!@#$%^&*()_+-=[]{}|;':\",./<>?~`\n\t"
r = send_request("keyboard_type", {"text": special})
report("特殊字符输入", r.get("result") and r["result"].get("success"))

# ── 6. 超长参数 ──
print("\n【6. 超长/畸形参数】")
# 超大 JSON（通过 client 直接构造，不走 json load）
# 测试超长参数通过 client CLI
import subprocess
cli_base = os.path.join(BASE, "client", "client.py")
result = subprocess.run(
    [sys.executable, cli_base, "mouse_move", '{"x": 999999, "y": 999999}'],
    capture_output=True, text=True, timeout=10
)
try:
    r = json.loads(result.stdout.strip())
    report("超大坐标参数", r.get("result") and r["result"].get("success"))
except:
    report("超大坐标参数", False, result.stderr[:200] if result.stderr else "parse error")

# ── 7. 空参数
print("\n【7. 空参数/缺参数】")
r = send_request("mouse_move", {})
report("缺坐标的 mouse_move（预期失败）", r.get("error") is not None,
       str(r))

# ── 汇总 ──
print("\n" + "=" * 70)
print(f"方案六: 自动化测试完毕")
print(f"✅ 通过: {PASS} | ❌ 失败: {FAIL} | ⚠️ 需人工验证: {WARN}")
if issues:
    print(f"\n📋 问题记录:")
    for iss in issues:
        print(f"  - {iss}")
print("=" * 70)
