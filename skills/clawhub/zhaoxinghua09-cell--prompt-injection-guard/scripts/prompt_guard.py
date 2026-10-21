#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""prompt-injection-guard — 提示注入/恶意指令检测（LGD 威胁模式库）。
理论根基：LGD 三律·有门禁（fail-closed）。Usage:
  python prompt_guard.py <file|text> [--json] [--badge out.svg]"""
import argparse, base64, hashlib, json, re, sys

THREATS = {
    "prompt_injection": [
        r"(?i)ignore (all )?(previous|prior|above) instructions",
        r"(?i)jailbreak|dan mode|system prompt override",
        r"[\u200b\u200c\u200d\u2060\u2062\u2063]",
    ],
    "hardcoded_secret": [
        r"(?i)(api[_-]?key|secret|token|password|passwd)\s*[:=]\s*['\"]?[A-Za-z0-9_\-]{16,}",
        r"(?i)(ghp_|sk-|AKIA|gho_)[A-Za-z0-9_\-]{16,}",
        r"(?i)private[_ ]?key|BEGIN [A-Z ]*PRIVATE KEY",
    ],
    "destructive_command": [
        r"(?i)rm\s+-rf\s*/|rm\s+-rf\s+~\s*$",
        r"(?i)DROP TABLE|DROP DATABASE",
        r"(?i)mkfs|dd\s+if=.*of=/dev/",
    ],
    "data_exfiltration": [
        r"(?i)curl\s+[^|]*\s+-d\s|curl\s+.*\|.*sh",
        r"(?i)~\/(\.ssh|\.aws|\.gnupg|\.git)",
        r"(?i)rev(erse)?[- ]?shell",
    ],
    "crypto_mining": [r"(?i)xmrig|coinhive|minerd|cpuminer|stratum\+tcp"],
    "privilege_escalation": [
        r"(?i)sudo\s+rm|chmod\s+777|chown\s+root",
        r"(?i)useradd\s+-o|passwd\s+-?\w*\s+root",
    ],
    "persistence": [
        r"(?i)crontab|@reboot|authorized_keys",
        r"(?i)\.bashrc|rc\.local|systemctl\s+enable",
    ],
    "obfuscation": [
        r"(?i)base64\s*-d\s*\||base64\s*--decode\s*\|",
        r"(?i)eval\(\$\(|compile\(.*exec\(|__import__\(['\"]os",
    ],
}

def scan(text):
    hits = []
    for cat, pats in THREATS.items():
        for p in pats:
            for m in re.finditer(p, text):
                hits.append({"category": cat, "pattern": p, "snippet": text[max(0, m.start()-20):m.end()+20]})
                break
    return hits

def score_text(text):
    hits = scan(text)
    # SAFE 角度：威胁扫描 45 分基线，每类命中 -6
    safe = max(0, 45 - len({h["category"] for h in hits}) * 6)
    machine = 55  # 基础机器可读分（输入输出结构化）
    total = round((safe + machine) / 2)
    return {"safe": safe, "machine": machine, "total": total,
            "verdict": "PASS" if total >= 60 else "FAIL", "hits": hits}

def esc(s):
    return s.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")

def make_badge(total, verdict):
    vc = "#16a34a" if verdict == "PASS" else "#f87171"
    label, score = "LGD SAFE", f"{total}/100"
    H, lf, vf = 20, 9, 10
    lw = 6 + 22 + lf * 0.62 * len(label)
    vw = 8 + vf * 0.62 * len(score)
    W = int(lw + vw)
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="{esc(label)} {esc(score)}">'
            f'<rect x="0.5" y="0.5" width="{W-1}" height="{H-1}" rx="4" fill="#ffffff" stroke="#e2e8f0" stroke-width="1"/>'
            f'<rect x="1" y="1" width="22" height="{H-2}" rx="3" fill="#16a34a"/>'
            f'<text x="12" y="13.8" fill="#ffffff" font-size="8.5" font-weight="500" text-anchor="middle" font-family="Segoe UI,Arial,sans-serif">SAFE</text>'
            f'<text x="30" y="13.9" fill="#0f172a" font-size="10" font-weight="500" font-family="Segoe UI,Arial,sans-serif">{esc(score)}</text></svg>')

def main():
    p = argparse.ArgumentParser()
    p.add_argument("input", help="file path or text")
    p.add_argument("--json", action="store_true")
    p.add_argument("--badge", help="output badge svg path")
    a = p.parse_args()
    if os.path.isfile(a.input):
        text = open(a.input, encoding="utf-8", errors="replace").read()
    else:
        text = a.input
    res = score_text(text)
    sha = hashlib.sha256(text.encode()).hexdigest()[:8]
    res["sha256_8"] = sha
    if a.badge:
        open(a.badge, "w", encoding="utf-8").write(make_badge(res["total"], res["verdict"]))
        print("badge written:", a.badge)
    if a.json:
        print(json.dumps(res, ensure_ascii=False, indent=2))
    else:
        print(f"SAFE={res['safe']} MACH={res['machine']} TOTAL={res['total']} {res['verdict']} (sha {sha})")
        for h in res["hits"]:
            print(f"  [HIT] {h['category']}: ...{h['snippet']}...")
    return 0 if res["verdict"] == "PASS" else 1

if __name__ == "__main__":
    sys.exit(main())
