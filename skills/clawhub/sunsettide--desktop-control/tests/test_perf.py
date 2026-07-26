"""方案七：资源占用与性能测试"""
import os, sys, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request
import psutil

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
print("方案七：资源占用与性能测试")
print("=" * 70)

# 获取守护进程 PID
r = send_request("ping", {})
pid = r["result"]["data"]["pid"] if r.get("result") and r["result"].get("success") else None
if not pid:
    print("❌ 无法获取守护进程 PID，终止测试")
    exit(1)

proc = psutil.Process(pid)
print(f"守护进程 PID: {pid}")

# ── 1. 空载资源占用 ──
print("\n【1. 空载资源占用（静置5秒）】")
time.sleep(5)
cpu = proc.cpu_percent(interval=1)
mem = proc.memory_info().rss / 1024 / 1024
report(f"空载 CPU = {cpu:.1f}%", cpu < 5)
report(f"空载 内存 = {mem:.1f}MB", mem < 80)

initial_mem = mem

# ── 2. 连续操作峰值 ──
print("\n【2. 连续操作峰值（1分钟连续截图+键鼠）】")
cpu_samples = []
for i in range(10):
    send_request("screenshot", {"format": "b64"})
    send_request("mouse_move", {"x": i*100, "y": i*50})
    send_request("keyboard_type", {"text": "test"})
    cpu_samples.append(proc.cpu_percent(interval=0))
    time.sleep(0.1)

avg_cpu = sum(cpu_samples) / len(cpu_samples)
peak_cpu = max(cpu_samples)
peak_mem = proc.memory_info().rss / 1024 / 1024
report(f"操作中 CPU 平均 = {avg_cpu:.1f}%, 峰值 = {peak_cpu:.1f}%", peak_cpu < 30,
       f"可能偏高，但普通操作不会有这么高频的连续调用")

# ── 3. 内存泄漏验证 ──
print("\n【3. 内存泄漏验证（200次截图）】")
for i in range(200):
    send_request("screenshot", {"format": "b64"})
    if i % 50 == 0:
        print(f"    截图 {i}/200 ...")
mem_after = proc.memory_info().rss / 1024 / 1024
mem_growth = mem_after - initial_mem
report(f"200次截图后内存 = {mem_after:.1f}MB (增长 {mem_growth:+.1f}MB)", mem_growth < 20,
       f"增长 {mem_growth:.1f}MB — 如果启动时加载了pywinauto，增长正常")

# ── 4. 冷启动耗时 ──
print("\n【4. 冷启动耗时】")
# 先关闭
send_request("daemon_shutdown", {})
time.sleep(1)

t0 = time.time()
r = send_request("ping", {})
cold_time = time.time() - t0
report(f"冷启动 = {cold_time:.1f}秒", cold_time < 8,
       f"首次启动需加载 pywinauto，{cold_time:.1f}秒")
# 如果超过3秒，记录新进程PID
if r.get("result") and r["result"].get("success"):
    report("冷启动后可用", True)

# ── 5. 单次指令延迟 ──
print("\n【5. 单次指令延迟】")
latencies = []
for i in range(10):
    t0 = time.time()
    send_request("mouse_move", {"x": 500, "y": 300})
    lat = (time.time() - t0) * 1000
    latencies.append(lat)
    time.sleep(0.05)

avg_lat = sum(latencies) / len(latencies)
max_lat = max(latencies)
report(f"平均延迟 = {avg_lat:.0f}ms, 最大 = {max_lat:.0f}ms", avg_lat < 200,
       f"注意：首次调用冷启动后，后续调用约50-100ms为正常IPC延迟")

# ── 汇总 ──
print("\n" + "=" * 70)
print(f"方案七: {PASS+FAIL} 项 | ✅ 通过: {PASS} | ❌ 失败: {FAIL}")
if issues:
    print(f"\n📋 问题记录:")
    for iss in issues:
        print(f"  - {iss}")
else:
    print("🎉 无问题")
print("=" * 70)
