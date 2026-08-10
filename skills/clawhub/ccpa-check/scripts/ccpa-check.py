#!/usr/bin/env python3
"""
CCPA Check — CCPA/CPRA compliance check (free skill + cloud compliance engine)

Based on the California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.)
and the California Privacy Rights Act (CPRA, effective Jan 1, 2023).
Covers 12 core checks across applicability, consumer rights, opt-out, service
providers, records, and security.

This skill is free to install. Check items are served by the CQDev
cloud compliance engine (compliancehub.cn); scoring and quota are computed in
the cloud. Before first use, register for a free API Key at compliancehub.cn:
  - Get a Key: run `python3 scripts/ccpa-check.py --login` (register/login in
    terminal; on success the Key is saved to your private store
    ~/.config/compliancehub/ccpa-check.key with 0600 perms)
  - Or open the account center: https://compliancehub.cn/account.html?skill=ccpa-check
  - Or pass it via env: export COMPLIANCEHUB_API_KEY=<your-key>

Flow:
  1. Load API Key (env COMPLIANCEHUB_API_KEY, or ~/.config/compliancehub/ccpa-check.key)
  2. Fetch check items from the cloud rule-library API (public read, single source)
  3. Interactively collect per-item compliance status (y=pass / n=fail / na=n/a)
  4. Submit to the cloud evaluate endpoint; the cloud scores and returns report data
  5. Render a professional report locally

Uses only Python built-in urllib — zero third-party dependencies. HTTPS + Bearer
transport for the key; no hardcoding, no covert exfiltration.
"""
import sys, os, json, argparse, datetime, ssl, getpass
import urllib.request
import urllib.error

sys.path.insert(0, os.path.dirname(__file__))

# ─── Cloud endpoints ──────────────────────────────────────────────
# API_BASE is PINNED to the operator's official compliance cloud and is
# intentionally NOT overridable via an environment variable. Allowing a
# COMPLIANCEHUB_API_BASE override would let a malicious environment redirect
# users' compliance answers AND their API Key (sent as a Bearer token) to an
# attacker-controlled server — flagged by security scanners as a "redirectable
# cloud endpoint" / credential-exfiltration chain. The destination is fixed.
API_BASE = "https://compliancehub.cn"
SKILL_SLUG = os.path.basename(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
RULES_URL = f"{API_BASE}/api/v1/rules/{SKILL_SLUG}/rules"        # public read: check items
EVALUATE_URL = f"{API_BASE}/api/v1/rules/{SKILL_SLUG}/evaluate"  # auth: scoring
ACCOUNT_PAGE = f"{API_BASE}/account.html?skill={SKILL_SLUG}"      # unified account center
REGISTER_PAGE = ACCOUNT_PAGE                                      # alias
AUTH_URL = f"{API_BASE}/api/v1/auth/register"
LOGIN_URL = f"{API_BASE}/api/v1/auth/login"
KEYS_URL = f"{API_BASE}/api/v1/auth/keys"


def _skill_version():
    pkg = os.path.join(os.path.dirname(__file__), "..", "package.json")
    try:
        if os.path.isfile(pkg):
            with open(pkg, encoding="utf-8") as f:
                return json.load(f).get("version", "2.0.0")
    except Exception:
        pass
    return "2.0.0"


def _ua():
    return f"{SKILL_SLUG}/{_skill_version()}"


# ─── API Key resolution ──────────────────────────────────────────

def _key_path():
    """Private, per-user key store OUTSIDE the skill directory.

    The API Key is written here (mode 0600) rather than inside the skill
    folder, so it is never committed to source control or shared with the
    workspace. This addresses the 'plaintext API key in shared/source-
    controlled workspace' concern raised in security review.
    """
    d = os.path.join(os.path.expanduser("~"), ".config", "compliancehub")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"{SKILL_SLUG}.key")


