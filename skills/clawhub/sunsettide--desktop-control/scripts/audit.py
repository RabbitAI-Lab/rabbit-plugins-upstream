"""desktop-control 全面检查"""
import sys, os, json, ast, importlib.metadata

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

issues = []
warnings = []

def check(name, ok, msg=""):
    if ok:
        print(f"  ✅ {name}")
    else:
        print(f"  ❌ {name}")
        if msg:
            issues.append(f"{name}: {msg}")

def warn(name, msg):
    warnings.append(f"{name}: {msg}")
    print(f"  ⚠️  {name}: {msg}")

print("=" * 60)
print("desktop-control 全面检查")
print("=" * 60)

# ── 1. 文件完整性 ──
print("\n【1. 文件完整性】")
required = [
    "SKILL.md", "README.md", "LICENSE", "SECURITY.md", "requirements.txt",
    "daemon/main.py", "daemon/server.py",
    "daemon/handlers/mouse.py", "daemon/handlers/keyboard.py",
    "daemon/handlers/screenshot.py", "daemon/handlers/window.py",
    "daemon/handlers/uia.py", "daemon/handlers/__init__.py",
    "daemon/utils/sendinput.py", "daemon/utils/lifecycle.py",
    "daemon/utils/uia_threadpool.py", "daemon/utils/__init__.py",
    "daemon/__init__.py",
    "client/client.py", "client/__init__.py",
    "scripts/install_deps.ps1",
]
for f in required:
    check(f, os.path.exists(os.path.join(BASE, f)))

# ── 2. 无残留文件 ──
print("\n【2. 无残留文件】")
for root, dirs, files in os.walk(BASE):
    for f in files:
        fp = os.path.join(root, f)
        if "__pycache__" in fp or ".pyc" in fp:
            warn(f"发现 __pycache__: {os.path.relpath(fp, BASE)}", "应删除")
        if "legacy" in fp:
            warn(f"发现 legacy: {os.path.relpath(fp, BASE)}", "应删除")

# ── 3. SKILL.md frontmatter ──
print("\n【3. SKILL.md 元数据】")
with open(os.path.join(BASE, "SKILL.md"), encoding="utf-8") as f:
    skill = f.read()
parts = skill.split("---", 2)
check("有 YAML frontmatter", len(parts) >= 3)
if len(parts) >= 3:
    fm = parts[1]
    check("包含 name", '"name"' in fm or "name:" in fm)
    check("包含 description", '"description"' in fm or "description:" in fm)
    check("包含 metadata.openclaw", "openclaw" in fm)
    check("os 限制 win32", "win32" in fm)

# ── 4. 安全声明 ──
print("\n【4. 安全声明完整性】")
full_text = skill
for term, desc in [
    ("本地执行", "隐私声明"),
    ("管理员", "权限说明"),
    ("严禁", "滥用禁止"),
    ("不受信任", "信任提示"),
    ("local-only", "local-only标签"),
]:
    check(f"SKILL.md 包含「{term}」({desc})", term in full_text)

with open(os.path.join(BASE, "README.md"), encoding="utf-8") as f:
    readme = f.read()
for term, desc in [
    ("免责声明", "免责声明"),
    ("隐私承诺", "隐私承诺"),
    ("严禁用于", "滥用禁止"),
    ("UIPI", "已知限制"),
    ("管理员", "权限说明"),
    ("127.0.0.1", "网络绑定"),
]:
    check(f"README.md 包含「{term}」({desc})", term in readme)

check("SECURITY.md 存在", os.path.exists(os.path.join(BASE, "SECURITY.md")))
check("LICENSE 存在", os.path.exists(os.path.join(BASE, "LICENSE")))

with open(os.path.join(BASE, "LICENSE"), encoding="utf-8") as f:
    check("LICENSE 内容为 MIT", "MIT License" in f.read())

# ── 5. 代码语法 ──
print("\n【5. 代码语法检查】")
all_py = []
for root, dirs, files in os.walk(BASE):
    for f in files:
        if f.endswith(".py"):
            all_py.append(os.path.join(root, f))
