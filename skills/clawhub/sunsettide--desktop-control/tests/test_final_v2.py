"""9大类补充：本机最终验证（独立文件避免PS转义问题）"""
import sys, os, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

P = 0; F = 0; W = 0
def R(n, o, d=""):
    global P, F
    if o: P += 1; print("  " + chr(0x2705) + " " + n)
    else: F += 1; print("  " + chr(0x274C) + " " + n + ": " + d)
def Wn(n, d):
    global W; W += 1
    print("  " + chr(0x26A0) + chr(0xFE0F) + " " + n + ": " + d)

print("=" * 50)
print("9大类补充：本机最终验证")
print("=" * 50)

# 五、系统保留键
print("\n[五] 系统保留键")
with open(os.path.join(BASE, "daemon", "handlers", "keyboard.py"), encoding="utf-8") as f: kb = f.read()
with open(os.path.join(BASE, "SKILL.md"), encoding="utf-8") as f: sk = f.read()
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f: sv = f.read()
R("文档含快捷键风险提示", "风险" in sk or "注意" in sk)
R("限流代码存在", "RATE_LIMITED" in sv)

# 四、文件IO
print("\n[四] 文件IO边界")
for name, out in [
    ("桌面截图", os.path.join(os.path.expanduser("~"), "Desktop", "oc_test_shot.png")),
    ("TEMP目录", os.path.join(os.environ["TEMP"], "oc_test_shot.png")),
]:
    r = send_request("screenshot_save", {"path": out})
    ok = r.get("result") and r["result"].get("success")
    R(name, ok, str(r.get("error")))
    if ok and os.path.exists(out):
        os.remove(out)

# 系统目录写入（预期失败）
r = send_request("screenshot_save", {"path": "C:\\Windows\\oc_test_shot.png"})
R("系统目录禁止写入", r.get("error") is not None, str(r.get("error")))

# 七、互斥锁
print("\n[七] 互斥锁")
with open(os.path.join(BASE, "daemon", "utils", "lifecycle.py"), encoding="utf-8") as f:
    lc = f.read()
R("CreateMutex存在", "CreateMutex" in lc)
R("PID_FILE存在", "PID_FILE" in lc)
R("write_pid_file存在", "write_pid_file" in lc)

pids = set()
for i in range(5):
    r = send_request("ping", {})
    if r.get("result"):
        pids.add(r["result"]["data"]["pid"])
R("多次ping同一PID", len(pids) <= 1, str(pids))

# 八、人机混合
print("\n[八] 人机混合设计验证")
with open(os.path.join(BASE, "daemon", "utils", "sendinput.py"), encoding="utf-8") as f:
    si = f.read()
R("SendInput成对: KEYDOWN+KEYUP", "KEYEVENTF_KEYDOWN" in si and "KEYEVENTF_KEYUP" in si)
R("Unicode模式", "KEYEVENTF_UNICODE" in si)
R("Mouse down+up成对", "MOUSEEVENTF_LEFTDOWN" in si and "MOUSEEVENTF_LEFTUP" in si)

# 功能完好性
r = send_request("mouse_move", {"x": 500, "y": 300})
R("最终功能正常", r.get("result") and r["result"].get("success"))

print("\n=== 结果 ===")
print(f"{P} 通过 | {F} 失败 | {W} 需手动")

print("\n=== 需手动/多环境验证的项 ===")
manual = [
    "输入法热键冲突：需要搜狗/QQ输入法+微信/钉钉热键环境",
    "休眠/断电重启：无法自动模拟",
    "图形渲染/DirectX：需要游戏/3D软件环境",
    "虚拟机/云桌面：需要VMWare/华为云桌面",
    "配置升级迁移：需要多版本skill迭代",
    "无显示器/无头主机：需要无外接屏幕环境",
    "辅助功能全开：需手动开启粘滞键/筛选键/鼠标键/旁白",
    "RDP远程桌面：需要mstsc远程连接测试",
    "多用户会话隔离：需要多Windows账户切换测试",
    "离线/断网验证：需断开网络后确认零外发",
    "电源模式：需切换节能/高性能模式验证CPU/内存",
    "文件磁盘满：无法自动化模拟",
    "24小时高负载调度：需长时间运行验证",
    "多版本Gateway兼容：需要安装不同版本OpenClaw",
    "多语言系统编码：需要EN/JA/KO系统环境",
]
for m in manual:
    print(f"  - {m}")
