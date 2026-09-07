#!/usr/bin/env python3
import importlib.util, shutil, subprocess, sys

mods = [
    "rdkit", "openmm", "MDAnalysis", "mdtraj", "prolif", "Bio", "gemmi",
    "pandas", "numpy", "scipy", "sklearn", "requests", "meeko"
]
cmds = ["vina", "obabel"]

print("Python:", sys.version)
print("\nPython modules:")
ok = True
for m in mods:
    found = importlib.util.find_spec(m) is not None
    print(f"  {m:12s} {'OK' if found else 'MISSING'}")
    ok = ok and found

print("\nExecutables:")
for c in cmds:
    path = shutil.which(c)
    print(f"  {c:12s} {path or 'MISSING'}")
    ok = ok and bool(path)

if shutil.which("vina"):
    try:
        out = subprocess.run(["vina", "--version"], text=True, capture_output=True, timeout=10)
        print("\nVina version:", (out.stdout or out.stderr).strip())
    except Exception as e:
        print("Vina check failed:", e)

raise SystemExit(0 if ok else 1)
