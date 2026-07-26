"""方案十五：字符集输入专项测试"""
import sys, os, time

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
        print(f"  \u2705 {name}")
    else:
        FAIL += 1
        print(f"  \u274c {name}: {detail}")
        issues.append(f"{name}: {detail}")

print("=" * 50)
print("方案十五：字符集输入专项测试")
print("=" * 50)

tests = [
    ("密码类型", "P@ssw0rd!2026#$%^&*"),
    ("混合特殊符号", '!@#$%^&*()_+-=[]{}|;:,.<>?~`'),
    ("500个中文字", "字" * 500),
    ("换行符", "line1\nline2\nline3"),
    ("制表符", "col1\tcol2\tcol3"),
]

for name, text in tests:
    r = send_request("keyboard_type", {"text": text})
    report(name, r.get("result") and r["result"].get("success"), str(r.get("error")))
    time.sleep(0.3)

print(f"\n{PASS}/{PASS+FAIL} 通过")
if not issues:
    print("\u2728 方案十五全部通过")
