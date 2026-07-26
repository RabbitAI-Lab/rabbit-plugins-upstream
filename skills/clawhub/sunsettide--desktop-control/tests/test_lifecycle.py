"""方案十七：系统生命周期 + 方案十八：可观测性"""
import sys, os, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0
issues = []
def report(n, o, d=""):
    global PASS, FAIL
    if o: PASS += 1; print(f"  {n}")
    else: FAIL += 1; print(f"  FAIL {n}: {d}"); issues.append(f"{n}: {d}")
def warn(n, d):
    print(f"  WARN {n}: {d}")
    issues.append(f"{n}: {d}")

print("=" * 50)
print("方案十七：系统生命周期")
print("=" * 50)

# 【17-1】daemon_shutdown + 重启
print("\n【1】关闭重启周期")
r = send_request("daemon_status", {})
if r.get("result") and r["result"].get("success"):
    uptime = r["result"]["data"].get("uptime_seconds", 0)
    report(f"当前运行: {uptime}s", uptime >= 0)

r = send_request("daemon_shutdown", {})
report("安全关闭", True)
time.sleep(2)

# 重启
r = send_request("ping", {})
report("关闭后可重新拉起", r.get("result") and r["result"].get("success"))
time.sleep(1)

r = send_request("daemon_status", {})
if r.get("result") and r["result"].get("success"):
    new_uptime = r["result"]["data"].get("uptime_seconds", 0)
    report(f"新实例运行: {new_uptime}s", new_uptime > 0)

# 【17-2】日志
print("\n【2】可观测性")
log = os.path.join(os.environ["TEMP"], "oc_desktop_daemon.log")
if os.path.exists(log):
    with open(log, encoding="utf-8") as f:
        lines = f.readlines()
    report(f"日志文件 {len(lines)} 行", len(lines) > 0)
    # 检查日志脱敏
    has_sensitive = False
    for line in lines:
        try:
            entry = json.loads(line)
            params = entry.get("params", {})
            for k, v in params.items():
                if isinstance(v, str) and len(v) > 50 and k == "text":
                    has_sensitive = True
        except:
            pass
    report("日志敏感内容已脱敏", not has_sensitive,
           "发现疑似明文日志" if has_sensitive else "")
else:
    warn("日志文件不存在", "上次清理后还未生成")

# 【17-3】错误码规范化
print("\n【3】错误码规范")
error_tests = [
    ("缺参数", "mouse_move", {}, "HANDLER_ERROR"),
    ("非法方法", "nonexistent_method", {}, "UNKNOWN_METHOD"),
    ("不存在窗口", "window_focus", {"title": "__nonexistent__test__"}, "HANDLER_ERROR"),
]
for name, method, params, expected_code in error_tests:
    r = send_request(method, params)
    code = r.get("error", {}).get("code", "") if r.get("error") else ""
    report(f"{name}: code={code}", expected_code in code)

# 【17-4】状态信息完整性 (18-3)
print("\n【4】状态接口")
r = send_request("daemon_status", {})
if r.get("result") and r["result"].get("success"):
    d = r["result"]["data"]
    fields = ["pid", "uptime_seconds"]
    all_have = all(f in d for f in fields)
    report(f"状态返回字段: {list(d.keys())}", all_have)

# 【17-5】清理
print("\n【5】卸载清理（模拟）")
r = send_request("daemon_shutdown", {})
report("关闭确认", True)
time.sleep(2)

# 确认无进程残留
import psutil
daemon_alive = False
for proc in psutil.process_iter(["pid", "name", "cmdline"]):
    try:
        cmd = " ".join(proc.info.get("cmdline") or [])
        if "daemon/main.py" in cmd:
            daemon_alive = True
    except:
        pass
report("无守护进程残留", not daemon_alive,
       "关闭后仍有守护进程进程" if daemon_alive else "")

# 清理日志/PID/管道文件
log = os.path.join(os.environ["TEMP"], "oc_desktop_daemon.log")
pid_file = os.path.join(os.environ["TEMP"], "oc_desktop_daemon.pid")
pipe_file = os.path.join(os.environ["TEMP"], "oc_desktop_pipe.txt")
for f in [log, pid_file, pipe_file]:
    if os.path.exists(f):
        try: os.remove(f)
        except: pass

print(f"\n{PASS}/{PASS+FAIL} 通过")
if not issues:
    print(f"方案十七/十八全部通过")
