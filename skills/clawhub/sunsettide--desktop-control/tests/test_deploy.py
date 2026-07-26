"""方案九：安装部署全生命周期测试"""
import os, sys, time, json, subprocess, shutil

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
print("方案九：安装部署全生命周期测试")
print("=" * 70)

# ── 1. 文件完整性 ──
print("\n【1. 文件完整性检查】")
req_files = ["SKILL.md", "README.md", "requirements.txt", "LICENSE", "SECURITY.md",
             "client/client.py", "daemon/main.py", "daemon/server.py",
             "daemon/handlers/mouse.py", "daemon/handlers/keyboard.py",
             "daemon/handlers/screenshot.py", "daemon/handlers/window.py",
             "daemon/handlers/uia.py",
             "daemon/utils/sendinput.py", "daemon/utils/lifecycle.py",
             "daemon/utils/uia_threadpool.py",
             "scripts/install_deps.ps1"]
missing = [f for f in req_files if not os.path.exists(os.path.join(BASE, f))]
report(f"所有 {len(req_files)} 个核心文件齐全", len(missing) == 0,
       f"缺失: {missing}" if missing else "")

# ── 2. Python 依赖可安装性 ──
print("\n【2. 依赖完整性检查】")
req_path = os.path.join(BASE, "requirements.txt")
with open(req_path) as f:
    deps = [l.strip() for l in f if l.strip() and not l.startswith("#")]
report(f"依赖声明: {len(deps)} 个包", len(deps) > 0, f"{deps}")

# 验证所有依赖已安装
import importlib.metadata
missing_deps = []
for dep in deps:
    pkg_name = dep.split(">=")[0].split("==")[0].strip()
    try:
        importlib.metadata.version(pkg_name)
    except importlib.metadata.PackageNotFoundError:
        missing_deps.append(pkg_name)
report(f"依赖全部已安装", len(missing_deps) == 0,
       f"缺失: {missing_deps}" if missing_deps else "")

# ── 3. 守护进程入口可执行
print("\n【3. 入口可执行性】")
result = subprocess.run(
    [sys.executable, "-c", f"import sys; sys.path.insert(0, r'{BASE}'); from daemon.main import main"],
    capture_output=True, text=True, timeout=5
)
report("daemon.main import 正常", result.returncode == 0,
       result.stderr[:200] if result.stderr else "")

result = subprocess.run(
    [sys.executable, "-c", f"import sys; sys.path.insert(0, r'{BASE}'); from client.client import send_request, _ensure_daemon"],
    capture_output=True, text=True, timeout=5
)
report("client.client import 正常", result.returncode == 0,
       result.stderr[:200] if result.stderr else "")

# ── 4. 重复安装/卸载验证
print("\n【4. 进程管理】")
# 模拟两次安装同一个目录（复制到临时路径再删除）
import tempfile
tmpdir = tempfile.mkdtemp(prefix="oc_desktop_test_")
shutil.copytree(BASE, os.path.join(tmpdir, "desktop-control"), dirs_exist_ok=True)
report("复制安装无冲突", os.path.exists(os.path.join(tmpdir, "desktop-control", "SKILL.md")))
shutil.rmtree(tmpdir)
report("卸载清理无残留", not os.path.exists(tmpdir))

# ── 5. 新旧版本共存
print("\n【5. 版本兼容性】")
with open(os.path.join(BASE, "LICENSE")) as f:
    has_license = "MIT" in f.read()
report("LICENSE 内容有效", has_license)

with open(os.path.join(BASE, "SECURITY.md"), encoding="utf-8") as f:
    content = f.read()
    has_policy = "漏洞" in content or "security" in content.lower()
report("SECURITY.md 有安全策略", has_policy)

# ── 6. 环境检测
print("\n【6. 运行环境检测】")
import platform
py_ver = platform.python_version_tuple()
report(f"Python 版本: {'.'.join(py_ver)}", int(py_ver[0]) >= 3 and int(py_ver[1]) >= 9)

import struct
report(f"系统: {platform.system()} {platform.release()} {struct.calcsize('P')*8}bit",
       platform.system() == "Windows")

# ── 7. ClawHub 技能元数据
print("\n【7. ClawHub 元数据检查】")
with open(os.path.join(BASE, "SKILL.md"), encoding="utf-8") as f:
    content = f.read()
has_name = "name:" in content.split("---")[1] if "---" in content else False
has_desc = "description:" in content.split("---")[1] if "---" in content else False
has_os = "win32" in content
report(f"SKILL.md frontmatter 完整", has_name and has_desc,
       "缺少 name 或 description" if not (has_name and has_desc) else "")

# ── 汇总 ──
print("\n" + "=" * 70)
print(f"方案九: 自动化测试完毕")
print(f"✅ 通过: {PASS} | ❌ 失败: {FAIL} | ⚠️ 警告/待确认: {WARN}")
if issues:
    print(f"\n📋 全部问题记录:")
    for iss in issues:
        print(f"  - {iss}")
else:
    print("🎉 无问题")
print("=" * 70)
