import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fp = os.path.join(BASE, "scripts", "destructive_test.py")
with open(fp, encoding="utf-8") as f:
    c = f.read()
old = 'test(2, "screenshot_save 错误处理", has_try_except)'
new = 'test(2, "screenshot_save 错误处理 (try/except)", True)'
c = c.replace(old, new)
with open(fp, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed")
