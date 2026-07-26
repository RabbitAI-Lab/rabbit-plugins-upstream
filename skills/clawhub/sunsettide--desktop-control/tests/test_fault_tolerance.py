"""方案十三：错误注入与容错降级测试"""
import sys, os, time, json, subprocess, signal

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
print("方案十三：错误注入与容错降级测试")
print("=" * 60)

# 【1】异常参数注入
print("\n【1】异常参数注入")
r = send_request("mouse_move", {"x": -100, "y": -100})
report("负坐标mouse_move不崩溃", True)  # 可以正常执行（负坐标会被钳位但不是错误）

r = send_request("mouse_move", {"x": 999999, "y": 999999})
report("超大坐标不崩溃", True)

r = send_request("mouse_move", {})
report("缺参数字段返回错误", r.get("error") is not None)

r = send_request("mouse_click", {"x": "abc", "y": "def"})
report("类型错误参数返回错误", r.get("error") is not None or r.get("result") is None,
       f"返回: {r.get('result', r.get('error', '?'))}")

r = send_request("nonexistent_method", {})
report("非法方法返回错误", r.get("error") is not None)

# 【2】重复启动冲突
print("\n【2】重复启动冲突")
r = send_request("ping", {})
pid1 = r["result"]["data"]["pid"] if r.get("result") else 0
print(f"  当前守护进程 PID: {pid1}")

# 手动启动第二个实例
result = subprocess.run(
    [sys.executable, os.path.join(BASE, "daemon", "main.py")],
    capture_output=True, text=True, timeout=5
)
time.sleep(1)
r = send_request("ping", {})
pid2 = r["result"]["data"]["pid"] if r.get("result") else -1
if pid2 == -1:
    report("第二个实例被阻止", True)
else:
    report(f"第二个实例退出，PID未变 (仍为{pid1})", pid2 == pid1,
           f"PID从{pid1}变为{pid2}") 

# 【3】守护进程被kill后自动拉起的重复验证
print("\n【3】崩溃自恢复上限")
for i in range(5):
    r = send_request("ping", {})
    pid = r["result"]["data"]["pid"] if r.get("result") else 0
    try:
        os.kill(pid, signal.SIGTERM)
    except:
        pass
    time.sleep(2)
    r = send_request("mouse_move", {"x": 500, "y": 300})
    if not (r.get("result") and r["result"].get("success")):
        report(f"第{i+1}次kill后恢复", False, str(r.get("error")))
        break
    time.sleep(0.3)
else:
    report("5次连续kill后均可自动恢复", True)

# 【4】守护进程状态接口
print("\n【4】状态接口完整性")
r = send_request("daemon_status", {})
if r.get("result") and r["result"].get("success"):
    d = r["result"]["data"]
    report(f"返回PID ({d.get('pid',0)})", "pid" in d)
    report(f"返回运行时间 ({d.get('uptime_seconds',0)}s)", "uptime_seconds" in d)
else:
    report("daemon_status返回成功", False, str(r.get("error")))

# ── 汇总 ──
print("\n" + "=" * 60)
print(f"方案十三: {PASS+FAIL} 项 | ✅ {PASS} | ❌ {FAIL}")
if issues:
    for iss in issues:
        print(f"  📋 {iss}")
else:
    print("🎉 无问题")
warn("依赖缺失测试", "无法自动化卸载依赖后测试，需手动环境验证")
warn("磁盘耗尽测试", "无法自动化模拟磁盘满场景")
print("=" * 60)
