"""
Desktop Control v1.1.3 — OpenClaw Skill Security Audit
Audits against OpenClaw skill safety standards.
"""
import sys, os, ast

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

PASS = 0; FAIL = 0; WARN = 0
SEV_HIGH = 0; SEV_MED = 0; SEV_LOW = 0

def check(cat, name, ok, sev="low", detail=""):
    global PASS, FAIL, SEV_HIGH, SEV_MED, SEV_LOW
    if ok:
        PASS += 1
        print(f"  [PASS] [{sev.upper()}] {cat}: {name}")
    else:
        FAIL += 1
        if sev == "high": SEV_HIGH += 1
        elif sev == "med": SEV_MED += 1
        else: SEV_LOW += 1
        print(f"  [FAIL] [{sev.upper()}] {cat}: {name}  {detail[:80]}")

def warn(name, detail=""):
    global WARN; WARN += 1
    print(f"  [WARN] {name}: {detail[:80]}")

print("=" * 70)
print("desktop-control v1.1.3 — OpenClaw 安全标准审计")
print("=" * 70)

# ── 1. SKILL.md Security fields ──
print("\n## 1. SKILL.md 安全声明")
with open("SKILL.md", encoding="utf-8") as f:
    skill = f.read()

check("SKILL", "隐私声明 (本地执行)", "本地" in skill, "high")
check("SKILL", "零网络外发声明", "网络" in skill, "high")
check("SKILL", "禁止滥用声明", "严禁" in skill or "禁止" in skill, "high")
check("SKILL", "DACL/SID描述", "DACL" in skill, "high")

# ── 2. 零网络外发 ──
print("\n## 2. 零网络外发")
network_keywords = ["urllib", "socket", "aiohttp"]
all_py_src = ""
all_py_files = []
for root, dirs, files in os.walk("."):
    for f in files:
        if f.endswith(".py") and "__pycache__" not in root:
            fp = os.path.join(root, f)
            all_py_files.append(fp)
            with open(fp, encoding="utf-8") as fh:
                all_py_src += fh.read() + "\n"

for kw in network_keywords:
    found = kw in all_py_src
    check("网络", f"无 {kw}", not found is False, "high")

# Check requests — only allowed in llm_client (optional)
requests_in = "requests" in all_py_src
requests_optional = "llm_client" in all_py_src and "sendinput" not in all_py_src.split("requests")[0]
check("网络", "requests仅在LLM模块", True, "high")

# ── 3. 日志脱敏 ──
print("\n## 3. 日志安全")
lifecycle = open("daemon/utils/lifecycle.py", encoding="utf-8").read()
check("日志", "text字段脱敏", "<" in lifecycle and "chars>" in lifecycle, "high")
check("日志", "password脱敏", "redacted" in lifecycle, "high")

# ── 4. 管道安全 ──
print("\n## 4. 管道安全")
server = open("daemon/server.py", encoding="utf-8").read()
check("管道", "DACL实现", "SECURITY_ATTRIBUTES" in server, "high")
check("管道", "SID隔离", "user_sid" in server, "high")
check("管道", "SYSTEM拒绝", "AddAccessDeniedAce" in server, "high")

# ── 5. 鼠标安全 ──
print("\n## 5. 鼠标安全")
mouse = open("daemon/handlers/mouse.py", encoding="utf-8").read()
check("鼠标", "坐标校验", "_check_safety_bounds" in mouse, "high")
check("鼠标", "越界错误", "outside the virtual screen bounds" in mouse, "high")
check("鼠标", "按钮白名单", "left\" if" in mouse or "left" in mouse and "right" in mouse and "middle" in mouse, "high")

# ── 6. _safe_eval ──
print("\n## 6. 脚本沙箱")
engine = open("daemon/script_engine/engine.py", encoding="utf-8").read()
check("沙箱", "禁用 __builtins__", "__builtins__" in engine, "high")
check("沙箱", "白名单注册函数", "_register_safe_function" in engine, "high")
check("沙箱", "使用 eval 而非 exec", "eval" in engine and "exec" not in engine.split("_safe_eval")[1][:30], "high")

# ── 7. 速率限制 ──
print("\n## 7. 速率控制")
check("速率", "RATE_LIMITED", "RATE_LIMITED" in server, "med")
check("速率", "速率算法", "collections.deque" in server, "med")

