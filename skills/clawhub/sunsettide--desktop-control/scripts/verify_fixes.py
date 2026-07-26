"""
验证所有修复：变量替换、OCR环境、窗口恢复。
"""
import sys, os, time, shutil, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

# Clear cache
for root, dirs, files in os.walk("."):
    for d in list(dirs):
        if d == "__pycache__":
            try: shutil.rmtree(os.path.join(root, d))
            except: pass

from client.client import send_request

PASS = 0; FAIL = 0
def test(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1
    else: FAIL += 1
    print(f"  [{'OK' if ok else 'FAIL'}] {name}: {detail[:80]}")

print("=" * 60)
print("验证修复 — v1.1.3")
print("=" * 60)

# Restart daemon (make sure it picks up new code)
try: send_request("daemon_shutdown", {})
except: pass
time.sleep(2)
r = send_request("ping", {})
pid = r.get("result", {}).get("data", {}).get("pid")
print(f"Daemon: {pid}")

# ── 测试1: {{var}} 同步路径变量替换 ──
print("\n## 测试1: {{var}} 同步路径变量替换")
r = send_request("script_run_sync", {"script": {
    "variables": {"a": 300, "b": 400},
    "steps": [
        {"action": "mouse_move", "params": {"x": "{{a}}", "y": "{{b}}"}},
    ]
}})
d = (r.get("result") or {}).get("data", {})
test("#42 script_run_sync {{var}}", d.get("status") == "completed", f"status={d.get('status')}")

# ── 测试2: {{var}} 异步路径变量替换 ──
print("\n## 测试2: {{var}} 异步路径变量替换")
r = send_request("script_run", {"script": {
    "variables": {"msg": "AsyncVarWorks"},
    "steps": [{"action": "keyboard_type", "params": {"text": " {{msg}} "}}],
}})
d = (r.get("result") or {}).get("data", {})
tid = d.get("task_id", "")
test("#42 script_run {{var}} 提交", d.get("status") == "running", f"task={tid[:12]}")
if tid:
    time.sleep(1)
    r2 = send_request("script_results", {"task_id": tid})
    d2 = (r2.get("result") or {}).get("data", {})
    test("#42 script_run {{var}} 完成", d2.get("status") == "completed", f"status={d2.get('status')}")

# ── 测试3: OCR find_text ──
print("\n## 测试3: OCR find_text")
# Type text
send_request("window_focus", {"title": "记事本"})
time.sleep(0.3)
send_request("mouse_click", {"x": 100, "y": 200})
time.sleep(0.2)
send_request("keyboard_type", {"text": " ZZ_FixVerify "})
time.sleep(1.5)

r = send_request("find_text", {"text": "FixVerify", "lang": "eng", "exact_match": False, "limit": 5})
d = (r.get("result") or {}).get("data", {})
matches = d.get("matches", [])
test("#37 find_text 返回结果", len(matches) > 0, f"{len(matches)} matches")
for m in matches:
    print(f'    text="{m.get("text","")}" at ({m.get("x","?")},{m.get("y","?")})')

if matches:
    r2 = send_request("click_text", {"text": "FixVerify", "lang": "eng", "exact_match": False, "wait": 0.2})
    d2 = (r2.get("result") or {}).get("data", {})
    test("#38 click_text 点击", d2.get("success"), f"at={d2.get('clicked_at')}")

# ── 测试4: 窗口枚举 ──
print("\n## 测试4: 窗口管理")
r = send_request("window_list", {})
d = (r.get("result") or {}).get("data", {})
windows = d.get("windows", [])
test("#27 窗口列表非空", len(windows) > 0, f"{len(windows)} windows")

# ── 测试5: OCR环境 — 直接测试screen_ocr ──
print("\n## 测试5: OCR环境")
r = send_request("screen_ocr", {"lang": "eng"})
d = (r.get("result") or {}).get("data", {})
if d:
    chars = d.get("chars", 0)
    test("screen_ocr 返回文字", chars > 50, f"{chars} chars")
else:
    err = r.get("error", {}).get("message", "?")
    test("screen_ocr 错误", False, err[:60])

# ── 汇总 ──
print(f"\n{'='*60}")
print(f"修复验证: {PASS}/{PASS+FAIL} 通过")
if FAIL == 0:
    print("✅ 所有修复验证通过!")
else:
    print("❌ 有失败项")
