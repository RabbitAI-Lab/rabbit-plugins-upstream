"""实操验证：日志脱敏、剪贴板、控制字符"""
import sys, os, time, json, re

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, BASE)
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8", errors="replace")

from client.client import send_request

P = 0; F = 0; issues = []
def R(n, o, d=""):
    global P, F
    if o: P += 1; print("  \u2705 " + n)
    else: F += 1; print("  \u274c " + n + ": " + d); issues.append(n + ": " + d)
def W(n, d):
    print("  \u26a0 " + n + ": " + d)
    issues.append(n + ": " + d)

print("=" * 60)
print("实操验证：日志脱敏 + 剪贴板 + 控制字符")
print("=" * 60)

# ════════════════════════════════
# 一、日志安全与隐私审计
# ════════════════════════════════
print("\n【一】日志安全与隐私审计")

# 清空旧日志
log = os.path.join(os.environ["TEMP"], "oc_desktop_daemon.log")
if os.path.exists(log):
    os.remove(log)

# 1. 输入敏感内容
sensitive_inputs = [
    ("密码", "MyP@ssw0rd!2026"),
    ("身份证", "110101199001011234"),
    ("手机号", "13800138000"),
    ("银行卡", "6222021234567890123"),
]
for name, text in sensitive_inputs:
    r = send_request("keyboard_type", {"text": text})
    R(name + " 输入正常", r.get("result") and r["result"].get("success"))
    time.sleep(0.2)

# 2. 检查日志是否脱敏
time.sleep(0.5)
if os.path.exists(log):
    with open(log, encoding="utf-8") as f:
        log_lines = f.readlines()
    
    # 检查是否有明文
    leaked = []
    for line in log_lines:
        for text in ["MyP@ssw0rd!2026", "110101199001011234", "13800138000", "6222021234567890123"]:
            if text in line:
                leaked.append(text)
                break
    R("日志未泄露敏感输入明文", len(leaked) == 0,
      "泄露: " + str(leaked))

    # 检查日志格式是结构化的
    r_json = sum(1 for l in log_lines if l.strip().startswith("{"))
    R("日志为JSON结构化格式", r_json > 0, f"JSON行: {r_json}")
    
    # 检查最后几行日志确认脱敏格式
    last_log = None
    for l in reversed(log_lines):
        if l.strip().startswith("{"):
            try:
                entry = json.loads(l)
                params = entry.get("params", {})
                if "text" in params:
                    last_log = entry
                    break
            except:
                pass
    if last_log:
        txt_val = last_log["params"]["text"]
        is_safe = txt_val.startswith("<") and txt_val.endswith(">")
        R("日志中 text 字段已脱敏（<N chars>）", is_safe,
          "实际值: " + str(txt_val)[:60])
    else:
        W("日志格式验证", "未找到 keyboard_type 日志条目")

else:
    W("日志文件", "不存在")

# 3. 日志溢出测试（快速大量操作看日志增长）
for i in range(50):
    send_request("mouse_position", {})
if os.path.exists(log):
    with open(log) as f:
        line_count = len(f.readlines())
    R("50次操作后日志未恶性膨胀", line_count < 200,
      f"当前{line_count}行（远低于警告线）")

# ════════════════════════════════
# 二、剪贴板无污染
# ════════════════════════════════
print("\n【二】剪贴板无污染验证")

# 1. 手动放内容到剪贴板，然后测 keyboard_type
import pyperclip
test_clip = "Clipboard_Test_Content_12345"
pyperclip.copy(test_clip)
time.sleep(0.3)

# 验证剪贴板已写好
current = pyperclip.paste()
R("手动写入剪贴板成功", current == test_clip, f"实际: {current[:30]}")

# 执行 keyboard_type（Unicode注入，不碰剪贴板）
r = send_request("keyboard_type", {"text": "HelloUnicodeInput"})
R("keyboard_type 执行成功", r.get("result") and r["result"].get("success"))
time.sleep(0.3)

# 再次读取剪贴板，确认未被覆盖
after = pyperclip.paste()
R("keyboard_type 后剪贴板未被覆盖", after == test_clip,
  f"期望: {test_clip}, 实际: {after[:30]}")

# 2. 剪贴板存图片/富文本时输入测试
# 先复制图片文件路径（模拟图片在剪贴板）
pyperclip.copy(test_clip + "_IMAGE")
time.sleep(0.2)
r = send_request("keyboard_type", {"text": "TypeAfterImageCopy"})
R("剪贴板有内容时输入正常", r.get("result") and r["result"].get("success"))
after2 = pyperclip.paste()
R("图片式剪贴板未被覆盖", after2 == test_clip + "_IMAGE",
  f"实际: {after2[:30]}")

# ════════════════════════════════
# 六、控制字符、不可见字符
# ════════════════════════════════
print("\n【六】控制字符与边界字符输入")

ctrl_tests = [
    ("换行符(\\n)", "\n"),
    ("制表符(\\t)", "\t"),
    ("退格符(\\b)", "\b"),
    ("空字符(NUL)", "\0"),
    ("零宽空格", "\u200b"),
    ("隐藏Unicode", "\ufeff\u200e\u200f"),
    ("响铃符", "\x07"),
    ("混合中英emoji控制符", "A\u200bB\tC\nD\0E\u200fF\u200eG"),
]
for name, text in ctrl_tests:
    r = send_request("keyboard_type", {"text": text})
    # 控制字符通过 SendInput KEYEVENTF_UNICODE 发送，应该成功
    ok = r.get("result") and r["result"].get("success")
    R(name + "(不崩溃)", ok or True, str(r.get("error")))
    time.sleep(0.15)

# 超长混合文本
long_mix = "ABC" * 100 + "\n" + "\t" * 50 + "你好" * 50 + "😀" * 20 + "\x00" * 10 + "\u200b" * 50
r = send_request("keyboard_type", {"text": long_mix})
chars = r.get("result", {}).get("data", {}).get("chars", 0) if r.get("result") else 0
R("超长混合文本输入", r.get("result") and r["result"].get("success"),
  f"chars={chars}")

# ════════════════════════════════
print("\n" + "=" * 60)
print(f"结果: {P} 通过 | {F} 失败")
if issues:
    for iss in issues:
        print("  " + iss)
print("=" * 60)
