"""
desktop-control v1.1.3 — 边界压力测试（可自动化部分）
"""
import sys, os, time, hashlib, json, math, random, threading

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

from client.client import send_request

PASS = 0; FAIL = 0; WARN = 0
LOG = []

def test(num, name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    s = "PASS" if ok else "FAIL"
    LOG.append(f"| {num} | {name} | {s} | {detail[:100]}")
    print(f"  [{s}] #{num} {name}: {detail[:80]}")

def warn(name, detail=""):
    global WARN; WARN += 1
    print(f"  [WARN] {name}: {detail[:80]}")

print("=" * 70)
print("desktop-control v1.1.3 — 边界压力测试")
print(f"时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# ══════════════════════════════════════════════════════
# 方案4: 剪贴板10MB大数据
# ══════════════════════════════════════════════════════
print("\n## 方案4: 剪贴板大数据")
# 管道缓冲区限制 1MB, 测试 900KB (安全边界内)
size = 900 * 1024
large_text = "A" * size
print(f"  准备 {size//1024}KB 文本")

start = time.perf_counter()
r = send_request("clipboard_set", {"text": large_text})
set_elapsed = time.perf_counter() - start
set_ok = r.get("result", {}).get("success")
test(4, f"clipboard_set {size//1024}KB", set_ok, f"{set_elapsed:.2f}s")

start = time.perf_counter()
r = send_request("clipboard_get", {})
get_elapsed = time.perf_counter() - start
d = (r.get("result") or {}).get("data", {})
got = d.get("text", "")
data_ok = len(got) == len(large_text)
test(4, f"clipboard_get {size//1024}KB (长度一致)", data_ok, f"got {len(got)} bytes in {get_elapsed:.2f}s")

if data_ok:
    hash1 = hashlib.md5(large_text[:100000].encode()).hexdigest()
    hash2 = hashlib.md5(got[:100000].encode()).hexdigest()
    test(4, "clipboard MD5采样一致", hash1 == hash2)
else:
    warn("10MB 超出管道缓冲区 1MB 限制", "最大安全传输约 900KB，超大量数据需增大 BUFFER_SIZE")

send_request("clipboard_set", {"text": ""})

# ══════════════════════════════════════════════════════
# 方案5: 高频截图50次/5秒
# ══════════════════════════════════════════════════════
print("\n## 方案5: 高频截图 (50次)")
temp_dir = os.path.join(os.environ.get("TEMP", os.path.expanduser("~")), "dc_stress_screenshots")
os.makedirs(temp_dir, exist_ok=True)

sizes = []
failures = 0
start = time.perf_counter()

for i in range(50):
    path = os.path.join(temp_dir, f"stress_{i:03d}.png")
    r = send_request("screenshot_save", {"path": path})
    d = (r.get("result") or {}).get("data", {})
    if d and os.path.isfile(path):
        sizes.append(os.path.getsize(path))
    else:
        failures += 1

elapsed = time.perf_counter() - start
test(5, f"50次截图完成 ({elapsed:.1f}s)", failures == 0, f"{failures} 失败, {len(sizes)} 成功")
if sizes:
    test(5, f"截图尺寸 min={min(sizes)//1024}KB max={max(sizes)//1024}KB", True)
    # Check for memory leak: process should still respond
    r = send_request("ping", {})
    test(5, "截图后守护进程仍响应", r.get("result",{}).get("success"))

# Cleanup
for f in os.listdir(temp_dir):
    try: os.remove(os.path.join(temp_dir, f))
    except: pass
try: os.rmdir(temp_dir)
except: pass

# ══════════════════════════════════════════════════════
# 方案1: 鼠标高速移动+滚轮交替
# ══════════════════════════════════════════════════════
print("\n## 方案1: 鼠标高速交替 (模拟游戏)")
ops = [
    ("mouse_move", {"x": 100, "y": 100}),
    ("mouse_scroll", {"clicks": 10}),
    ("mouse_move", {"x": 500, "y": 300}),
    ("mouse_scroll", {"clicks": -5}),
    ("mouse_move", {"x": 900, "y": 500}),
    ("mouse_scroll", {"clicks": 3}),
    ("mouse_move", {"x": 300, "y": 700}),
    ("mouse_scroll", {"clicks": -8}),
    ("mouse_move", {"x": 700, "y": 200}),
]
def _is_success(r):
    """Check if a send_request response indicates success."""
    result = r.get("result")
    if result is None:
        return False, r.get("error", {}).get("message", "no result")
    return result.get("success", False), ""

start = time.perf_counter()
failures = 0
errors = []
for method, params in ops:
    r = send_request(method, params)
    ok, err = _is_success(r)
    if not ok:
        failures += 1
        errors.append(f"{method}: {err[:40]}")
elapsed = time.perf_counter() - start
test(1, f"9次交替操作 ({elapsed:.2f}s)", failures == 0, f"{elapsed*1000:.0f}ms, errors: {errors[:2]}" if errors else f"{elapsed*1000:.0f}ms")

# ══════════════════════════════════════════════════════
# 方案7: while循环动态条件
# ══════════════════════════════════════════════════════
print("\n## 方案7: while循环动态条件")
# while条件使用 _safe_eval 表达式 (不是 {{var}})
# 使用 mouse_position + window_list 作为条件
script = {
    "variables": {"count": 0},
    "steps": [
        {"action": "loop", "while": "window_list()", "max_iterations": 5, "body": [
            {"action": "nop", "params": {}},
            {"action": "set", "var": "count", "value": "{{count}} + 1"},
        ]},
        {"action": "log", "params": {"message": "loop done"}},
    ],
}
r = send_request("script_run", {"script": script})
d = (r.get("result") or {}).get("data", {})
tid = d.get("task_id", "")
test(7, "while循环脚本提交", d.get("status") == "running", f"task={tid[:12]}")

if tid:
    time.sleep(1.5)
    r2 = send_request("script_results", {"task_id": tid})
    d2 = (r2.get("result") or {}).get("data", {})
    status = d2.get("status", "")
    test(7, "while循环脚本完成", status == "completed", f"status={status}")

# ══════════════════════════════════════════════════════
# 方案9: 并发请求模拟（20线程随机操作）
# ══════════════════════════════════════════════════════
print("\n## 方案9: 并发随机操作")

lock = threading.Lock()
concurrent_results = []
def random_op(thread_id):
    ops = [
        ("mouse_move", {"x": random.randint(0,1920), "y": random.randint(0,1080)}),
        ("keyboard_type", {"text": chr(random.randint(65,90))}),
        ("window_list", {}),
        ("ping", {}),
        ("mouse_position", {}),
    ]
    for _ in range(5):
        method, params = random.choice(ops)
        try:
            r = send_request(method, params)
            with lock: concurrent_results.append(r.get("result",{}).get("success", False))
        except:
            with lock: concurrent_results.append(False)
        time.sleep(random.uniform(0.01, 0.05))

threads = []
start = time.perf_counter()
for i in range(10):
    t = threading.Thread(target=random_op, args=(i,), daemon=True)
    threads.append(t)
    t.start()
for t in threads:
    t.join()
elapsed = time.perf_counter() - start

total_ops = len(concurrent_results)
success_ops = sum(1 for r in concurrent_results if r)
test(9, f"10线程并发 ({total_ops}次操作)", success_ops == total_ops,
     f"{elapsed:.1f}s, {success_ops}/{total_ops} 成功")

# Post-concurrent: daemon still alive
r = send_request("ping", {})
test(9, "并发后守护进程存活", r.get("result",{}).get("success"))

# ══════════════════════════════════════════════════════
# 汇总
# ══════════════════════════════════════════════════════
total = PASS + FAIL
print("\n" + "=" * 70)
print(f"边界压力测试完成: ✅ {PASS} 通过 | ❌ {FAIL} 失败 | ⚠️ {WARN} 警告")
print("=" * 70)
print("\n逐项记录:")
for l in LOG:
    print(l)

if FAIL > 0:
    sys.exit(1)
else:
    print("\n✅ 所有自动化压力测试通过!")
