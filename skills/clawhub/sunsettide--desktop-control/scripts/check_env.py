"""
Comprehensive environment check for desktop-control skill.
"""
import sys, os, importlib, subprocess, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

PASS = 0; FAIL = 0; WARN = 0

def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; print(f"  [PASS] {name}")
    else: FAIL += 1; print(f"  [FAIL] {name}: {detail[:100]}")

def warn(name, detail=""):
    global WARN
    WARN += 1
    print(f"  [WARN] {name}: {detail[:100]}")

print("=" * 70)
print("desktop-control v1.1.3 — 深度环境检查")
print("=" * 70)

# ── 1. File Integrity ──
print("\n## 1. 文件完整性")

required_core = [
    "SKILL.md", "requirements.txt", "README.md", "SECURITY.md",
    "client/client.py",
    "daemon/main.py", "daemon/server.py",
    "daemon/handlers/__init__.py",
    "daemon/utils/sendinput.py", "daemon/utils/lifecycle.py", "daemon/utils/monitors.py",
    "daemon/utils/session.py", "daemon/utils/release_guard.py",
    "daemon/utils/human_engine.py", "daemon/utils/human_profile.py", "daemon/utils/humanize.py",
    "daemon/script_engine/engine.py",
    "daemon/script_gen/__init__.py", "daemon/script_gen/generator.py", "daemon/script_gen/llm_client.py",
    "daemon/script_gen/prompts.py", "daemon/script_gen/templates/registry.py",
    "daemon/tools/__init__.py", "daemon/tools/registry.py", "daemon/tools/executor.py",
    "daemon/tools/goal_run.py", "daemon/tools/screen_context.py",
]
handler_files = [
    "mouse.py", "keyboard.py", "screenshot.py", "window.py", "uia.py",
    "filedrop.py", "ocr.py", "window_aware.py", "hotkeys.py",
    "image_match.py", "macro.py",
    "session_handler.py", "script_handler.py", "script_gen_handler.py",
    "vision_click.py", "tools_handler.py",
]

for f in required_core:
    check(f"核心文件: {f}", os.path.isfile(f))

for f in handler_files:
    path = f"daemon/handlers/{f}"
    check(f"Handler: {f}", os.path.isfile(path))

# 31 test files
test_count = len([f for f in os.listdir("tests") if f.startswith("test_") and f.endswith(".py")])
check(f"测试文件: {test_count} 个", test_count >= 10, f"found {test_count}")

# SKILL.md YAML validity
with open("SKILL.md", encoding="utf-8") as f:
    skill_content = f.read()
has_yaml = skill_content.startswith("---")
check("SKILL.md YAML 前置元数据", has_yaml)
check("SKILL.md 有 {baseDir}", "{baseDir}" in skill_content)
check("SKILL.md 有 client.py 引用", "client/client.py" in skill_content)
check("SKILL.md 有方法表格", "| 鼠标" in skill_content)

# ── 2. Python Syntax ──
print("\n## 2. Python 语法")
python_files = []
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".py") and "site-packages" not in root and "__pycache__" not in root:
            python_files.append(os.path.join(root, f))

import ast
syntax_errors = 0
for pf in python_files:
    try:
        with open(pf, encoding="utf-8") as f:
            ast.parse(f.read())
    except SyntaxError as e:
        syntax_errors += 1
        print(f"  [SYNTAX ERROR] {pf}: {e}")
    except Exception as e:
        pass

check(f"Python 语法 ({len(python_files)} 个文件)", syntax_errors == 0, f"{syntax_errors} errors")

# ── 3. Python Dependencies ──
print("\n## 3. Python 依赖")
import subprocess
with open("requirements.txt") as f:
    reqs = [l.strip() for l in f if l.strip() and not l.startswith("#")]

installed = subprocess.run([sys.executable, "-m", "pip", "list", "--format=columns"], capture_output=True, text=True, timeout=10).stdout

for r in reqs:
    pkg_name = r.split(">")[0].split("<")[0].split("=")[0].split("#")[0].strip()
    installed_lower = installed.lower()
    if pkg_name.lower().replace("-", "_") in installed_lower:
        # pywin32 uses 'win32api' as module name, not 'pywin32'
        import_map = {"pywin32": "win32api", "opencv-python": "cv2"}
        import_name = import_map.get(pkg_name, pkg_name.replace("-", "_").split(".")[0])
        try:
            importlib.import_module(import_name)
            check(f"  {pkg_name}", True)
        except ImportError:
            warn(f"  {pkg_name} 导入警告", f"模块名 '{import_name}' 导入失败，pip 列表有但可能命名不同")
    else:
        check(f"  {pkg_name}", False, "MISSING" )

