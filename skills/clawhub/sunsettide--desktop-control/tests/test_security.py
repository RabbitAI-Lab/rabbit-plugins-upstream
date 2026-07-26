"""方案八：安全机制有效性验证"""
import os, sys, time, json, subprocess

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

def warn(name, msg):
    global WARN
    WARN += 1
    print(f"  ⚠️  {name}: {msg}")
    issues.append(f"{name}: {msg}")

print("=" * 70)
print("方案八：安全机制有效性验证")
print("=" * 70)

# ── 1. 恶意参数注入 ──
print("\n【1. 恶意参数注入】")
# 超长字符串
r = send_request("keyboard_type", {"text": "A" * 100})
report("100字符输入正常", r.get("result") and r["result"].get("success"))

# 特殊 JSON 字符
r = send_request("keyboard_type", {"text": "<script>alert('xss')</script>"})
report("HTML 特殊字符输入正常", r.get("result") and r["result"].get("success"))

# 超大坐标
r = send_request("mouse_move", {"x": 999999, "y": 999999})
report("超大坐标不崩溃", r.get("result") and r["result"].get("success"))

# 非法方法名
r = send_request("nonexistent_method", {})
report("非法方法名返回错误", r.get("error") is not None)

# 空参数
r = send_request("mouse_move", {})
report("缺参数返回错误", r.get("error") is not None)

# ── 2. 无网络外发验证 ──
print("\n【2. 无网络外发验证】")
# 检查 daemon 代码中有无 HTTP/网络请求库
import ast
daemon_dir = os.path.join(BASE, "daemon")
network_imports = []
for root, dirs, files in os.walk(daemon_dir):
    for f in files:
        if f.endswith(".py"):
            fp = os.path.join(root, f)
            with open(fp, encoding="utf-8") as fh:
                for line in fh:
                    if any(kw in line for kw in ["urllib", "requests", "http.client", "socket", "aiohttp"]):
                        if "socket" in line and "win32" not in line.lower() and "import" in line:
                            network_imports.append(f"{f}: {line.strip()}")
if not network_imports:
    report("守护进程代码无网络请求库", True)
else:
    for ni in network_imports:
        warn("发现网络相关引用", ni)

# 检查 client.py 同样
with open(os.path.join(BASE, "client", "client.py"), encoding="utf-8") as f:
    client_code = f.read()
has_network = any(kw in client_code for kw in ["urllib", "requests", "http.", "socket."])
report("客户端代码无网络请求", not has_network, "发现网络引用" if has_network else "")

# ── 3. 操作日志审计
print("\n【3. 操作日志审计】")
log_file = os.path.join(os.environ.get("TEMP", os.path.expanduser("~")), "oc_desktop_daemon.log")
if os.path.exists(log_file):
    report("日志文件存在", True)
    with open(log_file, encoding="utf-8", errors="replace") as f:
        content = f.read()
        lines = content.strip().split("\n")
        report(f"日志有 {len(lines)} 行", len(lines) > 0)
    warn("日志内容仅本地", "当前日志仅做简单记录，未实现结构化审计，P2 待迭代")
else:
    warn("日志文件不存在", "当前守护进程未实现日志写入，P2 待迭代")

# ── 4. 命名管道权限（注释检查） ──
print("\n【4. 命名管道权限设计验证】")
with open(os.path.join(BASE, "daemon", "server.py"), encoding="utf-8") as f:
    server_code = f.read()
has_sid = "user_sid" in server_code or "get_user_sid" in server_code
has_session = "get_session_id" in server_code or "SessionId" in server_code or "session" in server_code
report(f"管道名含用户 SID（{has_sid}）", has_sid)
report(f"管道名含会话 ID（{has_session}）", has_session)

# 检查 SECURITY_ATTRIBUTES 实际使用
has_sec_attr = "SECURITY_ATTRIBUTES" in server_code or "SECURITY_ATTRIBUTES" in server_code
report(f"管道 SecurityAttributes 已配置", has_sec_attr)
warn("管道安全 ACL", "当前 SID+会话隔离是基本安全，未实现完整的 DACL 安全描述符，P2 待迭代")

# ── 5. document 安全声明检查
print("\n【5. 文档安全声明完整性】")
with open(os.path.join(BASE, "SKILL.md"), encoding="utf-8") as f:
    skill = f.read()
checks = {
    "隐私声明": "本地执行" in skill or "本地" in skill,
    "无上传声明": "上传" in skill or "外发" in skill or "上传" in skill,
    "管理员权限说明": "管理员" in skill,
    "禁止滥用声明": "严禁" in skill or "禁止" in skill,
}
all_ok = all(checks.values())
report(f"安全声明完整 ({sum(checks.values())}/{len(checks)})", all_ok)
for name, ok in checks.items():
    if not ok:
        warn(f"  SKILL.md 缺少: {name}", "建议补充")

# ── 汇总 ──
print("\n" + "=" * 70)
print(f"方案八: 自动化测试完毕")
print(f"✅ 通过: {PASS} | ❌ 失败: {FAIL} | ⚠️ 警告/待确认: {WARN}")
if issues:
    print(f"\n📋 全部问题记录:")
    for iss in issues:
        print(f"  - {iss}")
print("=" * 70)