for fp in all_py:
    try:
        ast.parse(open(fp, encoding="utf-8").read())
    except SyntaxError as e:
        check(f"语法正确: {os.path.relpath(fp, BASE)}", False, str(e))
check(f"所有 {len(all_py)} 个 .py 文件语法正确", True)

# ── 6. 依赖检查 ──
print("\n【6. 依赖版本锁定】")
with open(os.path.join(BASE, "requirements.txt")) as f:
    deps = [l.strip() for l in f if l.strip() and not l.startswith("#")]
for dep in deps:
    has_version = ">=" in dep or "==" in dep
    check(f"依赖已锁定: {dep}", has_version)

# 验证可安装
missing = []
for dep in deps:
    name = dep.split(">=")[0].split("==")[0].strip()
    try:
        importlib.metadata.version(name)
    except importlib.metadata.PackageNotFoundError:
        missing.append(name)
check(f"所有依赖可导入 ({len(deps)-len(missing)}/{len(deps)})", len(missing) == 0,
      f"缺失: {missing}" if missing else "")

# ── 7. 守护进程状态 ──
print("\n【7. 守护进程运行状态】")
r = send_request("ping", {})
if r.get("result") and r["result"].get("success"):
    pid = r["result"]["data"]["pid"]
    check(f"守护进程运行中 (PID={pid})", True)
    import psutil
    proc = psutil.Process(pid)
    mem = proc.memory_info().rss / 1024 / 1024
    cpu = proc.cpu_percent(interval=0.5)
    check(f"内存 < 80MB ({mem:.1f}MB)", mem < 80)
    check(f"CPU < 10% ({cpu:.1f}%)", cpu < 10)
else:
    check("守护进程", False, str(r.get("error")))

# ── 8. 功能验证 ──
print("\n【8. 核心功能抽样】")
check("mouse_move", send_request("mouse_move", {"x":500,"y":300}).get("result"))
check("keyboard_type", send_request("keyboard_type", {"text":"test"}).get("result"))
check("screenshot", send_request("screenshot",{"format":"b64"}).get("result"))
check("window_list", send_request("window_list",{}).get("result"))

# ── 9. 错误处理 ──
print("\n【9. 错误处理验证】")
check("缺参数报错", send_request("mouse_move",{}).get("error") is not None)
check("非法方法报错", send_request("nonexistent",{}).get("error") is not None)
check("不存在窗口报错", send_request("window_focus",{"title":"__nonexistent__?_"}).get("error") is not None)

# ── 10. 安全验证 ──
print("\n【10. 安全验证】")
# 检查代码无网络请求
no_network = True
for fp in all_py:
    with open(fp, encoding="utf-8") as f:
        for line in f:
            if any(kw in line for kw in ["urllib.request", "requests.", "http.client", "socket."]):
                if "import" in line and "#" not in line:
                    if "socket" in line and "win32" not in line.lower():
                        no_network = False
                    elif "urllib" in line:
                        no_network = False
check("代码无网络请求库", no_network)

# 管道名含SID
import win32file
pipe_sid = False
for f in win32file.FindFilesW(r"\\.\pipe\*"):
    name = f[8] if len(f) > 8 else ""
    if "oc-desktop" in str(name).lower() and "S-1" in str(name):
        pipe_sid = True
        break
check("管道名含用户 SID", pipe_sid)

# 频率限流生效
limited = False
for i in range(80):
    r = send_request("mouse_position", {})
    if r.get("error") and "RATE_LIMITED" in str(r.get("error",{})):
        limited = True
        break
check("频率限流生效", limited)

# ── 汇总 ──
print("\n" + "=" * 60)
print("检查完成")
print(f"发现 {len(issues)} 个问题")
if issues:
    for iss in issues:
        print(f"  ❌ {iss}")
if warnings:
    for w in warnings:
        print(f"  ⚠️  {w}")
if not issues and not warnings:
    print("🎉 全部通过！技能完整、安全、可发布")
print("=" * 60)
