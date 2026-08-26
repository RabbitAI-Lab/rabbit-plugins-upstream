#!/usr/bin/env python3
"""Skill Curator — Production-grade skill auditor for OpenClaw.

Scans every skill in $WORKSPACE/skills and produces a quality report:
  - Quality score (0-100)
  - Severity-tagged findings (CRITICAL/HIGH/MEDIUM/LOW/INFO)
  - Remediation proposals (NEVER auto-edits — curator only proposes)

Safety-aware: legitimate tokens are allowlisted, `X∞` and `❌` markers are
preserved (NOT flagged as corruption), `openclaw-` namespace is protected.
"""
import os, re, json, argparse

WORKSPACE_DEFAULT = os.path.expanduser("~/.openclaw/workspace/skills")

# --- Allowlist: legitimate tokens that MUST NOT be flagged as leaks ---
ALLOWLIST_TOKENS = [
    "sk-2445356914f9fa3f-gp56ar-95020e53",  # web-search-9routers-backup (legitimate)
]

# --- Patterns that are INTENTIONAL, never corruption ---
PRESERVED_MARKERS = ["X∞", "❌"]  # Skill Architecture Standard name + anti-pattern marker

# --- God-mode language (authority too broad) ---
GODMODE = [
    r"PRIME DIRECTIVE",
    r"overrides?\s+all",
    r"authority too broad",
    r"BEFORE every (response|message)",
    r"you (MUST|WILL) (always|obey|do)",
]

# --- Raw exec / network (potential danger in a skill) ---
EXEC_NET = [
    r"exec\(", r"subprocess", r"os\.system", r"child_process",
    r"eval\(", r"curl\s", r"wget\s", r"rm\s+-rf", r"base64\s+-d", r"/bin/sh",
]

# --- Hidden / bidirectional unicode ---
HIDDEN_UNICODE = [0x200B, 0x200D, 0x2066, 0x2067, 0x2068, 0x202E, 0x202D]

EMOJI_RE = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F0FF"
    "\U0001F1E6-\U0001F1FF\U00002B00-\U00002BFF\U0000FE00-\U0000FE0F"
    "\U00002190-\U000021FF]"
)
TOKEN_RE = re.compile(r"sk-[a-z0-9]{10,}|ghp_[a-z0-9]{20,}|api[_-]?key\s*[:=]\s*['\"]?[a-z0-9]{20,}")


def parse_frontmatter(text):
    if not text.startswith("---"):
        return None, text
    end = text.find("\n---", 3)
    if end == -1:
        return None, text
    fm = text[3:end].strip()
    body = text[end + 4:]
    meta = {}
    for line in fm.splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            meta[k.strip()] = v.strip().strip("'\"")
    return meta, body


