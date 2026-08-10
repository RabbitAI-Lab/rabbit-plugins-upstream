#!/usr/bin/env python3
"""
HIPAA Compliance Check — Health Insurance Portability and Accountability Act (HIPAA), 45 C.F.R. Parts 160 & 164 (Privacy, Security, Breach Notification Rules)

Free skill + CQDev cloud compliance engine (compliancehub.cn).
Scoring and quota are computed in the cloud; before first use, register for a
free API Key (100 free calls) at compliancehub.cn:
  - Get a Key: run `python3 scripts/hipaa-check.py --login`
  - Or open: https://compliancehub.cn/account.html?skill=hipaa-check

Flow:
  1. Load API Key (env COMPLIANCEHUB_API_KEY, or ~/.config/compliancehub/<slug>.key)
  2. Fetch check items from the cloud rule-library API (public read)
  3. Collect per-item compliance status (y=pass / n=fail / na=n/a)
  4. Submit to the cloud evaluate endpoint (auth) OR score locally on 404
  5. Render a professional report locally

Uses only Python built-in urllib — zero third-party dependencies. HTTPS + Bearer
transport for the key; no hardcoding, no covert exfiltration. The only outbound network calls are (a) the explicit `--login`/`--auth` flow, which POSTs your email + password to compliancehub.cn's official auth endpoints to provision a free API Key, and (b) your scored answers + the API Key (as a Bearer token) to the pinned evaluate endpoint. No other data leaves the machine.
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
                return json.load(f).get("version", "1.0.0")
    except Exception:
        pass
    return "1.0.0"


def _ua():
    return f"{SKILL_SLUG}/{_skill_version()}"


def _key_path():
    """Private, per-user key store OUTSIDE the skill directory.
    The API Key is written here (mode 0600) rather than inside the skill
    folder, so it is never bundled with or leaked by the skill package.
    """
    d = os.path.join(os.path.expanduser("~"), ".config", "compliancehub")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"{SKILL_SLUG}.key")


def load_api_key():
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
    return None


def require_key():
    key = load_api_key()
    if key:
        return key
    msg = {
        "error": "missing_api_key",
        "message": "This skill calls the CQDev cloud compliance engine and needs a free API Key.",
        "register_page": ACCOUNT_PAGE,
        "cli": f"python3 scripts/{os.path.basename(__file__)} --login",
    }
    print(json.dumps(msg, ensure_ascii=False, indent=2))
    sys.exit(2)


def _api_json(method, url, payload=None, token=None):
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
    p = _key_path()
    with open(p, "w", encoding="utf-8") as f:
        f.write(key.strip() + "\n")
    try:
        os.chmod(p, 0o600)
    except Exception:
        pass
    return p


def cmd_auth():
    """Register/login in terminal; on success the free API Key is saved locally (0600)."""
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
        st2, data2 = _api_json("POST", AUTH_URL, {"email": email, "password": password, "name": name, "org_name": org})
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
    print("\n💡 Now just run it (free cloud scoring, 100 calls per Key):")
    print(f"   python3 scripts/{os.path.basename(__file__)} --format html -o report.html")


def fetch_rules():
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


CHECK_ITEMS = [
    {"id": "ce_ba_determination", "name": "Covered Entity / Business Associate", "ref": "\u00a7160.102-.103", "category": "A. \u9002\u7528\u6027",
     "desc": "Are you a HIPAA covered entity or business associate handling ePHI?", "recommendation": "\u5148\u5224\u5b9a\u5b9e\u4f53\u7c7b\u578b\uff0c\u51b3\u5b9a\u9002\u7528\u4e49\u52a1\u8303\u56f4\u3002"},
    {"id": "notice_of_privacy_practices", "name": "Notice of Privacy Practices", "ref": "Privacy Rule \u00a7164.520", "category": "B. \u9690\u79c1\u544a\u77e5",
     "desc": "Do you provide and honor a Notice of Privacy Practices (NPP)?", "recommendation": "\u5411\u4e2a\u4eba\u63d0\u4f9b NPP \u5e76\u7559\u5b58\u9001\u8fbe\u8bb0\u5f55\u3002"},
    {"id": "authorization", "name": "Valid Authorizations", "ref": "\u00a7164.508", "category": "B. \u9690\u79c1\u544a\u77e5",
     "desc": "Do you obtain valid authorizations for uses/disclosures beyond treatment/payment/operations?", "recommendation": "\u8425\u9500\u3001\u552e\u5356\u7b49\u573a\u666f\u987b\u5355\u72ec\u6388\u6743\u3002"},
    {"id": "admin_safeguards", "name": "Administrative Safeguards", "ref": "Security Rule \u00a7164.308", "category": "C. \u5b89\u5168\u7ba1\u7406",
     "desc": "Do you have admin safeguards: security officer, risk analysis, workforce training, contingency plan?", "recommendation": "\u5efa\u7acb\u4fe1\u606f\u5b89\u5168\u7ba1\u7406\u5236\u5ea6\u4e0e\u5e74\u5ea6\u98ce\u9669\u8bc4\u4f30\u3002"},
    {"id": "physical_safeguards", "name": "Physical Safeguards", "ref": "\u00a7164.310", "category": "C. \u5b89\u5168\u7ba1\u7406",
     "desc": "Do you control facility access and workstation/device security for ePHI?", "recommendation": "\u95e8\u7981\u3001\u5de5\u4f5c\u7ad9\u9501\u5c4f\u3001\u4ecb\u8d28\u9500\u6bc1\u7b49\u7269\u7406\u63a7\u5236\u5230\u4f4d\u3002"},
    {"id": "technical_safeguards", "name": "Technical Safeguards", "ref": "\u00a7164.312", "category": "C. \u5b89\u5168\u7ba1\u7406",
     "desc": "Do you enforce access control, audit controls, integrity, and transmission encryption for ePHI?", "recommendation": "\u552f\u4e00\u8eab\u4efd\u6807\u8bc6\u3001\u5ba1\u8ba1\u65e5\u5fd7\u3001TLS \u4f20\u8f93\u52a0\u5bc6\u3002"},
    {"id": "breach_notification", "name": "Breach Notification", "ref": "Breach Rule \u00a7164.400+", "category": "D. \u8fdd\u7ea6\u901a\u77e5",
     "desc": "Do you have a process to notify HHS (\u226460 days) and affected individuals of breaches?", "recommendation": "\u5236\u5b9a\u8fdd\u7ea6\u54cd\u5e94\u9884\u6848\u5e76\u6f14\u7ec3\u3002"},
    {"id": "minimum_necessary", "name": "Minimum Necessary", "ref": "\u00a7164.502(b)", "category": "B. \u9690\u79c1\u544a\u77e5",
     "desc": "Do you apply the minimum-necessary standard to uses/disclosures of PHI?", "recommendation": "\u6309\u89d2\u8272\u9650\u5236 PHI \u8bbf\u95ee\u6700\u5c0f\u96c6\u3002"},
    {"id": "baa", "name": "Business Associate Agreements", "ref": "\u00a7164.504(e)", "category": "E. \u5408\u4f5c\u65b9",
     "desc": "Do you have BAAs with every business associate that handles ePHI?", "recommendation": "\u4e0e\u4e91\u670d\u52a1/\u627f\u8fd0\u5546\u7b7e\u7f72 BAA\u3002"},
    {"id": "risk_analysis", "name": "Ongoing Risk Analysis", "ref": "\u00a7164.308(a)(1)(ii)(A)", "category": "C. \u5b89\u5168\u7ba1\u7406",
     "desc": "Do you conduct and update a risk analysis of ePHI threats/vulnerabilities?", "recommendation": "\u98ce\u9669\u5206\u6790\u6587\u6863\u5316\u5e76\u8ddf\u8fdb\u6574\u6539\u3002"},
    {"id": "workforce_training", "name": "Workforce Training", "ref": "\u00a7164.308(a)(5)", "category": "C. \u5b89\u5168\u7ba1\u7406",
     "desc": "Do you train the workforce on HIPAA policies and periodic reinforcement?", "recommendation": "\u65b0\u5458\u5de5\u5165\u804c\u57f9\u8bad + \u5e74\u5ea6\u590d\u8bad\u3002"},
    {"id": "individual_rights", "name": "Individual Rights", "ref": "\u00a7164.524/.526", "category": "F. \u4e2a\u4eba\u6743\u5229",
     "desc": "Do you support access, amendment, and accounting of disclosures for individuals?", "recommendation": "\u63d0\u4f9b\u75c5\u5386\u8c03\u9605/\u66f4\u6b63\u901a\u9053\u3002"},
]


def collect_responses(items):
    responses = []
    total = len(items)
    print(f"\n📋 HIPAA Compliance Check — {total} items")
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
    items = []
    for r in responses:
        if r["status"] == "na":
            continue
        items.append({"item_key": r["id"], "passed": r["status"] == "pass", "evidence": None})
    return items


def compute_local_score(submission, items):
    """Fallback scoring when cloud rule library is not yet open (404)."""
    meta = {it["id"]: it for it in items}
    total = len(submission)
    passed = sum(1 for s in submission if s["passed"])
    score = round(passed / total * 100) if total else 0
    out_items = []
    for s in submission:
        it = meta.get(s["item_key"], {}) or {}
        out_items.append({
            "item_key": s["item_key"], "name": it.get("name", s["item_key"]),
            "passed": s["passed"], "legal_ref": it.get("ref", ""),
            "recommendation": it.get("recommendation", ""), "category_name": it.get("category", ""),
        })
    return {
        "version": _skill_version(), "score": score,
        "passed_count": passed, "failed_count": total - passed, "total_items": total,
        "quota_remaining": None, "scored_locally": True, "items": out_items,
    }


def call_evaluate(key, submission):
    payload = {"items": submission, "context": None}
    body = json.dumps(payload).encode("utf-8")
    req = urllib.request.Request(EVALUATE_URL, data=body, headers={
        "Content-Type": "application/json", "Authorization": f"Bearer {key}", "User-Agent": _ua()}, method="POST")
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
            return None, "API Key invalid; run `python3 scripts/%s --login`" % os.path.basename(__file__)
        if e.code == 403:
            return None, f"free quota exhausted: {detail}"
        if e.code == 404:
            return None, "RULE_LIB_NOT_OPEN"
        return None, f"cloud error HTTP {e.code}: {detail}"
    except Exception as e:
        return None, f"cloud call failed: {e}"


def _score_block(data):
    return (f"  Compliance score: {data.get('score')}/100\n"
            f"  ✅ Pass {data.get('passed_count')} | ❌ Fail {data.get('failed_count')} | Items {data.get('total_items')}")


def render_text(data, items):
    s = data
    lines = ["=" * 60, f"  HIPAA Compliance Check Report (cloud-scored)" if not s.get("scored_locally") else f"  HIPAA Compliance Check Report (local fallback score)",
             f"  Law: Health Insurance Portability and Accountability Act (HIPAA), 45 C.F.R. Parts 160 & 164 (Privacy, Security, Breach Notification Rules)", f"  Engine version: {s.get('version', '?')}",
             _score_block(s), "=" * 60]
    current_cat = ""
    for r in items:
        if r.get("category_name") != current_cat:
            current_cat = r.get("category_name", "")
            lines.append(f"\n  ── {current_cat} ──")
        icon = "✅" if r.get("passed") else "❌"
        lines.append(f"\n  {icon} [{r.get('item_key')}] {r.get('name')}")
        if r.get("legal_ref"):
            lines.append(f"    Authority: {r.get('legal_ref')}")
        if r.get("recommendation"):
            lines.append(f"    Recommendation: {r.get('recommendation')}")
    lines.append("=" * 60)
    lines.append("\n💡 Disclaimer: reference only, not legal advice.")
    return "\n".join(lines)


def render_html(data, items):
    s = data
    score = s.get("score", 0)
    color = "#4caf50" if score >= 80 else "#ff9800" if score >= 60 else "#f44336"
    rows = ""
    current_cat = ""
    for r in items:
        if r.get("category_name") != current_cat:
            current_cat = r.get("category_name", "")
            rows += f'<tr class="category-row"><td colspan="5">{current_cat}</td></tr>\n'
        icon = "✅" if r.get("passed") else "❌"
        cls = "pass" if r.get("passed") else "fail"
        rec = r.get("recommendation") or "Keep it up"
        rows += f"""<tr class="{cls}"><td>{icon}</td><td>{r.get('name')}</td><td>{r.get('legal_ref') or ''}</td><td>{cls.upper()}</td><td>{rec}</td></tr>\n"""
    return f"""<!DOCTYPE html>
