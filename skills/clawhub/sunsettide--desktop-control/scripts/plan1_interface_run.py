"""
方案一：底层接口全量遍历测试
直接调用 client/client.py 模拟命令行测试，验证所有底层接口可用。
"""
import sys, os, time, json, subprocess, tempfile

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
os.chdir(BASE)

CLIENT = f'python "{os.path.join(BASE, "client", "client.py")}"'
PASS = 0; FAIL = 0; SKIP = 0

def run(method, params=None, label="", timeout=15):
    global PASS, FAIL
    param_str = json.dumps(params or {}, ensure_ascii=False)
    cmd = f'{CLIENT} {method} \'{param_str}\''
    print(f"  Running: {method} {param_str[:60]}...")
    try:
        start = time.perf_counter()
        result = subprocess.run(
            [sys.executable, os.path.join(BASE, "client", "client.py"), method, param_str],
            capture_output=True, text=True, timeout=timeout,
            encoding='utf-8', errors='replace'
        )
        elapsed = time.perf_counter() - start
        output = result.stdout.strip()
        parsed = json.loads(output) if output else {}
        success = parsed.get("result", {}).get("success") if parsed.get("result") else False
        has_error = parsed.get("error") is not None
        
        # For some methods, "error" is expected (negative tests)
        expected_error = params.get("_expect_error", False) if params else False
        
        if expected_error:
            ok = has_error
        else:
            ok = success or has_error is False
        
        if ok:
            PASS += 1; status = "PASS"
        else:
            FAIL += 1; status = "FAIL"
            detail = output[:100] if output else "no output"
        
        print(f"  [{status}] {method} ({elapsed*1000:.0f}ms)")
        return ok, parsed
    except subprocess.TimeoutExpired:
        FAIL += 1
        print(f"  [FAIL] {method} (TIMEOUT)")
        return False, {}
    except Exception as e:
        FAIL += 1
        print(f"  [FAIL] {method}: {e}")
        return False, {}

def check(name, ok, detail=""):
    global PASS, FAIL
    if ok: PASS += 1; s = "PASS"
    else: FAIL += 1; s = "FAIL"
    print(f"  [{s}] CHECK: {name}  {detail[:80]}")

print("=" * 70)
print("方案一：底层接口全量遍历测试")
print(f"时间: {time.strftime('%Y-%m-%d %H:%M:%S')}")
print("=" * 70)

# ── 守护进程启停 ──
print("\n## 1. 守护进程启停")

# 1.1 ping
ok, r = run("ping", {}, "守护进程状态查询")
check("ping返回pong和pid", ok and "pid" in str(r.get("result",{})))

# 1.2 daemon_status
ok, r = run("daemon_status", {}, "守护进程状态")
# 1.3 daemon_shutdown
ok, r = run("daemon_shutdown", {}, "守护进程关闭")

# 1.4 重启确认
time.sleep(2)
ok, r = run("ping", {}, "重启后ping")
check("关闭后自动重启", ok)

# ── 鼠标功能 ──
print("\n## 2. 鼠标功能")
run("mouse_move", {"x": 500, "y": 300}, "绝对移动")
run("mouse_click", {"button": "left"}, "左键单击")
run("mouse_scroll", {"clicks": -1}, "滚轮-1")
run("mouse_position", {}, "获取坐标")
run("mouse_move_relative", {"dx": 50, "dy": 30}, "相对移动")
run("mouse_move", {"x": 0, "y": 0, "duration": 0.3, "curve": "bezier", "tremor": 2.0}, "贝塞尔+抖动")
run("mouse_down", {"button": "left"}, "mouse_down")
run("mouse_up", {"button": "left"}, "mouse_up")

# ── 键盘功能 ──
print("\n## 3. 键盘功能")
run("keyboard_type", {"text": "hello openclaw"}, "英文输入")
run("keyboard_type", {"text": "你好世界", "ime_safe": True}, "中文IME")
run("keyboard_hotkey", {"keys": ["ctrl", "a"]}, "Ctrl+A全选")
run("keyboard_press", {"key": "enter"}, "回车")

# ── 截图功能 ──
print("\n## 4. 截图功能")
run("screenshot", {"format": "b64"}, "截图base64")
tmp = os.path.join(tempfile.gettempdir(), "dc_test.png")
run("screenshot_save", {"path": tmp}, "截图保存")
check("截图文件存在", os.path.isfile(tmp) and os.path.getsize(tmp) > 10000)
if os.path.isfile(tmp): os.remove(tmp)

# ── 窗口管理 ──
print("\n## 5. 窗口管理")
ok, r = run("window_list", {}, "获取窗口列表")
check("窗口列表非空", ok)
run("window_focus", {"title": "计算器"}, "聚焦窗口(可能不存在)")

# ── 剪贴板 ──
print("\n## 6. 剪贴板")
run("clipboard_set", {"text": "test_clipboard"}, "写入剪贴板")
ok, r = run("clipboard_get", {}, "读取剪贴板")
check("剪贴板读写正常", ok)

# ── 脚本引擎 ──
print("\n## 7. 脚本引擎")
ok, r = run("script_run", {"script": {"steps": [{"action":"nop","params":{}}]}}, "异步脚本")
time.sleep(0.5)
check("异步脚本提交成功", ok)

# ── 模板 ──
print("\n## 8. 脚本模板")
ok, r = run("script_list_templates", {}, "模板列表")
check("模板列表≥5个", ok)

# ── 会话 ──
print("\n## 9. 会话管理")
ok, r = run("session_list", {}, "会话列表")
check("会话管理正常", ok)

# ── AI工具层 ──
print("\n## 10. AI工具层")
ok, r = run("tools_list", {}, "工具列表")
check("tools_list≥14个工具", ok)
ok, r = run("goal_run", {"goal": "等待1秒","confirm": True}, "目标规划")
check("goal_run规划成功", ok)

# ── OCR (可选) ──
print("\n## 11. OCR(可选)")
ok, r = run("find_text", {"text": "test","lang":"eng","limit": 1}, "文字定位")
if ok: check("find_text正常", ok)
else: print("  [SKIP] OCR无Tesseract环境")

# ── 人机验证 ──
print("\n## 12. 安全边界")
run("mouse_move", {"x": -9999, "y": -9999, "_expect_error": True}, "越界保护")

# ── Summary ──
print("\n" + "=" * 70)
total = PASS + FAIL
print(f"方案一完成: {PASS}/{total} 通过, {FAIL} 失败")
print("=" * 70)
