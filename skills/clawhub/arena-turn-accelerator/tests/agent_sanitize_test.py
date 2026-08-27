#!/usr/bin/env python3
"""A hostile ARENA_AGENT name must fail loudly with a clean message (never
silently fall back to the shared state dir). v1.5.0 regression."""
import os, subprocess, sys, pathlib

HERE = pathlib.Path(__file__).resolve().parent.parent / "scripts"
env = dict(os.environ)
env["ARENA_AGENT"] = "../evil"
r = subprocess.run([sys.executable, str(HERE / "request_lifecycle.py"), "new", "x"],
                   capture_output=True, text=True, env=env)
combined = r.stdout + r.stderr
ok = r.returncode != 0 and "agent name" in combined
# and a valid name must work
env["ARENA_AGENT"] = "claude-code"
r2 = subprocess.run([sys.executable, str(HERE / "request_lifecycle.py"), "status"],
                    capture_output=True, text=True, env=env)
ok = ok and r2.returncode == 0
sys.exit(0 if ok else 1)