def audit_skill(path, all_names):
    r = {
        "dir": os.path.basename(path),
        "name": None, "score": 100, "findings": [],
    }
    skill_md = os.path.join(path, "SKILL.md")
    if not os.path.isfile(skill_md):
        r["findings"].append(("CRITICAL", "no SKILL.md"))
        r["score"] = 0
        return r

    text = open(skill_md, encoding="utf-8", errors="replace").read()
    meta, body = parse_frontmatter(text)
    if not meta:
        r["findings"].append(("CRITICAL", "no frontmatter"))
        r["score"] -= 40
    else:
        if "name" not in meta:
            r["findings"].append(("CRITICAL", "missing name"))
            r["score"] -= 25
        else:
            r["name"] = meta["name"]
        if "description" not in meta or len(meta.get("description", "")) < 30:
            r["findings"].append(("MEDIUM", "description missing/too short (should be task-scoped)"))
            r["score"] -= 8
        else:
            # task-scoped check: description should say WHEN to use
            if not re.search(r"gunakan|saat|when|use this|if (user|asked)", meta["description"], re.I):
                r["findings"].append(("MEDIUM", "description not task-scoped (add 'Gunakan saat...')"))
                r["score"] -= 5

    # _meta.json
    if not os.path.isfile(os.path.join(path, "_meta.json")):
        r["findings"].append(("MEDIUM", "no _meta.json (needed for publish)"))
        r["score"] -= 6

    # GUARDRAILS / CHANGELOG
    if "GUARDRAILS" not in text:
        r["findings"].append(("MEDIUM", "no GUARDRAILS section"))
        r["score"] -= 6
    if "CHANGELOG" not in text:
        r["findings"].append(("LOW", "no CHANGELOG"))
        r["score"] -= 3

    # God-mode (scan body only, exclude backtick-wrapped example text to avoid self-flag)
    scan_body = re.sub(r"`[^`]*`", "", body)
    for pat in GODMODE:
        if re.search(pat, scan_body, re.IGNORECASE):
            r["findings"].append(("HIGH", "god-mode language: /%s/" % pat))
            r["score"] -= 12

    # Token leak (allowlisted excluded)
    for m in TOKEN_RE.finditer(text):
        tok = m.group(0)
        if any(a in tok for a in ALLOWLIST_TOKENS):
            continue
        r["findings"].append(("CRITICAL", "possible token/secret leak: %s" % tok[:12] + "..."))
        r["score"] -= 50

    # Hidden unicode
    hidden = sum(1 for c in text if ord(c) in HIDDEN_UNICODE)
    if hidden:
        r["findings"].append(("HIGH", "hidden unicode chars: %d" % hidden))
        r["score"] -= 10

    # Exec/network (scan body only, exclude backtick-wrapped example text)
    for pat in EXEC_NET:
        if re.search(pat, scan_body):
            r["findings"].append(("HIGH", "raw exec/network pattern: /%s/" % pat))
            r["score"] -= 10
            break

    # Duplicate slug (name appears in >1 dir)
    if r["name"] and all_names.count(r["name"]) > 1:
        r["findings"].append(("HIGH", "duplicate skill name across workspace"))
        r["score"] -= 15

    # Protected namespace check
    if r["name"] and r["name"].startswith("openclaw-"):
        r["findings"].append(("INFO", "protected namespace 'openclaw-' — do not rename/merge without owner consent"))
        r["score"] -= 0

    # Decorative emoji (X∞ preserved)
    emojis = [e for e in EMOJI_RE.findall(body) if e not in PRESERVED_MARKERS and e != "∞"]
    if emojis:
        r["findings"].append(("LOW", "decorative emoji in body: %d" % len(emojis)))
        r["score"] -= min(5, len(emojis) // 20)

    r["score"] = max(0, min(100, r["score"]))
    return r


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--skills", default=WORKSPACE_DEFAULT)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    paths = []
    for name in sorted(os.listdir(args.skills)):
        p = os.path.join(args.skills, name)
        if os.path.isdir(p) and os.path.isfile(os.path.join(p, "SKILL.md")):
            paths.append(p)
    all_names = []
    for p in paths:
        t = open(os.path.join(p, "SKILL.md"), encoding="utf-8", errors="replace").read()
        m, _ = parse_frontmatter(t)
        if m and "name" in m:
            all_names.append(m["name"])

    rows = [audit_skill(p, all_names) for p in paths]

    if args.json:
        print(json.dumps(rows, indent=2, ensure_ascii=False))
        return

    print("# Skill Curator — Quality Audit (%d skills)\n" % len(rows))
    print("| # | Skill | Score | Top findings |")
    print("|---|---|---|---|")
    for i, r in enumerate(sorted(rows, key=lambda x: x["score"]), 1):
        top = "; ".join("%s:%s" % (s, f) for s, f in r["findings"][:3]) or "clean"
        print("| %d | %s | %d | %s |" % (i, r.get("name", r["dir"]), r["score"], top))

    avg = sum(r["score"] for r in rows) / len(rows)
    critical = sum(1 for r in rows for s, _ in r["findings"] if s == "CRITICAL")
    high = sum(1 for r in rows for s, _ in r["findings"] if s == "HIGH")
    print("\n**Summary**: avg score %.1f/100 | %d CRITICAL | %d HIGH | %d skills" %
          (avg, critical, high, len(rows)))
    print("\nRemediation: curator PROPOSES fixes, never auto-edits. Run with --json for pipeline.")


if __name__ == "__main__":
    main()
