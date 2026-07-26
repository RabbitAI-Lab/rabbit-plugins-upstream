"""方案二/三合并验证：OpenClaw 开发模式 + 端到端能力验证"""
import os, sys, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

print("=" * 60)
print("方案二/三：端到端能力验证")
print("=" * 60)

tests = 0
passed = 0

def t(name, fn):
    global tests, passed
    tests += 1
    try:
        r = fn()
        if r.get("result") and r["result"].get("success"):
            passed += 1
            print(f"  [{tests}] {name}")
        else:
            print(f"  [{tests}] {name} -> {r.get('error', 'unknown')}")
    except Exception as e:
        print(f"  [{tests}] {name} -> ERROR: {e}")

# 1. 守护进程
print("\n【1. 守护进程状态】")
t("ping", lambda: send_request("ping", {}))
t("daemon_status", lambda: send_request("daemon_status", {}))

# 2. 鼠标
print("\n【2. 鼠标操作】")
t("mouse_move", lambda: send_request("mouse_move", {"x": 960, "y": 540}))
time.sleep(0.3)
t("mouse_click", lambda: send_request("mouse_click", {"button": "left"}))
time.sleep(0.3)
t("mouse_position", lambda: send_request("mouse_position", {}))

# 3. 键盘
print("\n【3. 键盘操作】")
t("keyboard_type", lambda: send_request("keyboard_type", {"text": "desktop-control test"}))

# 4. 窗口
print("\n【4. 窗口管理】")
t("window_list", lambda: send_request("window_list", {}))

# 5. 截图
print("\n【5. 截图】")
t("screenshot", lambda: send_request("screenshot", {"format": "b64"}))

# 6. 整体状态
print("\n" + "=" * 60)
print(f"测试: {tests} | 通过: {passed}")
if passed == tests:
    print("🎉 方案二/三全部通过！技能功能完整")
else:
    print(f"⚠️ {tests-passed} 项失败")
print("=" * 60)