<html lang="en"><head><meta charset="UTF-8"><title>HIPAA Compliance Check Report</title>
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
</style></head><body>
<h1>HIPAA Compliance Check Report</h1>
<p>Law: Health Insurance Portability and Accountability Act (HIPAA), 45 C.F.R. Parts 160 & 164 (Privacy, Security, Breach Notification Rules)</p>
<p>Engine version: {s.get('version','?')}{' ｜ Local fallback score (cloud rule library not open yet)' if s.get('scored_locally') else ''}</p>
<div class="score-card"><div class="score">{score}</div><div>Compliance score / 100</div>
<div class="summary"><div>✅ Pass<br><b>{s.get('passed_count')}</b></div><div>❌ Fail<br><b>{s.get('failed_count')}</b></div><div>Items<br><b>{s.get('total_items')}</b></div></div></div>
<table><thead><tr><th></th><th>Check</th><th>Authority</th><th>Status</th><th>Recommendation</th></tr></thead><tbody>{rows}</tbody></table>
<p class="note">This report is generated by the CQDev cloud compliance engine for reference only and does not constitute legal advice.</p>
</body></html>"""


def generate_report(payload, format="text"):
    data = payload.get("data", {}) if isinstance(payload, dict) else {}
    items = data.get("items", [])
    if format == "json":
        return json.dumps(payload, ensure_ascii=False, indent=2)
    elif format == "html":
        return render_html(data, items)
    return render_text(data, items)


def main():
    parser = argparse.ArgumentParser(description="HIPAA Compliance Check (free skill + cloud engine)")
    parser.add_argument("--non-interactive", action="store_true", help="free preview mode (list items, no scoring)")
    parser.add_argument("--non-interactive-json", action="store_true", help="free preview JSON mode")
    parser.add_argument("--login", "--auth", dest="auth", action="store_true",
                        help="register/login CQDev account; on success the free API Key is saved locally (~/.config/compliancehub/, 0600)")
    parser.add_argument("--format", "-f", choices=["text", "json", "html"], default="text")
    parser.add_argument("--output", "-o", help="report output file path")
    args = parser.parse_args()

    if args.auth:
        cmd_auth()
        return

    items = fetch_rules() or CHECK_ITEMS

    if args.non_interactive_json:
        preview_data = [{"id": it["id"], "name": it["name"], "desc": it["desc"], "ref": it["ref"], "category": it["category"]} for it in items]
        print(json.dumps({"preview": True, "total_items": len(items), "free": True, "needs_api_key": True,
                          "register_page": ACCOUNT_PAGE, "message": "Free skill; scoring runs on the CQDev cloud engine (free API Key).",
                          "preview_items": preview_data}, ensure_ascii=False, indent=2))
        return

    if args.non_interactive:
        print(f"\n🔍 Free preview mode — {len(items)} items; scoring needs a free API Key\n")
        current_cat = ""
        for it in items:
            if it.get("category") != current_cat:
                current_cat = it.get("category", "")
                print(f"\n  ── {current_cat} ──")
            print(f"  • [{it['id']}] {it['name']}  [{it['ref']}]")
            print(f"      {it['desc']}")
        print(f"\n💡 Scoring runs on the cloud engine. Get a free API Key: {ACCOUNT_PAGE}")
        return

    key = require_key()
    responses = collect_responses(items)
    submission = build_submission(responses)
    if not submission:
        print("❌ No countable items (all marked not applicable).")
        sys.exit(1)

    print("\n⏳ Submitting to cloud compliance engine for scoring…")
    payload, err = call_evaluate(key, submission)
    if err == "RULE_LIB_NOT_OPEN":
        print("⚠️ Cloud rule library not open yet — using local fallback score (same questions, local computation).")
        data = compute_local_score(submission, items)
        payload = {"data": data}
    elif err:
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