def load_api_key():
    """Resolve API Key precedence:
      1) env COMPLIANCEHUB_API_KEY (ephemeral, safest)
      2) private store ~/.config/compliancehub/<slug>.key (mode 0600)
      3) legacy references/api_key.md (read-only, kept for backward compat)
    """
    env_key = os.environ.get("COMPLIANCEHUB_API_KEY")
    if env_key and env_key.strip():
        return env_key.strip()
    p = _key_path()
    if os.path.isfile(p):
        try:
            with open(p, encoding="utf-8") as f:
                s = f.read().strip()
                if s:
                    return s
        except Exception:
            pass
    # legacy fallback (read-only)
    cand = os.path.join(os.path.dirname(__file__), "..", "references", "api_key.md")
    if os.path.isfile(cand):
        try:
            with open(cand, encoding="utf-8") as f:
                for line in f:
                    s = line.strip()
                    if not s or s.startswith("#"):
                        continue
                    if s.lower().startswith("key") and "=" in s:
                        s = s.split("=", 1)[1].strip()
                    if s.startswith("sk_live_") or len(s) >= 16:
                        return s
        except Exception:
            pass
    return None


def require_key():
    key = load_api_key()
    if key:
        return key
    msg = {
        "error": "missing_api_key",
        "message": "This check calls the CQDev cloud compliance engine and needs a free API Key.",
        "register_page": REGISTER_PAGE,
        "cli": f"python3 scripts/{os.path.basename(__file__)} --login",
            "howto": (
            "Option 1 (recommended): run `python3 scripts/%s --login`, enter your email and "
            "password in the terminal, and the Key is written to your private key store "
            "(~/.config/compliancehub/%s.key, mode 0600) automatically; "
            "Option 2: open %s to register in the browser, then run `--login` to fetch the Key, "
            "or export env COMPLIANCEHUB_API_KEY; then run this check again."
            % (os.path.basename(__file__), SKILL_SLUG, REGISTER_PAGE)
        ),
    }
    print(json.dumps(msg, ensure_ascii=False, indent=2))
    sys.exit(2)


# ─── Account & Key acquisition (terminal register/login, auto-write) ─

def _api_json(method, url, payload=None, token=None):
    """Minimal JSON request: returns (status, data)."""
    body = json.dumps(payload).encode("utf-8") if payload is not None else None
    headers = {"Content-Type": "application/json", "User-Agent": _ua()}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    req = urllib.request.Request(url, data=body, headers=headers, method=method)
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            return resp.status, json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        try:
            return e.code, json.loads(e.read().decode("utf-8", "ignore"))
        except Exception:
            return e.code, {}
    except Exception:
        return 0, {}


def write_key_to_file(key):
    """Persist the API Key to a private, per-user store (~/.config/compliancehub/<slug>.key)
    with 0600 permissions — OUTSIDE the skill directory, so it is never committed to source
    control or shared with the workspace. Returns the path."""
    p = _key_path()
    with open(p, "w", encoding="utf-8") as f:
        f.write(key.strip() + "\n")
    try:
        os.chmod(p, 0o600)
    except Exception:
        pass
    return p


