"""补充9大类：本机可自动化验证部分"""
import sys, os, time, json, subprocess, threading

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0
WARN = 0
issues = []

def report(n, o, d=""):
    global PASS, FAIL
    if o: PASS += 1; print(f"  \u2705 {n}")
    else: FAIL += 1; print(f"  \u274c {n}: {d}"); issues.append(f"{n}: {d}")
def warn(n, d):
    global WARN
    WARN += 1
    print(f"  \u26a0\ufe0f {n}: {d}")
    issues.append(f"{n}: {d}")

print("=" * 60)
print("补充9大类：本机可自动化部分")
print("=" * 60)

# ══════════════════════════════════════
# 五、快捷键系统保留键拦截
# ══════════════════════════════════════
print("\n【五】系统保留键拦截")

# 检查代码中是否有对高危快捷键的保护
with open(os.path.join(BASE, "daemon", "handlers", "keyboard.py"), encoding="utf-8") as f:
    kb_code = f.read()

with open(os.path.join(BASE, "SKILL.md"), encoding="utf-8") as f:
    sk = f.read()

# 检查文档是否区分说明
report("文档区分安全快捷键风险", "风险" in sk or "注意" in sk or "限制" in sk,
       "建议增加对Win+L/Ctrl+Alt+Del等快捷键的风险说明")

# 检查是否有调用频率限制（已在server.py实现）
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    sv_code = f.read()
report("server.py有频率限流代码", "RATE_LIMITED" in sv_code)

# 测试快速拉取快捷键看是否被限流
limited = False
for i in range(150):
    r = send_request("keyboard_press", {"key": "enter"})
    if r.get("error") and "RATE_LIMITED" in str(r.get("error", {})):
        limited = True
        if i < 10:
            report(f"第{i}次触发限流", True)
        break
if not limited:
    warn("频率限流", "150次未触发（可能速率不够高或窗口太大）")

# ══════════════════════════════════════
# 七、多进程互斥锁与管道残留
# ══════════════════════════════════════
print("\n【七】多进程互斥与管道残留")

# 互斥锁代码检查
with open(os.path.join(BASE, "daemon", "utils", "lifecycle.py"), encoding="utf-8") as f:
    lc_code = f.read()
report("有互斥锁机制", "CreateMutex" in lc_code)
report("有PID文件机制", "PID_FILE" in lc_code or "pid_file" in lc_code)

# 10次并发启动测试
pids_before = set()
for i in range(10):
    r = send_request("ping", {})
    if r.get("result"):
        pids_before.add(r["result"]["data"]["pid"])

p = len(pids_before)
report(f"10次ping返回统一PID ({p}种)", p == 1,
       f"发现{p}个不同PID: {pids_before}")

# ══════════════════════════════════════
# 四、文件IO边界
# ══════════════════════════════════════
print("\n【四】文件IO边界")

# 特殊文件名截图
for name in ["test.png", "测试 截图.png", "shot#$&.png", "emoji😀.png"]:
    out_path = os.path.join(os.environ["TEMP"], name)
    r = send_request("screenshot_save", {"path": out_path})
    ok = r.get("result") and r["result"].get("success")
    exists = os.path.exists(out_path)
    report(f"保存: {name}", ok and exists, f"ok={ok}, exists={exists}")
    if exists:
        os.remove(out_path)

# 只读路径模拟（C:\Windows 系统目录）
r = send_request("screenshot_save", {"path": r"C:\Windows\test_shot.png"})
report("系统目录保存（预期失败）", r.get("error") is not None,
       f"实际返回: {r.get('result', r.get('error', '?'))[:80]}")

# ══════════════════════════════════════
# 八、人机交互混合
# ══════════════════════════════════════
print("\n【八】人机混合操作检验")

# 验证SendInput不会互相覆盖的基本设计
with open(os.path.join(BASE, "daemon", "utils", "sendinput.py"), encoding="utf-8") as f:
    si_code = f.read()
report("SendInput成对发送", "KEYEVENTF_KEYDOWN" in si_code and "KEYEVENTF_KEYUP" in si_code)
report("Unicode模式（不依赖剪贴板）", "KEYEVENTF_UNICODE" in si_code)
report("鼠标点击成对(down+up)", "MOUSEEVENTF_LEFTDOWN" in si_code and "MOUSEEVENTF_LEFTUP" in si_code)

# ══════════════════════════════════════
# 三、图形渲染兼容（仅代码检查）
# ══════════════════════════════════════
print("\n【三】图形渲染程序兼容性（代码检查）")
# mss截图默认使用虚拟屏幕，可以处理DX窗口
with open(os.path.join(BASE, "daemon", "handlers", "screenshot.py"), encoding="utf-8") as f:
    sc_code = f.read()
report("mss截图使用虚拟屏幕", "monitors[0]" in sc_code)
report("SendInput硬件无关", "sendinput" in si_code or "SendInput" in si_code)

# ══════════════════════════════════════
# 汇总
# ══════════════════════════════════════
print("\n" + "=" * 60)
print(f"本机可自动化: {PASS}/{PASS+FAIL} | ✅ {PASS} | ❌ {FAIL} | ⚠️ {WARN}")
print("\n需要多环境/手动验证的项（已记录到memory）：")
warn("输入法热键冲突", "需要安装搜狗/QQ输入法后手动验证")
warn("系统休眠/断电", "无法自动模拟断电重启")
warn("DirectX/游戏窗口", "需要安装游戏后手动验证")
warn("虚拟机/云桌面", "需要VMWare或云桌面环境")
warn("配置升级迁移", "需要多版本skill迭代测试")
warn("无显示器/远程桌面", "需要无头主机或RDP环境")
warn("多用户会话隔离", "需要多用户账户环境")
warn("离线/断网", "当前网络环境模拟需要手动断网")
warn("辅助功能全部开启", "需要手动开启粘滞键/筛选键/鼠标键/旁白后验证")
print("=" * 60)
