#!/usr/bin/env python3
"""ClawCode Lens — sikkerheds-scanning (unik feature)."""
import sys
import re

PATTERNS = [
    ("KRITISK", r"(api[_-]?key|secret|password|token)\s*[=:]\s*['\"][A-Za-z0-9_\-]{12,}['\"]",
     "Hardcodet nøgle/hemmelighed — brug miljøvariabel"),
    ("HØJ", r"(SELECT|INSERT|UPDATE|DELETE).*f['\"]\s*[+%]|f['\"].*\{.*\}.*(SELECT|INSERT)",
     "Mulig SQL-injektion — brug parameteriserede queries"),
    ("HØJ", r"\beval\s*\(", "eval() — eksekverer vilkårlig kode, undgå"),
    ("HØJ", r"\bexec\s*\(", "exec() — eksekverer vilkårlig kode, undgå"),
    ("MEDIUM", r"os\.system\s*\(", "os.system() — brug subprocess med argument-liste"),
    ("MEDIUM", r"input\s*\(.*\)\s*$", "Rå input() uden validering"),
    ("LOW", r"http://", "HTTP (ukrypteret) — brug HTTPS"),
]


def scan(path: str) -> str:
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.readlines()
    out = [f"🔒 Sikkerheds-scan: {path}", ""]
    hits = 0
    for i, line in enumerate(lines, 1):
        for sev, pattern, msg in PATTERNS:
            if re.search(pattern, line, re.I):
                out.append(f"  [{sev}] Linje {i}: {msg}")
                out.append(f"         → {line.strip()[:90]}")
                hits += 1
    if hits == 0:
        out.append("  ✅ Ingen kendte mønstre fundet.")
    out.append(f"\n{len(lines)} linjer scannet · {hits} fund")
    return "\n".join(out)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit("BRUG: python3 security_scan.py fil.py [--out rapport.md]")
    report = scan(sys.argv[1])
    if "--out" in sys.argv:
        out_path = sys.argv[sys.argv.index("--out") + 1]
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"✅ Rapport gemt: {out_path}")
    else:
        print(report)