def cmd_auth():
    """Register or login in the terminal, then fetch and save the API Key.

    Tries login first; if the account does not exist (401) falls back to register.
    Runs ONLY on the explicit `--login` command. After successful auth, creates a new
    Key with the JWT (plaintext returned once) and saves it to the private key store
    (~/.config/compliancehub/<slug>.key, 0600) — ordinary API-key persistence, not
    agent installation or auto-start.
    """
    print(f"\n🔐 {SKILL_SLUG} · CQDev account (free, 100 calls per Key)")
    email = input("Email: ").strip()
    password = getpass.getpass("Password: ")
    if not email or not password:
        print("❌ Email and password cannot be empty")
        sys.exit(1)

    st, data = _api_json("POST", LOGIN_URL, {"email": email, "password": password})
    if st == 200:
        jwt = (data.get("data") or {}).get("access_token")
        print("✅ Login successful")
    else:
        print("   No account found, registering a new one…")
        name = input("Name (optional, Enter to skip): ").strip() or None
        org = input("Organization (optional, Enter to skip): ").strip() or None
        st2, data2 = _api_json("POST", AUTH_URL, {
            "email": email, "password": password,
            "name": name, "org_name": org,
        })
        if st2 != 200:
            err = (data2.get("error")) or (data2.get("detail")) or "registration failed"
            print(f"❌ {err}")
            sys.exit(1)
        key = (data2.get("data") or {}).get("api_key")
        if not key:
            print("❌ Registered but no Key returned; please retry on the website")
            sys.exit(1)
        path = write_key_to_file(key)
        print(f"✅ Registered. API Key saved (mode 0600) to: {path}")
        print(f"   Manage your keys at: {ACCOUNT_PAGE}")
        _after_auth_hint()
        return

    st3, data3 = _api_json("POST", KEYS_URL, {}, token=jwt)
    if st3 != 200:
        err = (data3.get("error")) or (data3.get("detail")) or "failed to create key"
        print(f"❌ {err}")
        sys.exit(1)
    key = (data3.get("data") or {}).get("api_key")
    if not key:
        print("❌ No Key returned; please retry on the website")
        sys.exit(1)
    path = write_key_to_file(key)
    print(f"✅ New API Key saved (mode 0600) to: {path}")
    print(f"   Manage your keys at: {ACCOUNT_PAGE}")
    _after_auth_hint()


def _after_auth_hint():
    print("\n💡 Now just run the full check (free cloud scoring, 100 calls per Key):")
    print(f"   python3 scripts/{os.path.basename(__file__)} --format html -o report.html")


# ─── Rule data source (cloud rule-library API, public read) ──────

def fetch_rules():
    """Fetch ccpa-check items from the cloud rule library (public, no Key needed).

    Returns a mapped item list (id=item_key / name / desc / ref / category /
    recommendation); returns None on any error so the caller falls back to the
    built-in CHECK_ITEMS.
    """
    try:
        ctx = ssl.create_default_context()
        req = urllib.request.Request(RULES_URL, headers={"User-Agent": _ua()})
        with urllib.request.urlopen(req, context=ctx, timeout=10) as resp:
            if resp.status != 200:
                return None
            payload = json.loads(resp.read().decode("utf-8"))
        if not payload.get("success"):
            return None
        raw_items = payload.get("items") or []
        if not raw_items:
            return None
        items = []
        for it in raw_items:
            items.append({
                "id": it.get("item_key"),
                "name": it.get("name"),
                "desc": it.get("question") or it.get("description") or "",
                "ref": it.get("legal_ref") or "",
                "category": it.get("category_name") or "",
                "recommendation": it.get("recommendation") or "",
            })
        return items
    except Exception:
        return None


# ─── Check items (fallback data source) ─────────────────────────

