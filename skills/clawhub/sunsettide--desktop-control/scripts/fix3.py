import os
BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
fp = os.path.join(BASE, "scripts", "destructive_test.py")
with open(fp, encoding="utf-8") as f:
    c = f.read()
c = c.replace('c.get("cancelled") == True', 'c.get("cancelled")')
with open(fp, "w", encoding="utf-8") as f:
    f.write(c)
print("Fixed")
