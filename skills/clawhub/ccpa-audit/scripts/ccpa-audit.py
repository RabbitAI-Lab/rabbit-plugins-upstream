#!/usr/bin/env python3
"""
CCPA Compliance Audit — California Consumer Privacy Act (CCPA, Cal. Civ. Code §1798.100 et seq.) & CPRA amendment

Free skill + CQDev cloud compliance engine (compliancehub.cn).
Scoring and quota are computed in the cloud; before first use, get a free API
Key (100 free calls) at the web account center. Registration is browser-only
because it includes a human/captcha check the terminal cannot perform:
  - Open: https://compliancehub.cn/account.html?skill=ccpa-audit
  - Then hand the Key to this skill via COMPLIANCEHUB_API_KEY or a key file

Flow:
  1. Load API Key (env COMPLIANCEHUB_API_KEY, or ~/.config/compliancehub/<slug>.key)
  2. Fetch check items from the cloud rule-library API (public read)
  3. Collect per-item compliance status (y=pass / n=fail / na=n/a)
  4. Submit to the cloud evaluate endpoint (auth) OR score locally on 404
  5. Render a professional report locally

Uses only Python built-in urllib — zero third-party dependencies. HTTPS + Bearer
transport for the key; no hardcoding, no covert exfiltration. Outbound network calls are:
(a) fetching the public check-item rule library from the pinned endpoint before any preview/scored
run (read-only, NO answers sent); (b) your scored answers + the API Key (as a Bearer token)
to the pinned evaluate endpoint. The API Key is obtained from the web account center and
supplied via the COMPLIANCEHUB_API_KEY environment variable or ~/.config/compliancehub/<slug>.key;
this skill never collects your email/password or creates accounts. No other data leaves the machine.

Language: bilingual (中文/English). Item names, categories and recommendations are
presented in Chinese by default for Chinese-speaking compliance teams; legal/regulatory
references keep English originals. Users may request English output at any time.
"""
import sys, os, json, argparse, datetime, ssl
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
ACCOUNT_PAGE = f"{API_BASE}/account.html?skill={SKILL_SLUG}"      # unified account center (register here; skill only consumes the Key)


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
    if sys.stdin.isatty():
        # Human at an interactive terminal: print friendly guidance, not raw JSON.
        print("\n🔑 生成评分报告需要一把免费的 API Key（每个 Key 含 100 次免费调用）。")
        print("   两步即可开通：")
        print(f"   1) 打开网页注册并领取 Key：{ACCOUNT_PAGE}")
        print("   2) 把 Key 交给本工具（任选其一）：")
        print("        export COMPLIANCEHUB_API_KEY=<网页显示的 Key>")
        print(f"        mkdir -p ~/.config/compliancehub && echo '<网页显示的 Key>' > ~/.config/compliancehub/{SKILL_SLUG}.key")
        print("   若只想先看题目、暂不评分，可运行："
              f"python3 scripts/{os.path.basename(__file__)} --non-interactive")
    else:
        # Non-interactive (agent / piped): keep machine-readable JSON for the caller.
        msg = {
            "error": "missing_api_key",
            "message": "This skill calls the CQDev cloud compliance engine and needs a free API Key.",
            "get_key_page": ACCOUNT_PAGE,
            "option_env": "export COMPLIANCEHUB_API_KEY=sk_live_xxx",
            "option_file": f"mkdir -p ~/.config/compliancehub && echo 'sk_live_xxx' > ~/.config/compliancehub/{SKILL_SLUG}.key",
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


# NOTE: account registration is handled by the web account center
# (https://compliancehub.cn/account.html). This skill only CONSUMES an API Key
# via COMPLIANCEHUB_API_KEY or ~/.config/compliancehub/<slug>.key — it never
# registers accounts or collects credentials in the terminal.


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


def _draft_path():
    """Per-user audit draft, stored OUTSIDE the skill folder (never bundled)."""
    d = os.path.join(os.path.expanduser("~"), ".config", "compliancehub")
    os.makedirs(d, exist_ok=True)
    return os.path.join(d, f"{SKILL_SLUG}.audit.draft.json")


def _normalize_answer(ans):
    """Accept both English and Chinese answers so Chinese-first users aren't stuck."""
    a = (ans or "").strip().lower()
    if a in ('y', 'yes', '是', '通过', '符合'):
        return 'pass'
    if a in ('n', 'no', '否', '不通过', '不符合'):
        return 'fail'
    if a in ('na', 'n/a', '不适用', '豁免'):
        return 'na'
    if a in ('?', 'h', '帮助', '建议'):
        return 'help'
    return None


def _save_draft(path, answers):
    try:
        with open(path, 'w', encoding='utf-8') as f:
            json.dump(answers, f, ensure_ascii=False)
    except Exception:
        pass


def _load_draft(path):
    try:
        if os.path.isfile(path):
            with open(path, encoding='utf-8') as f:
                return json.load(f)
    except Exception:
        pass
    return None


def collect_responses(items):
    responses = []
    total = len(items)
    draft_path = _draft_path()

    # Resume an unfinished draft (interactive terminals only).
    if sys.stdin.isatty():
        draft = _load_draft(draft_path)
        if draft:
            print(f"\n📝 检测到上次未完成的审计草稿（{len(draft)}/{total} 项已作答）。")
            r = input("   继续作答 (y) 还是重新开始 (n)？[y] > ").strip().lower()
            if r != 'n':
                responses = list(draft)
            try:
                os.remove(draft_path)
            except Exception:
                pass

    print(f"\n📋 CCPA Compliance Audit — 共 {total} 项")
    print("   逐项确认实际状态：y=通过 / n=不符合 / na=不适用；输入 ? 可看该项建议\n")

    for i in range(len(responses), total):
        item = items[i]
        idx = i + 1
        if item.get('category') and (not responses or responses[-1].get('category') != item.get('category')):
            print(f"  ── {item.get('category')} ──")
        pct = round(idx / total * 100)
        while True:
            ans = input(f"  [{idx}/{total} · {pct}%] {item['name']} [{item['ref']}]\n"
                        f"        {item['desc']}\n"
                        f"        (y/n/na/?) > ").strip().lower()
            norm = _normalize_answer(ans)
            if norm == 'help':
                rec = item.get('recommendation') or '对照法规要求落实并保持证据。'
                print(f"        💡 建议：{rec}")
                continue
            if norm is None:
                print("        请输入 y / n / na 或 ?（也可用中文：是 / 否 / 不适用）")
                continue
            responses.append({**item, "status": norm})
            break
        # Autosave so a long audit isn't lost on interruption.
        if sys.stdin.isatty():
            _save_draft(draft_path, responses)

    passed = sum(1 for r in responses if r['status'] == 'pass')
    failed = sum(1 for r in responses if r['status'] == 'fail')
    na = sum(1 for r in responses if r['status'] == 'na')
    print(f"\n  ✅ 通过 {passed} ｜ ❌ 不符合 {failed} ｜ ⚪ 不适用 {na} ｜ 共 {total} 项")

    try:
        os.remove(draft_path)
    except Exception:
        pass
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
            return None, "API Key invalid; get a free Key at %s and set COMPLIANCEHUB_API_KEY" % ACCOUNT_PAGE
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
    parser.add_argument("--format", "-f", choices=["text", "json", "html"], default="text")
    parser.add_argument("--output", "-o", help="report output file path")
    args = parser.parse_args()

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