CHECK_ITEMS = [
    {"id": "applicability_business", "name": "Business Applicability", "desc": "Does your business meet the CCPA 'business' threshold (revenue > $25M; buys/sells/shares PI of ≥100k consumers; or ≥50% revenue from selling/sharing PI)?", "ref": "CCPA §1798.140(d)", "category": "A. Applicability & Notice"},
    {"id": "notice_disclosure", "name": "Privacy Notice at Collection", "desc": "At or before collection, do you disclose categories of PI collected and purposes of use?", "ref": "CCPA §1798.100(b)", "category": "A. Applicability & Notice"},
    {"id": "consumer_rights", "name": "Consumer Rights Fulfillment", "desc": "Do you support know/delete/correct rights with working request channels?", "ref": "CCPA §1798.100/105/106", "category": "B. Consumer Rights"},
    {"id": "identity_verification", "name": "Identity Verification", "desc": "Do you verify the consumer's identity for rights requests without undue burden?", "ref": "CCPA §1798.145(i)", "category": "B. Consumer Rights"},
    {"id": "response_timeliness", "name": "Response Timeliness", "desc": "Do you respond to verifiable requests within 45 calendar days (or one permitted extension)?", "ref": "CCPA §1798.130(a)(2)", "category": "B. Consumer Rights"},
    {"id": "non_discrimination", "name": "Non-Discrimination", "desc": "Do you refrain from discriminating against consumers who exercise their rights?", "ref": "CCPA §1798.125", "category": "B. Consumer Rights"},
    {"id": "opt_out_mechanism", "name": "Right to Opt-Out", "desc": "Do you provide a 'Do Not Sell or Share' link and honor opt-out (incl. GPC signals)?", "ref": "CCPA §1798.120", "category": "C. Opt-Out & Data Control"},
    {"id": "sensitive_pi_handling", "name": "Sensitive PI Handling", "desc": "For sensitive PI, do you limit use to permitted purposes and offer a right to limit use?", "ref": "CPRA §1798.121", "category": "C. Opt-Out & Data Control"},
    {"id": "data_sale_management", "name": "Sale/Sharing of PI", "desc": "If you sell/share PI, is it disclosed with opt-out and bounded by contract?", "ref": "CCPA §1798.140(t)/115", "category": "C. Opt-Out & Data Control"},
    {"id": "service_provider_mgmt", "name": "Service Provider Contracts", "desc": "Do contracts with service providers/contractors prohibit secondary use of PI?", "ref": "CCPA §1798.140(ag)", "category": "D. Service Providers & Records"},
    {"id": "record_keeping", "name": "Record Keeping", "desc": "Do you keep records of consumer requests and how they were handled (≥24 months)?", "ref": "CCPA §1798.130(a)", "category": "D. Service Providers & Records"},
    {"id": "data_security_measures", "name": "Reasonable Security", "desc": "Do you maintain reasonable security procedures appropriate to the nature of the PI?", "ref": "CCPA §1798.81.5", "category": "E. Data Security"},
]


# ─── Interactive collection ──────────────────────────────────────

def collect_responses(items):
    """Collect per-item compliance status interactively (y=pass / n=fail / na=n/a)."""
    responses = []
    total = len(items)
    print(f"\n📋 CCPA/CPRA Compliance Check — {total} items")
    print("   Answer each item's actual status (y=pass / n=fail / na=not applicable)\n")
    for i, item in enumerate(items):
        idx = i + 1
        while True:
            ans = input(f"  [{idx}/{total}] {item['name']} [{item['ref']}]\n"
                        f"        {item['desc']}\n"
                        f"        (y/n/na) > ").strip().lower()
            if ans in ('y', 'n', 'na'):
                if ans == 'na':
                    responses.append({**item, "status": "na"})
                else:
                    responses.append({**item, "status": "pass" if ans == 'y' else "fail"})
                break
            print("        please enter y, n or na")
    return responses


def build_submission(responses):
    """Convert interactive results to cloud evaluate request items (na excluded)."""
    items = []
    for r in responses:
        if r["status"] == "na":
            continue
        items.append({
            "item_key": r["id"],
            "passed": r["status"] == "pass",
            "evidence": None,
        })
    return items


# ─── Cloud scoring ───────────────────────────────────────────────

def call_evaluate(key, submission):
    """Call the cloud evaluate endpoint; returns (data, error)."""
    payload = {"items": submission, "context": None}
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(
        EVALUATE_URL,
        data=body,
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {key}",
            "User-Agent": _ua(),
        },
        method="POST",
    )
    ctx = ssl.create_default_context()
    try:
        with urllib.request.urlopen(req, context=ctx, timeout=15) as resp:
            if resp.status != 200:
                return None, f"cloud returned HTTP {resp.status}"
            return json.loads(resp.read().decode("utf-8")), None
    except urllib.error.HTTPError as e:
        detail = ""
        try:
            detail = json.loads(e.read().decode("utf-8", "ignore")).get("detail", "")
        except Exception:
            pass
        if e.code == 401:
            return None, "API Key invalid or unauthorized; run `python3 scripts/%s --login` to fetch a new one (or get it at %s)" % (os.path.basename(__file__), REGISTER_PAGE)
        if e.code == 403:
            return None, f"free quota exhausted: {detail} (log in at %s to upgrade or create a new key)" % REGISTER_PAGE
        if e.code == 404:
            return None, f"rule library not open: {detail}"
        return None, f"cloud error HTTP {e.code}: {detail}"
    except Exception as e:
        return None, f"cloud call failed: {e}"


