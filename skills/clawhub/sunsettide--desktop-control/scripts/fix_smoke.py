import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fp = os.path.join(BASE, "scripts", "smoke_test_final.py")
with open(fp, encoding="utf-8") as f:
    c = f.read()
old = 'r.get("result",{}).get("data",{})'
new = '(r.get("result") or {}).get("data",{})'
c = c.replace(old, new)
with open(fp, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed all", c.count(new), "occurrences")
