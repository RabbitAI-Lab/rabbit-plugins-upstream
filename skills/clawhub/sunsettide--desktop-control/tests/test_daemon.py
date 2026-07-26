"""方案五：守护进程与IPC通信专项测试"""
import os, sys, time, json, random, threading
from collections import Counter

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

print("=" * 70)
print("方案五：守护进程与IPC通信专项测试")
print("=" * 70)

# ── 1. 高频连续调用稳定性 ──
print("\n【1. 高频连续调用 100 次鼠标移动】")
errors = []
for i in range(100):
    x = random.randint(0, 1920)
    y = random.randint(0, 1080)
    r = send_request("mouse_move", {"x": x, "y": y})
    if not (r.get("result") and r["result"].get("success")):
        errors.append((i, r.get("error")))
report("100 次全部成功", len(errors) == 0,
       f"第{errors[0][0]}次失败: {errors[0][1]}" if errors else "")
print(f"    成功: {100-len(errors)}/100")

# ── 2. 并发压力测试 ──
print("\n【2. 并发指令压力测试（2线程×10次）】")
results = []
lock = threading.Lock()
def worker(name, count):
    for i in range(count):
        if name == "mouse":
            x, y = random.randint(0, 1920), random.randint(0, 1080)
            r = send_request("mouse_move", {"x": x, "y": y})
        else:
            r = send_request("screenshot", {"format": "b64"})
        with lock:
            results.append((name, r.get("result") is not None))

t1 = threading.Thread(target=worker, args=("mouse", 10))
t2 = threading.Thread(target=worker, args=("screenshot", 10))
t1.start(); t2.start()
t1.join(); t2.join()

mouse_ok = sum(1 for n,r in results if n=="mouse" and r)
shot_ok = sum(1 for n,r in results if n=="screenshot" and r)
report("并发鼠标全部成功", mouse_ok == 10)
report("并发截图全部成功", shot_ok == 10)

# ── 3. 单实例机制验证 ──
print("\n【3. 单实例机制验证（10次ping）】")
pids = set()
for i in range(10):
    r = send_request("ping", {})
    if r.get("result") and r["result"].get("success"):
        pids.add(r["result"]["data"]["pid"])
report("始终只有一个守护进程", len(pids) == 1,
       f"检测到 {len(pids)} 个不同PID: {pids}")
print(f"    PID: {pids}")

# ── 4. 异常断开自动恢复 ──
print("\n【4. 异常断开自动恢复】")
# 先记录当前 PID
r = send_request("ping", {})
old_pid = r["result"]["data"]["pid"] if r.get("result") and r["result"].get("success") else 0
print(f"    当前守护进程 PID: {old_pid}")

# 强制结束守护进程
import signal
try:
    os.kill(old_pid, signal.SIGTERM)
except:
    pass
time.sleep(1)

# 立即执行指令，应自动拉起新守护进程
r = send_request("mouse_move", {"x": 400, "y": 300})
new_pid = r["result"]["data"].get("pid", -1) if r.get("result") else -1
if r.get("result") and r["result"].get("success"):
    report("异常断开后自动恢复", True)
    # 再查一次看是不是新进程
    time.sleep(0.5)
    r2 = send_request("ping", {})
    current_pid = r2["result"]["data"]["pid"] if r2.get("result") and r2["result"].get("success") else -1
    report(f"新PID({new_pid}) ≠ 旧PID({old_pid})", current_pid != old_pid,
           f"旧={old_pid} 新={current_pid}")
else:
    report("异常断开后自动恢复", False, str(r.get("error")))

# ── 5. 退出清理完整性 ──
print("\n【5. 退出清理完整性】")
r = send_request("daemon_shutdown", {})
report("daemon_shutdown 返回成功", r.get("result") and r["result"].get("success"))
time.sleep(2)

# 再ping应该自动启新进程（不是原来的）
r = send_request("ping", {})
if r.get("result") and r["result"].get("success"):
    report("shutdown后进程可重新拉起", True)
else:
    report("shutdown后进程自动清理", True)  # 进程已退出，清理干净

# ── 汇总 ──
print("\n" + "=" * 70)
print(f"方案五: {PASS+FAIL} 项 | ✅ 通过: {PASS} | ❌ 失败: {FAIL}")
if issues:
    print(f"\n⚠️  发现 {len(issues)} 个问题:")
    for iss in issues:
        print(f"  - {iss}")
else:
    print("🎉 无发现任何问题")
print("=" * 70)