# ─── Report rendering ────────────────────────────────────────────

def render_text(data, items):
    s = data
    lines = [
        "=" * 60,
        "  CCPA/CPRA Compliance Check Report (cloud-scored)",
        "  Law: California Consumer Privacy Act (CCPA) & CPRA amendment",
        f"  Engine version: {s.get('version', '?')}",
        f"  Compliance score: {s.get('score')}/100",
        "=" * 60,
        f"  Overview: {s.get('total_items')} items counted | ✅ Pass {s.get('passed_count')} | ❌ Fail {s.get('failed_count')} | Free quota left {s.get('quota_remaining')}",
        "=" * 60,
    ]
    current_cat = ""
    for r in items:
        if r.get("category") != current_cat:
            current_cat = r.get("category", "")
            lines.append(f"\n  ── {current_cat} ──")
        icon = "✅" if r.get("passed") else "❌"
        lines.append(f"\n  {icon} [{r.get('item_key')}] {r.get('name')}")
        lines.append(f"    Status: {'Pass' if r.get('passed') else 'Fail'}")
        if r.get("legal_ref"):
            lines.append(f"    Authority: {r.get('legal_ref')}")
        if r.get("recommendation"):
            lines.append(f"    Recommendation: {r.get('recommendation')}")
    lines.append("=" * 60)
    lines.append("\n💡 Disclaimer: This report is generated by the CQDev cloud compliance engine for reference only and does not constitute legal advice.")
    return "\n".join(lines)


def render_html(data, items):
    s = data
    score = s.get("score", 0)
    color = "#4caf50" if score >= 80 else "#ff9800" if score >= 60 else "#f44336"
    rows = ""
    current_cat = ""
    for r in items:
        if r.get("category") != current_cat:
            current_cat = r.get("category", "")
            rows += f'<tr class="category-row"><td colspan="5">{current_cat}</td></tr>\n'
        icon = "✅" if r.get("passed") else "❌"
        cls = "pass" if r.get("passed") else "fail"
        rec = r.get("recommendation") or "Keep it up"
        rows += f"""<tr class="{cls}"><td>{icon}</td><td>{r.get('name')}</td><td>{r.get('legal_ref') or ''}</td><td>{cls.upper()}</td><td>{rec}</td></tr>\n"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8"><title>CCPA/CPRA Compliance Check Report</title>
<style>
body{{font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;max-width:960px;margin:2rem auto;padding:0 1rem;color:#333}}
h1{{border-bottom:2px solid #2563eb;padding-bottom:.5rem}}
.score-card{{background:linear-gradient(135deg,#2563eb,#1d4ed8);color:#fff;padding:2rem;border-radius:12px;text-align:center;margin:1.5rem 0}}
.score{{font-size:4rem;font-weight:700}}
.summary{{display:flex;gap:2rem;justify-content:center;margin-top:1rem}}
.summary div{{text-align:center;font-size:1.2rem}}
table{{width:100%;border-collapse:collapse;margin-top:1.5rem}}
th{{background:#f1f5f9;text-align:left;padding:.75rem;border-bottom:2px solid #e2e8f0}}
td{{padding:.75rem;border-bottom:1px solid #e2e8f0}}
tr.pass td:first-child{{color:#4caf50}}
tr.fail td:first-child{{color:#f44336}}
tr.category-row td{{background:#dbeafe;font-weight:600;color:#1d4ed8}}
.note{{color:#94a3b8;margin-top:2rem;font-size:.85rem}}
</style></head>
<body>
<h1>CCPA/CPRA Compliance Check Report</h1>
<p>Law: California Consumer Privacy Act (CCPA) &amp; California Privacy Rights Act (CPRA)</p>
<p>Engine version: {s.get('version','?')} ｜ Free quota left: {s.get('quota_remaining')}</p>
<div class="score-card"><div class="score">{score}</div><div>Compliance score / 100</div>
<div class="summary"><div>✅ Pass<br><b>{s.get('passed_count')}</b></div><div>❌ Fail<br><b>{s.get('failed_count')}</b></div><div>Items<br><b>{s.get('total_items')}</b></div></div></div>
<table><thead><tr><th></th><th>Check</th><th>Authority</th><th>Status</th><th>Recommendation</th></tr></thead><tbody>{rows}</tbody></table>
<p class="note">This report is generated by the CQDev cloud compliance engine for reference only and does not constitute legal advice.</p>
</body></html>"""


