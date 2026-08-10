#!/usr/bin/env python3
"""
CCPA Compliance Audit — California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment

Free skill + CQDev cloud compliance engine (compliancehub.cn).
Scoring and quota are computed in the cloud; before first use, register for a
free API Key (100 free calls) at compliancehub.cn:
  - Get a Key: run `python3 scripts/ccpa-audit.py --login`
  - Or open: https://compliancehub.cn/account.html?skill=ccpa-audit

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
    {"id": "right_to_know", "name": "\u77e5\u60c5\u6743", "ref": "CCPA \u00a71798.100", "category": "A. \u6d88\u8d39\u8005\u6743\u5229",
     "desc": "\u662f\u5426\u652f\u6301\u6d88\u8d39\u8005\u77e5\u6653\u6240\u6536\u96c6 PI \u7684\u7c7b\u522b\u4e0e\u6765\u6e90/\u76ee\u7684\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "right_to_delete", "name": "\u5220\u9664\u6743", "ref": "CCPA \u00a71798.105", "category": "A. \u6d88\u8d39\u8005\u6743\u5229",
     "desc": "\u662f\u5426\u63d0\u4f9b\u53ef\u6267\u884c\u7684\u5220\u9664\u8bf7\u6c42\u901a\u9053\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "right_to_optout", "name": "\u9009\u62e9\u9000\u51fa\u6743", "ref": "CCPA \u00a71798.120", "category": "A. \u6d88\u8d39\u8005\u6743\u5229",
     "desc": "\u662f\u5426\u63d0\u4f9b\u300cDo Not Sell/Share\u300d\u5e76\u5c0a\u91cd GPC\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "non_discrimination", "name": "\u975e\u6b67\u89c6\u539f\u5219", "ref": "CCPA \u00a71798.125", "category": "A. \u6d88\u8d39\u8005\u6743\u5229",
     "desc": "\u662f\u5426\u4e0d\u56e0\u884c\u4f7f\u6743\u5229\u800c\u6b67\u89c6\u6d88\u8d39\u8005\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "notice_at_collection", "name": "\u6536\u96c6\u901a\u77e5", "ref": "CCPA \u00a71798.100(b)", "category": "B. \u544a\u77e5\u4e49\u52a1",
     "desc": "\u6536\u96c6\u65f6\u662f\u5426\u62ab\u9732\u7c7b\u522b\u4e0e\u76ee\u7684\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "pi_categories", "name": "\u4e2a\u4eba\u4fe1\u606f\u7c7b\u522b", "ref": "CCPA \u00a71798.140", "category": "B. \u544a\u77e5\u4e49\u52a1",
     "desc": "\u662f\u5426\u5b8c\u6574\u5217\u793a\u6240\u5904\u7406 PI \u7c7b\u522b\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "data_minimization", "name": "\u6570\u636e\u6700\u5c0f\u5316", "ref": "CPRA \u00a71798.100(b)", "category": "C. \u5904\u7406\u539f\u5219",
     "desc": "\u662f\u5426\u5728\u76ee\u7684\u5fc5\u8981\u8303\u56f4\u5185\u6536\u96c6\u5408\u89c4\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "service_provider", "name": "\u670d\u52a1\u63d0\u4f9b\u5546\u4e49\u52a1", "ref": "CCPA \u00a71798.140(ag)", "category": "D. \u7b2c\u4e09\u65b9",
     "desc": "\u4e0e\u670d\u52a1\u63d0\u4f9b\u5546\u5408\u540c\u662f\u5426\u7981\u6b62\u4e8c\u6b21\u4f7f\u7528\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "third_party_sharing", "name": "\u7b2c\u4e09\u65b9\u5171\u4eab", "ref": "CCPA \u00a71798.115", "category": "D. \u7b2c\u4e09\u65b9",
     "desc": "\u662f\u5426\u62ab\u9732\u5171\u4eab\u7684\u7b2c\u4e09\u65b9\u7c7b\u522b\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "sensitive_pi", "name": "\u654f\u611f\u4e2a\u4eba\u4fe1\u606f(CPRA)", "ref": "CPRA \u00a71798.140(ae)", "category": "C. \u5904\u7406\u539f\u5219",
     "desc": "\u654f\u611f PI \u662f\u5426\u9650\u5b9a\u7528\u9014\u5e76\u63d0\u4f9b\u9650\u5236\u6743\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "right_to_correct", "name": "\u66f4\u6b63\u6743", "ref": "CPRA \u00a71798.106", "category": "A. \u6d88\u8d39\u8005\u6743\u5229",
     "desc": "\u662f\u5426\u652f\u6301\u66f4\u6b63\u4e0d\u51c6\u786e PI\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "limit_sensitive_use", "name": "\u9650\u5236\u654f\u611fPI\u4f7f\u7528", "ref": "CPRA \u00a71798.121", "category": "C. \u5904\u7406\u539f\u5219",
     "desc": "\u662f\u5426\u63d0\u4f9b\u9650\u5236\u654f\u611f PI \u4f7f\u7528\u7684\u9009\u9879\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "automated_decisions", "name": "\u81ea\u52a8\u5316\u51b3\u7b56", "ref": "CPRA \u00a71798.185(a)(16)", "category": "E. \u95ee\u8d23",
     "desc": "\u753b\u50cf/\u81ea\u52a8\u51b3\u7b56\u662f\u5426\u6709\u8bf4\u660e\u4e0e\u9000\u51fa\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "privacy_policy", "name": "\u9690\u79c1\u653f\u7b56", "ref": "CCPA \u00a71798.130", "category": "B. \u544a\u77e5\u4e49\u52a1",
     "desc": "\u9690\u79c1\u653f\u7b56\u662f\u5426\u5e74\u5ea6\u66f4\u65b0\u5e76\u5217\u660e\u6743\u5229\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "request_verification", "name": "\u8bf7\u6c42\u9a8c\u8bc1", "ref": "CCPA \u00a71798.145(i)", "category": "A. \u6d88\u8d39\u8005\u6743\u5229",
     "desc": "\u6743\u5229\u8bf7\u6c42\u662f\u5426\u505a\u8eab\u4efd\u6838\u9a8c\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "minors_data", "name": "\u672a\u6210\u5e74\u4eba\u6570\u636e", "ref": "CCPA \u00a71798.120(c)", "category": "E. \u95ee\u8d23",
     "desc": "\u662f\u5426\u5bf9\u672a\u6210\u5e74\u4eba\u52a0\u4e25\u540c\u610f\uff08\u542b opt-in\uff09\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "annual_disclosure", "name": "\u5e74\u5ea6\u62ab\u9732", "ref": "CCPA \u00a71798.130(a)(5)", "category": "B. \u544a\u77e5\u4e49\u52a1",
     "desc": "\u662f\u5426\u5411\u5458\u5de5\u62ab\u9732\u6536\u96c6\u7684 PI \u7c7b\u522b\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "audit_rights", "name": "\u5408\u540c\u5ba1\u8ba1\u6743", "ref": "CCPA \u00a71798.140(ag)(3)", "category": "D. \u7b2c\u4e09\u65b9",
     "desc": "\u670d\u52a1\u63d0\u4f9b\u5546\u5408\u540c\u662f\u5426\u4fdd\u7559\u5ba1\u8ba1\u6743\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "retention_period", "name": "\u7559\u5b58\u671f\u9650", "ref": "CPRA \u00a71798.100(a)(3)", "category": "C. \u5904\u7406\u539f\u5219",
     "desc": "\u662f\u5426\u8bbe\u5b9a PI \u7559\u5b58\u671f\u9650\u5e76\u5230\u671f\u5220\u9664\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
    {"id": "security_obligation", "name": "\u5b89\u5168\u4e49\u52a1", "ref": "CCPA \u00a71798.150(a)(1)", "category": "F. \u5b89\u5168",
     "desc": "\u662f\u5426\u91c7\u53d6\u5408\u7406\u5b89\u5168\u63aa\u65bd\u5e76\u5177\u5907\u8fdd\u7ea6\u6551\u6d4e\uff1f", "recommendation": "\u5bf9\u7167\u6cd5\u89c4\u8981\u6c42\u843d\u5b9e\u5e76\u4fdd\u6301\u8bc1\u636e\u3002"},
]


def collect_responses(items):
    responses = []
    total = len(items)
    print(f"\n📋 CCPA Compliance Audit — {total} items")
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
    lines = ["=" * 60, f"  CCPA Compliance Audit Report (cloud-scored)" if not s.get("scored_locally") else f"  CCPA Compliance Audit Report (local fallback score)",
             f"  Law: California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment", f"  Engine version: {s.get('version', '?')}",
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
<html lang="en"><head><meta charset="UTF-8"><title>CCPA Compliance Audit Report</title>
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
<h1>CCPA Compliance Audit Report</h1>
<p>Law: California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment</p>
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
    parser = argparse.ArgumentParser(description="CCPA Compliance Audit (free skill + cloud engine)")
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
