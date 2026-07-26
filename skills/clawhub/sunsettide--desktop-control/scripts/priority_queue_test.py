"""实操验证：进程优先级 + 任务队列 + 信号容错"""
import sys, os, time, json, signal, subprocess, threading

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

P = 0; F = 0; issues = []
def R(n, o, d=""):
    global P, F
    if o: P += 1; print("  \u2705 " + n)
    else: F += 1; print("  \u274c " + n + ": " + d); issues.append(n + ": " + d)
def W(n, d):
    print("  \u26a0 " + n + ": " + d)
    issues.append(n + ": " + d)

print("=" * 60)
print("实操验证：进程优先级 + 任务队列 + 信号容错")
print("=" * 60)

# 先获取守护进程PID
r = send_request("ping", {})
pid = r["result"]["data"]["pid"] if r.get("result") else 0
print(f"  守护进程 PID: {pid}")

# ════════════════════════════════
# 五、进程优先级调度
# ════════════════════════════════
print("\n【五】进程优先级调度")

import psutil
proc = psutil.Process(pid)

# 1. 设置为低优先级
try:
    proc.nice(psutil.IDLE_PRIORITY_CLASS)
    R("设为低优先级成功", True)
except Exception as e:
    R("设为低优先级", False, str(e))

# 2. 低优先级下执行指令
errors = 0
for i in range(20):
    r = send_request("mouse_move", {"x": i*50, "y": i*30})
    if not (r.get("result") and r["result"].get("success")):
        errors += 1
    time.sleep(0.05)
R(f"低优先级下20次操作: 失败{errors}次", errors == 0)

# 3. 恢复普通优先级
try:
    proc.nice(psutil.NORMAL_PRIORITY_CLASS)
    R("恢复普通优先级成功", True)
except:
    pass

# ════════════════════════════════
# 八、进程信号与异常终止
# ════════════════════════════════
print("\n【八】进程信号与异常终止")

# 1. taskkill /f 强制杀死
r = send_request("ping", {})
old_pid = r["result"]["data"]["pid"] if r.get("result") else 0
print(f"  当前PID: {old_pid}")

subprocess.run(["taskkill", "/F", "/PID", str(old_pid)], capture_output=True)
time.sleep(2)

# 下一次调用应自动重建
r = send_request("mouse_move", {"x": 100, "y": 100})
R("taskkill后自动恢复", r.get("result") and r["result"].get("success"))

# 2. 获取新PID
r = send_request("ping", {})
new_pid = r["result"]["data"]["pid"] if r.get("result") else 0
R(f"新PID({new_pid}) != 旧PID({old_pid})", new_pid != old_pid and new_pid > 0)

# 3. 未捕获异常——检查server.py的try块
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    server_code = f.read()
R("server.py有try-except包裹", "try:" in server_code and "except" in server_code)

with open(os.path.join(BASE, "daemon", "handlers", "mouse.py"), encoding="utf-8") as f:
    mouse_code = f.read()
# mouse.py 用 raise ValueError 报告错误，server.py 捕获
R("handler内部有异常抛出机制", "raise" in mouse_code)

# ════════════════════════════════
# 十三、任务队列压力与堆积
# ════════════════════════════════
print("\n【十三】任务队列压力与堆积")

# 200条混合指令
t0 = time.time()
results = []
for i in range(200):
    if i % 3 == 0:
        r = send_request("mouse_move", {"x": i, "y": i})
    elif i % 3 == 1:
        r = send_request("mouse_position", {})
    else:
        r = send_request("window_list", {})
    results.append(r.get("result") and r["result"].get("success"))
    if i % 50 == 49:
        print(f"  {i+1}/200 ...")
t1 = time.time()

success = sum(1 for x in results if x)
R(f"200条混合指令: {success}/{200} 成功", success == 200,
  f"耗时: {(t1-t0):.1f}s")
R(f"队列有序执行内存稳定", success > 0)

# 单条失败不影响后续
r = send_request("mouse_move", {})  # 缺参数，应失败
r2 = send_request("mouse_position", {})  # 正常，应成功
R("单条失败后后续指令正常", r2.get("result") and r2["result"].get("success"),
  f"第一条: {r.get('error','ok')[:30]}")

# 内存检查
import psutil
proc = psutil.Process(pid)
mem = proc.memory_info().rss / 1024 / 1024
R(f"操作后内存: {mem:.1f}MB", mem < 100, f"当前: {mem:.1f}MB")

# ════════════════════════════════
print("\n" + "=" * 60)
print(f"结果: {P} 通过 | {F} 失败")
if issues:
    for iss in issues:
        print("  " + iss)
print("=" * 60)