def generate_report(payload, format="text"):
    """Render report from cloud response. payload is the full evaluate JSON."""
    data = payload.get("data", {}) if isinstance(payload, dict) else {}
    items = data.get("items", [])
    if format == "json":
        return json.dumps(payload, ensure_ascii=False, indent=2)
    elif format == "html":
        return render_html(data, items)
    return render_text(data, items)


# ─── Main entry ──────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(description="CCPA/CPRA compliance check (free skill + cloud engine)")
    parser.add_argument("--non-interactive", action="store_true", help="free preview mode (list items, no scoring)")
    parser.add_argument("--non-interactive-json", action="store_true", help="free preview JSON mode (for sandbox case generation)")
    parser.add_argument("--login", "--auth", dest="auth", action="store_true",
                        help="register/login CQDev account in terminal; on success the free API Key is saved locally (~/.config/compliancehub/, 0600) for future runs")
    parser.add_argument("--format", "-f", choices=["text", "json", "html"], default="text")
    parser.add_argument("--output", "-o", help="report output file path")
    args = parser.parse_args()

    if args.auth:
        cmd_auth()
        return

    # Check items come from the cloud rule library; fall back to built-in CHECK_ITEMS on failure
    items = fetch_rules() or CHECK_ITEMS

    # ── free preview JSON (no Key) ──
    if args.non_interactive_json:
        preview_data = [{
            "id": item["id"], "name": item["name"],
            "desc": item["desc"], "ref": item["ref"], "category": item["category"],
        } for item in items]
        print(json.dumps({
            "preview": True,
            "total_items": len(items),
            "free": True,
            "needs_api_key": True,
            "register_page": REGISTER_PAGE,
            "message": "This check is free, but scoring runs on the CQDev cloud engine and needs a free API Key.",
            "preview_items": preview_data,
        }, ensure_ascii=False, indent=2))
        return

    # ── free preview (list items, no scoring, no Key) ──
    if args.non_interactive:
        print(f"\n🔍 Free preview mode — {len(items)} items; scoring needs a free API Key\n")
        current_cat = ""
        for it in items:
            if it.get("category") != current_cat:
                current_cat = it.get("category", "")
                print(f"\n  ── {current_cat} ──")
            print(f"  • [{it['id']}] {it['name']}  [{it['ref']}]")
            print(f"      {it['desc']}")
        print(f"\n💡 Scoring runs on the cloud engine. Get a free API Key: {REGISTER_PAGE}")
        return

    # ── full check: needs Key ──
    key = require_key()
    responses = collect_responses(items)
    submission = build_submission(responses)
    if not submission:
        print("❌ No countable items (all marked not applicable).")
        sys.exit(1)

    print("\n⏳ Submitting to cloud compliance engine for scoring…")
    payload, err = call_evaluate(key, submission)
    if err:
        print(f"❌ {err}")
        sys.exit(1)

    report = generate_report(payload, format=args.format)
    if args.output:
        with open(args.output, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"✅ Report saved to: {args.output}")
    else:
        print(report)
    rem = (payload.get("data") or {}).get("quota_remaining")
    if rem is not None:
        print(f"\n💡 This Key's remaining free quota: {rem} calls.")


if __name__ == "__main__":
    main()
