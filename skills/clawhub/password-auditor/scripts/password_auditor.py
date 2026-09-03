#!/usr/bin/env python3
"""Password vault auditor — analyzes reuse, weakness, staleness, breach exposure,
and 2FA coverage WITHOUT ever storing or printing a plaintext password.

Outputs: terminal report, optional JSON, optional self-contained HTML dashboard.
Optional breach check uses HaveIBeenPwned k-anonymity (only 5 hash chars leave
the machine).

Read-only. Never writes credentials anywhere.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import json
import math
import re
import sys
import urllib.request
from collections import Counter, defaultdict
from dataclasses import dataclass, field
from datetime import datetime, timezone
from pathlib import Path
from typing import Optional

# ---------------------------------------------------------------------------
# Constants
# ---------------------------------------------------------------------------

COMMON_PASSWORDS = {
    "password", "123456", "123456789", "qwerty", "abc123", "football", "monkey",
    "letmein", "dragon", "111111", "iloveyou", "admin", "welcome", "login",
    "princess", "sunshine", "master", "trustno1", "shadow", "superman",
    "password1", "p@ssw0rd", "12345678", "qwerty123", "1q2w3e4r", "zaq12wsx",
}

LEET_MAP = str.maketrans({"@": "a", "4": "a", "3": "e", "1": "i", "l": "i",
                           "!": "i", "0": "o", "$": "s", "5": "s", "7": "t"})

KEYBOARD_ROWS = ["qwertyuiop", "asdfghjkl", "zxcvbnm", "1234567890"]
ALPHA_SEQS = ["abcdefghijklmnopqrstuvwxyz", "0123456789"]

# Small dictionary of words humans build passwords from (name/movie/place/
# fantasy tropes). Leetspeak variants are caught by normalizing, then matching.
DICTIONARY_WORDS = {
    "password", "secret", "welcome", "letmein", "sunshine", "dragon",
    "monkey", "shadow", "master", "superman", "batman", "spiderman",
    "football", "baseball", "hockey", "soccer", "liverpool", "arsenal",
    "chelsea", "starwars", "jedi", "skywalker", "gandalf", "harrypotter",
    "troubador", "troubadour", "whatever", "computer", "internet",
    "orange", "apple", "banana", "chocolate", "coffee", "summer",
    "winter", "spring", "autumn", "january", "purple", "yellow",
    "princess", "unicorn", "rainbow", "butterfly", "angel", "devil",
    "hunter", "ranger", "warrior", "ninja", "pirate", "wizard",
    "charlie", "jordan", "michael", "jackson", "jessica", "ashley",
    "matrix", "pokemon", "minecraft", "ferrari", "porsche", "mercedes",
}

CRITICAL_DOMAINS = [
    "mail", "gmail", "google", "outlook", "icloud", "protonmail", "yahoo",
    "bank", "chase", "wellsfargo", "citibank", "hsbc", "barclays", "hsbcuk",
    "amex", "americanexpress", "paypal", "revolut", "monzo", "wise",
    "dropbox", "drive.google", "onedrive", "icloud.com",
    "okta", "auth0", "login.microsoftonline", "ssa.gov", "irs.gov",
    "namecheap", "godaddy", "cloudflare",
]

SENSITIVE_DOMAINS = [
    "amazon", "ebay", "etsy", "walmart", "target", "bestbuy", "shop",
    "facebook", "instagram", "twitter", "x.com", "tiktok", "reddit", "linkedin",
    "netflix", "spotify", "steam", "playstation", "xbox", "nintendo",
    "health", "mychart", "nhs", "medicare", "gov",
]

TWOFA_CAPABLE = {
    "google.com", "gmail.com", "outlook.com", "icloud.com", "proton.me",
    "facebook.com", "instagram.com", "x.com", "twitter.com", "reddit.com",
    "linkedin.com", "amazon.com", "ebay.com", "paypal.com", "stripe.com",
    "github.com", "gitlab.com", "dropbox.com", "netflix.com", "spotify.com",
    "steampowered.com", "discord.com", "twitch.tv", "chase.com",
    "wellsfargo.com", "americanexpress.com", "coinbase.com", "binance.com",
    "cloudflare.com", "namecheap.com", "godaddy.com",
}

STALE_DAYS_HIGH = 1460   # 4 years
STALE_DAYS_MED = 730     # 2 years

DIMENSION_WEIGHTS = {"reuse": 0.35, "weakness": 0.30, "breach": 0.20,
                     "staleness": 0.10, "twofa": 0.05}

# ---------------------------------------------------------------------------
# Data model
# ---------------------------------------------------------------------------


@dataclass
class Entry:
    idx: int
    title: str
    username: str = ""
    password: str = ""
    url: str = ""
    last_modified: Optional[datetime] = None
    folder: str = ""
    # analysis results
    strength: int = 4
    guesses_bits: float = 0.0
    weak_reasons: list = field(default_factory=list)
    reuse_group: int = 0            # 0 = unique, else component id
    reuse_size: int = 1
    tier: str = "standard"          # critical | sensitive | standard
    tier_mult: float = 1.0
    breach_count: Optional[int] = None  # None = not checked
    twofa_capable: bool = False
    has_totp: bool = False
    age_days: Optional[int] = None

    @property
    def domain(self) -> str:
        m = re.search(r"([a-z0-9-]+\.[a-z0-9.-]+)", (self.url or "").lower())
        return m.group(1).rstrip(".") if m else ""

    @property
    def fp(self) -> str:
        """Non-reversible short fingerprint for safe reporting."""
        h = hashlib.sha256(self.password.encode()).hexdigest()
        return f"#{self.idx}({h[:6]})"


# ---------------------------------------------------------------------------
# Parsing / format detection
# ---------------------------------------------------------------------------

CSV_PROFILES = [
    # (name, header signature, column map)
    ("bitwarden", {"name", "login_uri", "login_username"}, {
        "title": "name", "username": "login_username", "password": "login_password",
        "url": "login_uri", "last_modified": "login_updated", "folder": "folder",
        "totp": "login_totp"}),
    ("1password", {"Title", "Username", "Password"}, {
        "title": "Title", "username": "Username", "password": "Password",
        "url": "URL", "last_modified": "Date Modified", "folder": "Folder",
        "totp": "OTPAuth"}),
    ("keepass", {"Title", "UserName", "Password"}, {
        "title": "Title", "username": "UserName", "password": "Password",
        "url": "URL", "folder": "Group", "totp": "TOTP"}),
    ("chrome", {"name", "username", "password"}, {
        "title": "name", "username": "username", "password": "password",
        "url": "url"}),
    ("firefox", {"url", "username", "password"}, {
        "title": "url", "username": "username", "password": "password",
        "url": "url"}),
]


def _parse_date(v: str) -> Optional[datetime]:
    if not v:
        return None
    v = v.strip()
    if re.fullmatch(r"\d{10}", v):
        return datetime.fromtimestamp(int(v), tz=timezone.utc)
    if re.fullmatch(r"\d{13}", v):
        return datetime.fromtimestamp(int(v) / 1000, tz=timezone.utc)
    for fmt in ("%Y-%m-%dT%H:%M:%S.%f%z", "%Y-%m-%dT%H:%M:%S%z",
                "%Y-%m-%d %H:%M:%S", "%Y-%m-%d", "%m/%d/%Y %H:%M:%S"):
        try:
            return datetime.strptime(v.replace("Z", "+0000"), fmt)
        except ValueError:
            continue
    return None


def load_vault(path: Path, fmt: str = "auto") -> tuple[list[Entry], str]:
    text = path.read_text(encoding="utf-8-sig", errors="replace")
    entries: list[Entry] = []
    detected = "generic-json"

    # JSON?
    if fmt in ("auto", "json"):
        try:
            data = json.loads(text)
            if isinstance(data, dict):
                data = data.get("items") or data.get("accounts") or []
            if isinstance(data, list) and data and isinstance(data[0], dict):
                for i, obj in enumerate(data, 1):
                    low = {k.lower(): v for k, v in obj.items()}

                    def pick(*keys):
                        for k in keys:
                            for lk, lv in low.items():
                                if k in lk and isinstance(lv, str) and lv:
                                    return lv
                        return ""

                    lm = _parse_date(pick("modified", "updated", "changed", "date"))
                    entries.append(Entry(
                        i, pick("title", "name", "label", "account") or "(untitled)",
                        pick("username", "user", "login", "email"),
                        pick("password", "secret", "pass"),
                        pick("url", "uri", "website"), lm,
                        "otpauth://" in text[:0] or bool(pick("totp", "otp"))))
                    # TOTP via otpauth URL in any field
                    if any("otpauth://" in str(v) for v in obj.values()):
                        entries[-1].has_totp = True
                return entries, detected
        except (json.JSONDecodeError, ValueError):
            pass

    # CSV
    reader = csv.DictReader(text.splitlines())
    headers = set(reader.fieldnames or [])
    profile = None
    if fmt == "auto":
        for name, sig, mapping in CSV_PROFILES:
            if sig <= headers:
                profile = (name, mapping)
                break
    else:
        for pname, _sig, mapping in CSV_PROFILES:
            if pname == fmt:
                profile = (pname, mapping)
                break
    if profile is None:
        # heuristic generic CSV
        cols = list(headers)
        mapping = {}
        for c in cols:
            cl = c.lower()
            if not mapping.get("password") and re.search(r"pass|secret", cl):
                mapping["password"] = c
            elif not mapping.get("username") and re.search(r"user|login|email|mail", cl):
                mapping["username"] = c
            elif not mapping.get("url") and re.search(r"url|uri|site|web", cl):
                mapping["url"] = c
            elif not mapping.get("title") and re.search(r"title|name|label", cl):
                mapping["title"] = c
            elif not mapping.get("last_modified") and re.search(r"date|modified|updated|changed", cl):
                mapping["last_modified"] = c
        profile = ("generic-csv", mapping)

    pname, m = profile
    detected = pname
    now = datetime.now(timezone.utc)
    export_mtime = datetime.fromtimestamp(path.stat().st_mtime, tz=timezone.utc)
    for i, row in enumerate(reader, 1):
        get = lambda k: (row.get(m.get(k, "")) or "").strip() if m.get(k) else ""
        lm = _parse_date(get("last_modified")) or export_mtime
        pwd = get("password")
        totp_field = (row.get("login_totp") or row.get("TOTP") or
                      row.get("OTPAuth") or "")
        e = Entry(i, get("title") or get("url") or "(untitled)",
                  get("username"), pwd, get("url"), lm, get("folder"),
                  has_totp=bool(totp_field) or "otpauth://" in json.dumps(row))
        e.age_days = max(0, (now - lm).days) if lm else None
        entries.append(e)
    return entries, detected


def make_demo_vault() -> list[Entry]:
    """Deterministic sample vault showcasing every finding type."""
    now = datetime.now(timezone.utc)
    days = lambda n: datetime.fromtimestamp(now.timestamp() - n * 86400, tz=timezone.utc)
    rows = [
        ("GitHub", "dev@example.com", "correct-horse-battery-staple-42", "https://github.com/login", days(200), "Dev"),
        ("Gmail", "dev@example.com", "Tr0ub4dor&3", "https://accounts.google.com", days(1900), "Email"),
        ("Chase Bank", "dev@example.com", "Summer2024!", "https://chase.com", days(1500), "Finance"),
        ("Amazon", "shopper@example.com", "Summer2024!", "https://amazon.com", days(400), "Shopping"),
        ("Netflix", "shopper@example.com", "Summer2024!", "https://netflix.com", days(300), "Media"),
        ("Old Forum", "user2001", "password123", "https://retroforum.example.net", days(2600), "Legacy"),
        ("AWS Root", "ops@example.com", "kp$9vXQ2!mZ#wR7tLp3n", "https://console.aws.amazon.com", days(90), "Work"),
        ("Reddit", "lurker@example.com", "monkey42", "https://reddit.com", days(800), "Media"),
        ("PayPal", "shopper@example.com", "dragon99", "https://paypal.com", days(1200), "Finance"),
        ("Wifi Note", "home", "Skywalker1", "note://home-network", days(100), "Home"),
    ]
    return [Entry(i, t, u, p, url, lm, folder) for i, (t, u, p, url, lm, folder)
            in enumerate(rows, 1)]


# ---------------------------------------------------------------------------
# Analysis
# ---------------------------------------------------------------------------


def classify_tier(e: Entry) -> None:
    d = e.domain
    for kw in CRITICAL_DOMAINS:
        if kw in d:
            e.tier, e.tier_mult = "critical", 3.0
            return
    for kw in SENSITIVE_DOMAINS:
        if kw in d:
            e.tier, e.tier_mult = "sensitive", 1.5
            return


def _has_sequence(s: str, minlen: int = 4) -> bool:
    low = s.lower()
    for seq in ALPHA_SEQS + [r[::-1] for r in ALPHA_SEQS] + KEYBOARD_ROWS + \
            [r[::-1] for r in KEYBOARD_ROWS]:
        for i in range(len(seq) - minlen + 1):
            if seq[i:i + minlen] in low:
                return True
    return False


def score_strength(pwd: str) -> tuple[int, float, list[str]]:
    """Return (zxcvbn-style 0-4 score, estimated bits, weakness reasons)."""
    if not pwd:
        return 0, 0.0, ["empty password"]
    reasons = []
    norm = pwd.lower().translate(LEET_MAP)

    if pwd.lower() in COMMON_PASSWORDS or norm in COMMON_PASSWORDS:
        return 0, 3.0, ["in top common-password lists"]
    # common word + trailing digits ("password123", "admin2024")
    stripped = re.sub(r"\d{1,4}$", "", pwd.lower())
    if stripped in COMMON_PASSWORDS:
        return 0, 4.0, ["common password + digits"]

    CLASS_SIZES = {r"[a-z]": 26, r"[A-Z]": 26, r"[0-9]": 10, r"[^A-Za-z0-9]": 33}
    charset = sum(size for pat, size in CLASS_SIZES.items()
                  if re.search(pat, pwd))
    bits = len(pwd) * math.log2(max(charset, 2))

    if len(pwd) < 8:
        reasons.append("shorter than 8 chars")
        bits = min(bits, 20)
    elif len(pwd) < 12:
        reasons.append("shorter than 12 chars")
    if re.fullmatch(r"[A-Za-z]+\d+[!.?@#$]?", pwd):
        reasons.append("word+digits pattern (very common shape)")
        bits = min(bits, 26.0)
    # leetspeak + dictionary word ("Tr0ub4dor&3" → "troubador...")
    leet_stripped = re.sub(r"[^a-z]", "", norm)
    if len(leet_stripped) < 24 and any(
            len(w) >= 6 and w in leet_stripped for w in DICTIONARY_WORDS):
        reasons.append("leetspeak/variant of a dictionary word")
        bits = min(bits, 28.0)
    if _has_sequence(pwd):
        reasons.append("contains keyboard/alpha sequence")
        bits *= 0.7
    if re.search(r"(.)\1{2,}", pwd):
        reasons.append("repeated characters")
        bits *= 0.8
    if re.search(r"20\d\d", pwd) and len(pwd) <= 14:
        reasons.append("contains a year")
        bits *= 0.85
    words = norm.split()
    if pwd.count(" ") >= 3 and all(w.isalpha() for w in words):
        bits = max(bits, 10 * len(words) + 6)  # passphrase credit
    bits = min(bits, 128.0)

    score = 0 if bits < 10 else 1 if bits < 25 else 2 if bits < 40 else \
        3 if bits < 60 else 4
    return score, round(bits, 1), reasons


def find_reuse(entries: list[Entry]) -> None:
    groups = defaultdict(list)
    for e in entries:
        if e.password:
            groups[hashlib.sha256(e.password.encode()).hexdigest()].append(e)
    comp = 0
    for members in groups.values():
        if len(members) >= 2:
            comp += 1
            for e in members:
                e.reuse_group, e.reuse_size = comp, len(members)


def check_breaches(entries: list[Entry], timeout: float = 15.0) -> tuple[int, int]:
    """HIBP k-anonymity range API. Returns (checked, matched)."""
    checked = matched = 0
    by_prefix: dict[str, list[Entry]] = defaultdict(list)
    for e in entries:
        if e.password:
            h = hashlib.sha1(e.password.encode()).hexdigest().upper()
            by_prefix[h[:5]].append(e)
    for prefix, members in by_prefix.items():
        try:
            req = urllib.request.Request(
                f"https://api.pwnedpasswords.com/range/{prefix}",
                headers={"User-Agent": "password-auditor-skill"})
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                body = resp.read().decode()
        except Exception as exc:
            print(f"  ! breach check failed for prefix {prefix}: {exc}",
                  file=sys.stderr)
            continue
        suffixes = {}
        for line in body.splitlines():
            suf, _, cnt = line.partition(":")
            suffixes[suf.strip()] = int(cnt or 0)
        for e in members:
            h = hashlib.sha1(e.password.encode()).hexdigest().upper()
            e.breach_count = suffixes.get(h[5:], 0)
            checked += 1
            matched += 1 if e.breach_count > 0 else 0
    return checked, matched


def analyze(entries: list[Entry], now: Optional[datetime] = None) -> dict:
    now = now or datetime.now(timezone.utc)
    for e in entries:
        classify_tier(e)
        e.strength, e.guesses_bits, e.weak_reasons = score_strength(e.password)
        d = e.domain.split(".")[0] if e.domain else ""
        dom2 = ".".join(e.domain.split(".")[-2:]) if "." in e.domain else ""
        e.twofa_capable = dom2 in TWOFA_CAPABLE
        if e.last_modified:
            e.age_days = max(0, (now - e.last_modified).days)
    find_reuse(entries)

    n = len(entries) or 1
    findings: dict[str, list] = {"reuse": [], "weakness": [], "staleness": [],
                                 "breach": [], "twofa": []}

    for e in entries:
        if e.reuse_size >= 2:
            findings["reuse"].append({
                "entry": e.idx, "title": e.title, "tier": e.tier,
                "shared_with": e.reuse_size - 1,
                "action": f"Rotate immediately — same password on {e.reuse_size - 1} other entries"})
        if e.strength <= 1 and e.password:
            findings["weakness"].append({
                "entry": e.idx, "title": e.title, "tier": e.tier,
                "score": e.strength, "reasons": e.weak_reasons,
                "action": "Replace with a generated 16+ char password"})
        if e.age_days is not None and e.age_days > STALE_DAYS_HIGH:
            findings["staleness"].append({
                "entry": e.idx, "title": e.title, "tier": e.tier,
                "age_years": round(e.age_days / 365.25, 1),
                "action": "Rotate — unchanged for over 4 years"})
        if e.breach_count:
            findings["breach"].append({
                "entry": e.idx, "title": e.title, "tier": e.tier,
                "breach_count": e.breach_count,
                "action": f"PWNED — appears {e.breach_count:,}x in breach corpora; rotate NOW"})
        if e.twofa_capable and not e.has_totp and e.password:
            findings["twofa"].append({
                "entry": e.idx, "title": e.title, "tier": e.tier,
                "action": "Site supports 2FA but no TOTP stored — enroll"})

    def penalty(kind: str, cap: float = 40.0) -> float:
        mult = {"reuse": 6.0, "weakness": 5.0, "breach": 12.0,
                "staleness": 1.5, "twofa": 1.0}[kind]
        tier_boost = {"critical": 3.0, "sensitive": 1.5, "standard": 1.0}
        total = 0.0
        for f in findings[kind]:
            total += mult * tier_boost.get(f.get("tier", "standard"), 1.0)
        return min(total / n * 10, cap)

    sub = {k: max(0.0, round(100 - penalty(k) * (100 / 40), 1))
           for k in DIMENSION_WEIGHTS}
    score = round(sum(sub[k] * w for k, w in DIMENSION_WEIGHTS.items()), 1)
    score = max(0, min(100, score))

    # Remediation plan: worst risk first
    prio = []
    for kind, items in findings.items():
        for f in items:
            tb = {"critical": 3.0, "sensitive": 1.5, "standard": 1.0}[f.get("tier", "standard")]
            risk = {"reuse": 6, "weakness": 5, "breach": 12,
                    "staleness": 1.5, "twofa": 1}[kind] * tb
            prio.append((risk, kind, f))
    prio.sort(key=lambda x: -x[0])

    return {
        "total_entries": len(entries),
        "with_passwords": sum(1 for e in entries if e.password),
        "score": score,
        "subscores": sub,
        "findings": {k: v for k, v in findings.items() if v},
        "plan": [{"priority": i + 1, "dimension": kind,
                  "risk": round(r, 1), **f}
                 for i, (r, kind, f) in enumerate(prio[:20])],
        "largest_reuse_component": max((e.reuse_size for e in entries), default=1),
        "avg_strength": round(sum(e.strength for e in entries) / n, 2),
    }


# ---------------------------------------------------------------------------
# Reports
# ---------------------------------------------------------------------------

BAR = "█"


def render_report(res: dict, fmt: str, breach_checked: tuple) -> str:
    lines = []
    a = lines.append
    a("=" * 62)
    a(" PASSWORD VAULT AUDIT")
    a("=" * 62)
    a(f" Format detected      : {fmt}")
    a(f" Entries              : {res['total_entries']} ({res['with_passwords']} with passwords)")
    if any(e for e in [breach_checked] if breach_checked[0]):
        a(f" Breach check         : {breach_checked[0]} checked, "
          f"{breach_checked[1]} FOUND IN BREACHES")
    a("")
    sc = res["score"]
    bar_len = int(sc / 5)
    a(f" SECURITY SCORE : {sc}/100  [{BAR * bar_len}{'░' * (20 - bar_len)}]")
    grade = "A" if sc >= 90 else "B" if sc >= 75 else "C" if sc >= 60 else \
        "D" if sc >= 40 else "F"
    a(f" Grade          : {grade}")
    a("")
    a(" Sub-scores:")
    for k, v in res["subscores"].items():
        a(f"   {k:<11} {v:>6.1f}/100")
    a("")
    f = res["findings"]
    a(" FINDINGS")
    a(f"   Reused passwords   : {len(f.get('reuse', []))} entries "
      f"(largest group shares {res['largest_reuse_component']} accounts)")
    a(f"   Weak passwords     : {len(f.get('weakness', []))}")
    if breach_checked[0]:
        a(f"   Breach-exposed     : {len(f.get('breach', []))}")
    a(f"   Stale (>4y)        : {len(f.get('staleness', []))}")
    a(f"   2FA opportunities  : {len(f.get('twofa', []))}")
    a("")
    if res["plan"]:
        a(" TOP REMEDIATION ACTIONS (do these first)")
        for p in res["plan"][:10]:
            tier_tag = f"[{p['tier'].upper()}]" if p.get("tier") else ""
            a(f"  {p['priority']:>2}. {tier_tag} #{p['entry']} {p['title'][:34]:<34} "
              f"→ {p['action'][:52]}")
    else:
        a(" No findings. Vault looks healthy — re-audit quarterly.")
    a("")
    a(" ⚠  Remember: delete the vault export from disk after this audit.")
    a("=" * 62)
    return "\n".join(lines)


HTML_TEMPLATE = """<!DOCTYPE html>
<html lang="en"><head><meta charset="utf-8">
<title>Password Audit Dashboard</title>
<style>
 body{{font-family:-apple-system,Segoe UI,Roboto,sans-serif;background:#0d1117;color:#c9d1d9;margin:0;padding:2rem}}
 h1,h2{{color:#f0f6fc}} .card{{background:#161b22;border:1px solid #30363d;border-radius:8px;padding:1.2rem;margin:1rem 0}}
 .score{{font-size:3rem;font-weight:700;color:{score_color}}} .grade{{font-size:2rem;margin-left:1rem}}
 .bar{{height:10px;background:#21262d;border-radius:5px;overflow:hidden;margin:.4rem 0 1rem}}
 .bar>div{{height:100%;background:{score_color};width:{score_pct}%}}
 table{{width:100%;border-collapse:collapse;font-size:.9rem}} th,td{{text-align:left;padding:.45rem .6rem;border-bottom:1px solid #21262d}}
 th{{color:#8b949e;text-transform:uppercase;font-size:.75rem;letter-spacing:.05em}}
 .tag{{padding:.1rem .5rem;border-radius:10px;font-size:.72rem;font-weight:600}}
 .critical{{background:#da3633;color:#fff}} .sensitive{{background:#bb8009;color:#fff}} .standard{{background:#30363d;color:#8b949e}}
 .p0{{color:#f85149;font-weight:600}}
 .muted{{color:#8b949e;font-size:.85rem}}
</style></head><body>
<h1>🔐 Password Audit Dashboard</h1>
<p class="muted">Generated {date} · {entries} entries · no plaintext passwords in this file</p>
<div class="card">
 <span class="score">{score}</span><span class="grade">/100 · Grade {grade}</span>
 <div class="bar"><div></div></div>
 <table><tr><th>Dimension</th><th>Sub-score</th></tr>
 {subrows}</table>
</div>
<div class="card"><h2>Findings</h2><table>
 <tr><th>#</th><th>Severity</th><th>Dimension</th><th>Entry</th><th>Action</th></tr>
 {finding_rows}</table></div>
<div class="card"><h2>Remediation Plan (top 15)</h2><table>
 <tr><th>Priority</th><th>Entry</th><th>Dimension</th><th>Action</th></tr>
 {plan_rows}</table></div>
<div class="card"><h2>Next steps</h2>
<ol><li>Rotate every entry marked <b>pwned</b> or reused on critical sites first.</li>
<li>Enable TOTP 2FA where flagged.</li>
<li>Replace weak passwords with generated ones (16+ chars).</li>
<li>Delete the vault export from disk. Re-run this audit quarterly.</li></ol></div>
</body></html>"""


def render_html(res: dict) -> str:
    color = "#3fb950" if res["score"] >= 75 else "#d29922" if res["score"] >= 50 else "#f85149"
    subrows = "".join(
        f"<tr><td>{k}</td><td>{v}/100</td></tr>" for k, v in res["subscores"].items())
    frows = []
    for kind, items in res["findings"].items():
        for f in items:
            sev = {"breach": "P0", "reuse": "P1", "weakness": "P1",
                   "staleness": "P3", "twofa": "P3"}[kind]
            sevcls = "p0" if sev == "P0" else ""
            tag = f.get("tier", "")
            tagcls = tag if tag in ("critical", "sensitive") else "standard"
            frows.append(f"<tr><td>{f['entry']}</td><td class='{sevcls}'>{sev}</td>"
                         f"<td>{kind}</td><td>{f['title']} "
                         f"<span class='tag {tagcls}'>{tagcls}</span></td>"
                         f"<td>{f['action']}</td></tr>")
    prows = "".join(
        f"<tr><td>{p['priority']}</td><td>#{p['entry']} {p['title']}</td>"
        f"<td>{p['dimension']}</td><td>{p['action']}</td></tr>"
        for p in res["plan"][:15])
    return HTML_TEMPLATE.format(
        date=datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M UTC"),
        entries=res["total_entries"], score=res["score"],
        grade="A" if res["score"] >= 90 else "B" if res["score"] >= 75 else
        "C" if res["score"] >= 60 else "D" if res["score"] >= 40 else "F",
        score_color=color, score_pct=res["score"], subrows=subrows,
        finding_rows="".join(frows) or "<tr><td colspan=5>No findings</td></tr>",
        plan_rows=prows or "<tr><td colspan=4>Nothing to do 🎉</td></tr>")


def compare(old: dict, new: dict) -> str:
    lines = [" VAULT AUDIT COMPARISON", "-" * 50]
    for label, o, n in (("score", old["score"], new["score"]),
                        ("reused entries", len(old["findings"].get("reuse", [])),
                         len(new["findings"].get("reuse", []))),
                        ("weak entries", len(old["findings"].get("weakness", [])),
                         len(new["findings"].get("weakness", []))),
                        ("breached", len(old["findings"].get("breach", [])),
                         len(new["findings"].get("breach", []))),
                        ("2FA gaps", len(old["findings"].get("twofa", [])),
                         len(new["findings"].get("twofa", [])))):
        d = n - o if isinstance(o, (int, float)) else 0
        arrow = "↑" if d > 0 else "↓" if d < 0 else "="
        lines.append(f" {label:<16} {o:>8} → {n:<8} {arrow}")
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main() -> int:
    ap = argparse.ArgumentParser(
        description="Audit password vault exports without storing passwords.")
    ap.add_argument("--vault", type=Path, help="vault export (CSV or JSON)")
    ap.add_argument("--format", default="auto",
                    choices=["auto", "json", "bitwarden", "1password",
                             "keepass", "chrome", "firefox"])
    ap.add_argument("--demo", action="store_true", help="use built-in demo vault")
    ap.add_argument("--check-breaches", action="store_true",
                    help="check HIBP k-anonymity API (5 hash chars only)")
    ap.add_argument("--json", type=Path, help="write JSON report")
    ap.add_argument("--html", type=Path, help="write HTML dashboard")
    ap.add_argument("--compare", nargs=2, type=Path, metavar=("OLD", "NEW"),
                    help="diff two previous JSON reports")
    ap.add_argument("--twofa-list", type=Path,
                    help="custom 2FA-capable domains file (one per line)")
    args = ap.parse_args()

    if args.compare:
        old = json.loads(args.compare[0].read_text())
        new = json.loads(args.compare[1].read_text())
        print(compare(old, new))
        return 0

    if args.demo:
        entries = make_demo_vault()
        fmt = "demo"
    elif args.vault:
        entries, fmt = load_vault(args.vault, args.format)
    else:
        ap.error("provide --vault or --demo")
        return 2

    if args.twofa_list:
        TWOFA_CAPABLE.update(
            d.strip().lower() for d in args.twofa_list.read_text().splitlines()
            if d.strip() and not d.startswith("#"))

    if not entries:
        print("No entries found in vault.", file=sys.stderr)
        return 1

    breach_stats = (0, 0)
    if args.check_breaches:
        print("Checking breaches via HIBP k-anonymity (sending only 5-char "
              "hash prefixes)...", file=sys.stderr)
        breach_stats = check_breaches(entries)

    res = analyze(entries)
    print(render_report(res, fmt, breach_stats))

    if args.json:
        safe = json.loads(json.dumps(res))  # already password-free by construction
        args.json.write_text(json.dumps(safe, indent=2))
        print(f"\nJSON report  → {args.json}")
    if args.html:
        args.html.write_text(render_html(res))
        print(f"HTML report  → {args.html}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
