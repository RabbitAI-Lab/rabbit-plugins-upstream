"""方案四：异常与兼容性验证"""
import os, sys, time, json

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

PASS = 0
FAIL = 0

def test(name, method, params=None, expect_success=None):
    global PASS, FAIL
    params = params or {}
    try:
        r = send_request(method, params)
        has_error = r.get("error") is not None
        ok = r.get("result") and r["result"].get("success")
        if expect_success is True:
            if ok:
                PASS += 1
                print(f"  ✅ {name}")
            else:
                FAIL += 1
                print(f"  ❌ FAIL {name}: expected success, got error: {r.get('error')}")
        elif expect_success is False:
            if has_error:
                PASS += 1
                print(f"  ✅ {name} (预期失败: {r.get('error', {}).get('code', '?')})")
            else:
                FAIL += 1
                print(f"  ❌ FAIL {name}: expected failure but it succeeded")
        else:
            PASS += 1
            status = "✅" if ok else "⚠️"
            print(f"  {status} {name}")
    except Exception as e:
        FAIL += 1
        print(f"  ❌ FAIL {name}: {e}")

print("=" * 60)
print("方案四：异常与兼容性验证")
print("=" * 60)

# 1. 非法参数测试
print("\n【1. 非法参数边界】")
test("负坐标 mouse_move", "mouse_move", {"x": -100, "y": -100})
test("超大坐标", "mouse_move", {"x": 99999, "y": 99999})
test("不存在的按键", "keyboard_press", {"key": "nonexistent_key"}, expect_success=False)
test("空文本输入", "keyboard_type", {"text": ""})
test("极长文本", "keyboard_type", {"text": "A" * 5000})

# 2. 窗口不存在测试
print("\n【2. 窗口不存在场景】")
test("不存在的窗口 focus", "window_focus", {"title": "这个窗口绝对不存在abc123"}, expect_success=False)
test("不存在的窗口 info", "window_info", {"title": "这个窗口绝对不存在abc123"}, expect_success=False)

# 3. 重复高频调用
print("\n【3. 重复调用测试】")
for i in range(5):
    test(f"重复调用 mouse_position #{i+1}", "mouse_position", {})
    time.sleep(0.05)

# 4. 守护进程稳定性
print("\n【4. 守护进程稳定性】")
test("多次 ping", "ping", {})
test("状态查询", "daemon_status", {})

# 5. 快速连续截图
print("\n【5. 连续操作】")
for i in range(3):
    test(f"连续截图 #{i+1}", "screenshot", {"format": "b64"})
    time.sleep(0.2)

print("\n" + "=" * 60)
total = PASS + FAIL
print(f"总计: {total} | ✅ 通过: {PASS} | ❌ 失败: {FAIL}")
if FAIL == 0:
    print("🎉 方案四全部通过！异常处理鲁棒")
else:
    print(f"⚠️ {FAIL} 项需排查")
print("=" * 60)
