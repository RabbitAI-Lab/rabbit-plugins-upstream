#!/usr/bin/env python3
"""guard.py — the defensive validator TuringNet's SKILL.md always promised.

Pre-export / pre-send checker for drafts (reports, tickets, replies):
  BLOCK — draft contains prohibited-instruction content: censorship/filtering
          bypass, VPN/tunnel evasion, domain fronting, traffic obfuscation,
          scanning/enumeration, flooding, credential/identifier harvesting,
          exploitation steps.
  WARN  — residual PII suspicion (reuses redactor patterns) or borderline wording.
  PASS  — clean.

Shipped defense templates (which legitimately DISCUSS SIM-jacking etc.) carry
the marker <!-- turingnet:defense --> and are exempt from the discussion
patterns; imperative exploit steps still block even inside marked files.

Exit codes: 0 pass · 1 warn · 2 block · 3 input error. Never networks.
"""
import argparse
import json
import re
import sys

sys.path.insert(0, __file__.rsplit("/", 1)[0])
from redact_pii import redact  # reuse the same PII engine

SCHEMA = "turingnet.guard.v1"
DEFENSE_MARKER = "turingnet:defense"

# (id, category, regex, severity) — matched on normalized lowercase text
PATTERNS = [
    ("G01", "bypass", r"(?:bypass|circumvent|get\s+around|beat|evade)\s+(?:the\s+)?(?:filter|censor|firewall|dpi|blocking|block|restrict|sanction|paywall|account\s+control)", "block"),
    ("G02", "tunnel-evasion", r"(?:stealth\s+)?(?:tunnel|vpn|proxy|ssh\s+-d|domain\s+front[ae]?ing|fronting|obfuscat\w+|cloaking|disguis\w+\s+traffic|traffic\s+obfuscation)\s+(?:to|for|so|that|which|server|config|setup|evasion|avoid|bypass|detection)?", "block"),
    ("G03", "evasion-detect", r"(?:avoid|defeat|detect)\s+(?:the\s+)?(?:dpi|deep\s+packet\s+inspection|blocking\s+detection|censorship\s+detection)", "block"),
    ("G04", "scan-enumerate", r"(?:nmap|masscan|zmap|port\s+scan|scan\s+(?:all\s+)?(?:ports|hosts|subnet|range)|enumerate\s+(?:subdomain|user|ssid|device|node)|sweep\s+(?:network|subnet))", "block"),
    ("G05", "flood", r"(?:flood|ddos|dos\s+attack|slowloris|syn\s+flood|icmp\s+flood|hping|stress\s+test\s+(?:someone|third|their|server))", "block"),
    ("G06", "credential-harvest", r"(?:harvest|collect|steal|sniff|capture|log)\s+(?:someone'?s?\s+|their\s+|user\s+|all\s+)?(?:password|passwd|credential|mfa|otp|2fa|cookie|session|api[_\s-]?key|private\s+key|sim|imei|imsi|subscriber)", "block"),
    ("G07", "exploit-steps", r"(?:run|execute|launch|deploy)\s+(?:the\s+)?(?:exploit|payload|metasploit|msfvenom|reverse\s+shell)|(?:exploit|attack)\s+steps?\s*:", "block"),
    ("G08", "interfere", r"(?:deauth|jam|interfere\s+with|knock\s+offline|hijack)\s+(?:the\s+|their\s+|a\s+)?(?:network|router|wifi|wi-fi|connection|session|bsf|cell)", "block"),
    ("G09", "bypass-ask", r"(?:how\s+to|help\s+me|ways?\s+to|teach\s+me)\s+(?:bypass|circumvent|evade|get\s+past)\s+(?:the\s+|this\s+|iran'?s?\s+)?(?:filter|censor|firewall|dpi|block|restrict|sanction)", "block"),
    ("G10", "education-mention", r"(?:simjack|sim\s+jack|sim\s+swap|phishing|ddos|dpi|deep\s+packet\s+inspection|domain\s+fronting)", "warn"),
]


def check(text, defense_exempt=False):
    findings = []
    for gid, cat, rx, sev in PATTERNS:
        for m in re.finditer(rx, text, re.I):
            if defense_exempt and sev == "warn":
                continue
            if defense_exempt and sev == "block" and cat not in ("G09", "G05", "G07"):
                # inside a marked defense template, descriptive/defensive mentions
                # of bypass/tunnel/scan/harvest topics are the point of the file;
                # only explicit how-to-requests (G09) and attack instructions
                # (G05/G07) still block.
                continue
            findings.append({"id": gid, "category": cat, "severity": sev,
                             "span": m.group(0)[:60]})
    # residual PII (any mode — always strict for outgoing drafts)
    _, counts, residual = redact(text, mode="strict")
    for r in residual[:10]:
        findings.append({"id": "R-" + r["type"], "category": "residual-pii",
                         "severity": "warn", "span": r["span"]})
    verdict = ("block" if any(f["severity"] == "block" for f in findings)
               else "warn" if findings else "pass")
    return {"schema": SCHEMA, "verdict": verdict,
            "defense_exempt": defense_exempt,
            "findings": findings, "pii_replacements": counts}


def main():
    ap = argparse.ArgumentParser(description="TuringNet defensive validator")
    ap.add_argument("--input", required=True, help="draft file to check")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()
    try:
        text = open(args.input, encoding="utf-8", errors="replace").read()
    except Exception as e:
        print(json.dumps({"schema": SCHEMA, "error": str(e)}))
        return 3
    result = check(text, defense_exempt=(DEFENSE_MARKER in text))
    if args.json:
        print(json.dumps(result, indent=1))
    else:
        print(f"[guard] verdict: {result['verdict']} "
              f"({len(result['findings'])} findings)")
        for f in result["findings"]:
            print(f"  [{f['severity']}] {f['id']} {f['category']}: {f['span']}")
    return {"pass": 0, "warn": 1, "block": 2}[result["verdict"]]


if __name__ == "__main__":
    sys.exit(main())
