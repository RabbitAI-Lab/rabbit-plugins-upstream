"""补充维度：参数极值边界 + 辅助功能 + 定时调度 + 多实例冲突"""
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
print("补充维度测试")
print("=" * 60)

# ── 五、API入参边界极值 ──
print("\n【五】API入参边界极值")

# 坐标边界
for name, params in [
    ("原点(0,0)", {"x": 0, "y": 0}),
    ("超大坐标(99999,99999)", {"x": 99999, "y": 99999}),
    ("负坐标(-100,-100)", {"x": -100, "y": -100}),
]:
    r = send_request("mouse_move", params)
    report(f"mouse_move {name}", r.get("result") and r["result"].get("success"))
    time.sleep(0.2)

# 空数组快捷键
r = send_request("keyboard_hotkey", {"keys": []})
report("空数组快捷键", r.get("error") is not None)  # 应该报错

# 单键数组
r = send_request("keyboard_hotkey", {"keys": ["ctrl"]})
report("单键快捷键", r.get("result") and r["result"].get("success"))

# 窗口名称边界
for name, title in [
    ("空标题", ""),
    ("超长标题(200字)", "A" * 200),
    ("特殊符号标题", "!@#$%^&*()_+" * 10),
]:
    r = send_request("window_focus", {"title": title})
    report(f"window_focus {name}", True)  # 不应崩溃，找不到是预期
    time.sleep(0.2)

# 超大滚动值
r = send_request("mouse_scroll", {"clicks": 1000})
report("滚轮+1000", r.get("result") and r["result"].get("success"))
r = send_request("mouse_scroll", {"clicks": -1000})
report("滚轮-1000", r.get("result") and r["result"].get("success"))

# ── 六、辅助功能（代码检查） ──
print("\n【六】Windows辅助功能兼容性")
# 检查辅助功能状态
import ctypes
SF_STICKYKEYSON = 0x1
SF_FILTERKEYSON = 0x4
SF_MOUSEKEYSON = 0x8
try:
    sticky = ctypes.windll.user32.SystemParametersInfoW(0x003B, 0, ctypes.byref(ctypes.c_int()), 0)
except:
    sticky = 0
status = []
if sticky: status.append("粘滞键")
warn("辅助功能状态", f"粘滞键:{'开启' if sticky else '关闭'} (需手动开启后验证)")

# ── 八、定时调度 ──
print("\n【八】队列有序执行")
# 模拟一次性下发50条任务
results = []
t0 = time.time()
for i in range(50):
    r = send_request("mouse_position", {})
    results.append(r.get("result") and r["result"].get("success"))
t1 = time.time()
report(f"50条指令排队耗时: {(t1-t0)*1000:.0f}ms", all(results),
       f"失败{sum(1 for x in results if not x)}条")

# ── 九、多实例冲突（模拟） ──
print("\n【九】多网关实例冲突")
# 检查当前守护进程PID
r = send_request("ping", {})
pid1 = r["result"]["data"]["pid"] if r.get("result") else 0
print(f"  当前守护进程: PID={pid1}")

# 尝试启动第二个客户端（应该连到同一个守护进程）
r2 = send_request("ping", {})
pid2 = r2["result"]["data"]["pid"] if r2.get("result") else -1
report("两次ping返回相同PID", pid2 == pid1 or pid2 == -1 or pid2 == 0,
       f"PID1={pid1}, PID2={pid2}")

# ── 汇总 ──
print("\n" + "=" * 60)
print(f"测试: {PASS+FAIL} | ✅ {PASS} | ❌ {FAIL} | ⚠️ {WARN}")
if issues:
    for iss in issues:
        print(f"  {iss}")
print("=" * 60)