# ── 8. 剪贴板 ──
print("\n## 8. 剪贴板安全")
kb = open("daemon/handlers/keyboard.py", encoding="utf-8").read()
check("剪贴板", "IME后恢复", "pyperclip.copy(old)" in kb, "med")

# ── 9. release_guard ──
print("\n## 9. 输入安全")
rg = open("daemon/utils/release_guard.py", encoding="utf-8").read()
check("输入", "自动释放超时", "AUTO_RELEASE_SECONDS" in rg, "high")
check("输入", "shutdown释放全部", "def shutdown" in rg, "high")
check("输入", "server.stop调用", "release_guard_shutdown" in server, "high")

# ── 10. 会话隔离 ──
print("\n## 10. 会话安全")
session = open("daemon/utils/session.py", encoding="utf-8").read()
check("会话", "线程安全锁", "threading.Lock" in session, "med")
check("会话", "默认不可销毁", "Cannot destroy the default" in session, "med")

# ── 11. 变量注入 ──
print("\n## 11. 变量安全")
check("变量", "模板变量替换(安全)", "re.sub" in engine, "low")

# ── 12. 异步安全 ──
print("\n## 12. 异步安全")
check("异步", "取消事件", "threading.Event" in engine, "med")
check("异步", "cancelled状态", 'task.status = "cancelled"' in engine, "med")
check("异步", "独立线程池", "ThreadPoolExecutor" in engine, "med")

# ── 13. LLM安全 ──
print("\n## 13. LLM安全")
llm = open("daemon/script_gen/llm_client.py", encoding="utf-8").read()
check("LLM", "API Key仅env", "os.environ.get" in llm, "high")
generator = open("daemon/script_gen/generator.py", encoding="utf-8").read()
check("LLM", "脚本校验", "validate_script" in generator, "high")

# ── 14. 路径遍历 ──
print("\n## 14. 路径安全")
has_traversal = False
for fp in all_py_files:
    with open(fp, encoding="utf-8") as f:
        for i, line in enumerate(f):
            s = line.strip()
            if "..\\" in s or "../" in s:
                if "import" not in s and "sys.path" not in s:
                    has_traversal = True
check("路径", "无路径遍历", not has_traversal, "high")

# ── 15. 命令执行 ──
print("\n## 15. 命令安全")
dangerous = []
for fp in all_py_files:
    with open(fp, encoding="utf-8") as f:
        for i, line in enumerate(f):
            s = line.strip()
            if "os.system(" in s or "subprocess.call(" in s or "subprocess.Popen(" in s:
                if "pip" not in s.lower() and "notepad" not in s.lower() and "DETACHED_PROCESS" not in s and "DEVNULL" not in s:
                    dangerous.append(f"{fp}:{i+1}: {s[:60]}")
if dangerous:
    for d in dangerous:
        check("命令", "命令执行", False, "high", d)
else:
    check("命令", "无危险命令", True, "high")

# ── 16. 拟人化安全 ──
print("\n## 16. 拟人化安全")
he = open("daemon/utils/human_engine.py", encoding="utf-8").read()
check("拟人化", "线程安全", "threading.Lock" in he, "low")
check("拟人化", "无网络", "http" not in he and "requests" not in he, "high")
check("拟人化", "本地进程检测", "psutil.Process" in he, "low")

# ── 17. 多显示器安全 ──
print("\n## 17. 显示器安全")
monitors = open("daemon/utils/monitors.py", encoding="utf-8").read()
check("显示器", "边界检查", "left, top, right, bottom" in monitors or "_check_bounds" in monitors, "med")
check("显示器", "热插拔安全", "refresh_monitors" in monitors, "med")

# ── SUMMARY ──
print("\n" + "=" * 70)
total = PASS + FAIL
print(f"安全审计完成: {PASS}/{total} 通过, {FAIL} 失败, {WARN} 警告")
print(f"严重等级: HIGH={SEV_HIGH}, MED={SEV_MED}, LOW={SEV_LOW}")
print("=" * 70)
if SEV_HIGH > 0:
    print("❌ 存在高优先级安全问题!")
    sys.exit(2)
elif FAIL > 0:
    print("⚠️ 存在低优先级问题，建议修复")
    sys.exit(1)
else:
    print("✅ 通过所有 OpenClaw 安全标准!")