# Check optional deps
for pkg, import_name in [("pytesseract", "pytesseract"), ("opencv-python", "cv2"), ("pynput", "pynput")]:
    try:
        importlib.import_module(import_name)
        check(f"  (可选) {pkg}", True)
    except ImportError:
        warn(f"  (可选) {pkg} 未安装", "多数功能仍可用")

# ── 4. Tesseract ──
print("\n## 4. Tesseract OCR")
try:
    subprocess.run(["tesseract", "--version"], capture_output=True, timeout=5)
    check("Tesseract 二进制可用", True)
    langs = subprocess.run(["tesseract", "--list-langs"], capture_output=True, text=True, timeout=5)
    has_chi_sim = "chi_sim" in langs.stdout
    if has_chi_sim:
        check("Tesseract 中文语言包", True)
    else:
        warn("Tesseract 中文语言包缺失", "中文OCR不可用，英文OK")
except FileNotFoundError:
    # Check for TESSERACT_PATH
    tess_path = os.environ.get("TESSERACT_PATH", "")
    if tess_path and os.path.isfile(tess_path):
        check("Tesseract (TESSERACT_PATH)", True)
    else:
        check("Tesseract 二进制", False, "未安装或不在PATH")
except subprocess.TimeoutExpired:
    warn("Tesseract 检查超时", "可能路径问题")
except OSError as e:
    warn(f"Tesseract 检查错误: {e}")

# ── 5. Daemon Runtime ──
print("\n## 5. 守护进程运行时")
from client.client import send_request as sr
try:
    r = sr("ping", {})
    pong = r.get("result", {}).get("success") and r["result"]["data"].get("pong")
    pid = r["result"]["data"].get("pid", "?")
    check("守护进程运行中", pong, f"pid={pid}")

    # Check log dir
    log_dir = os.path.join(os.environ.get("LOCALAPPDATA", ""), "DesktopControl", "Logs")
    if os.path.isdir(log_dir):
        check("日志目录存在", True)
        log_files = [f for f in os.listdir(log_dir) if f.endswith(".log")]
        check(f"日志文件 ({len(log_files)}个)", len(log_files) > 0, str(log_files[:3]))
    else:
        warn("日志目录未创建", log_dir)

    # Test mouse move
    r = sr("mouse_move", {"x": 100, "y": 100})
    check("鼠标移动响应", r.get("result", {}).get("success", False))

    # Test keyboard
    r = sr("keyboard_type", {"text": "test"})
    check("键盘输入响应", r.get("result", {}).get("success", False))

    # Test window_list
    r = sr("window_list", {})
    windows = r.get("result", {}).get("data", {}).get("windows", [])
    check(f"窗口枚举响应 ({len(windows)} 个窗口)", r.get("result", {}).get("success", False))

    # Test tools_list
    r = sr("tools_list", {})
    tools = r.get("result", {}).get("data", {}).get("tools", [])
    check(f"工具列表 ({len(tools)} 个工具)", len(tools) >= 14, f"got {len(tools)}")

    # Test script engine
    r = sr("script_run", {"script": {"steps": [{"action": "nop", "params": {}}]}})
    d = (r.get("result") or {}).get("data", {})
    check("脚本引擎异步提交", d.get("status") == "running", f"got {d.get('status')}")

    # Test session
    r = sr("session_list", {})
    sessions = r.get("result", {}).get("data", {}).get("sessions", {})
    check(f"会话管理 ({len(sessions)} 个)", len(sessions) >= 1)

    # Test human engine
    from daemon.utils.human_engine import get_engine
    e = get_engine()
    lv = e.get_level("click", process_name="chrome.exe")
    check("拟人化引擎 (浏览器)", lv != "robotic", f"level={lv}")

except Exception as e:
    check("守护进程运行时检查", False, str(e)[:80])

# ── 6. OpenClaw Registration ──
print("\n## 6. OpenClaw 技能注册")
try:
    result = subprocess.run(["openclaw", "skills", "list", "--json"], capture_output=True, text=True, timeout=10)
    if "desktop-control" in result.stdout:
        check("OpenClaw 技能列表", True)
    else:
        check("OpenClaw 技能列表", False, "desktop-control 未出现在列表中")
except Exception as e:
    warn("OpenClaw 技能列表检查", str(e)[:60])

# ── SUMMARY ──
print("\n" + "=" * 70)
total = PASS + FAIL
print(f"结果: ✅ {PASS} 通过 | ❌ {FAIL} 失败 | ⚠️ {WARN} 警告")
if FAIL > 0:
    print("❌ 存在需要修复的失败项")
elif WARN > 0:
    print("⚠️ 全部通过但有警告（不影响核心功能）")
else:
    print("✅ 环境完美！")
print("=" * 70)
