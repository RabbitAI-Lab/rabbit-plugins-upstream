#!/usr/bin/env python3
"""amazon.es fetch via session-cookie replay — no browser in the loop.

The browser is used ONCE, to authenticate (scripts/session-capture.mjs). After
that every request is plain HTTP with Chrome's TLS fingerprint, which is ~30x
faster than driving the shared tab and does not touch your browser at all.

The session itself is stored in the OS keychain (see scripts/session_store.py),
with a warned 0600 file fallback. Clear it with:
    node scripts/session-capture.mjs --logout

Two things make the replay work where a naive requests.get() fails:
  * curl_cffi impersonate="chrome" — amazon.es fingerprints the TLS/JA3 stack,
    so a stock Python client is blocked regardless of headers.
  * the captured cookies — they carry the ACCOUNT and the DELIVERY ADDRESS, and
    the delivery promise is derived from the address. Anonymous requests get a
    pessimistic generic date, which is the bug this whole path exists to fix.

Exit codes:
  0 ok · 2 NO_SESSION · 3 SESSION_STALE (cookies no longer authenticate)
  4 BLOCKED (WAF/captcha) · 5 bad usage
"""

import argparse
import json
import pathlib
import re
import sys
import time
import urllib.parse

from curl_cffi import requests

import session_store

# "Get It Tomorrow" refinement on amazon.es. NOT guessable — read from the URL
# after ticking the box in a real browser tab (2026-08-06).
NEXT_DAY_RH = "p_90:6820340031"

HEADERS = {
    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
    "accept-language": "en-GB,en;q=0.9,es;q=0.8,ca;q=0.7",
    "cache-control": "no-cache",
    "pragma": "no-cache",
    "upgrade-insecure-requests": "1",
    "sec-fetch-dest": "document",
    "sec-fetch-mode": "navigate",
    "sec-fetch-site": "none",
    "sec-fetch-user": "?1",
}


def load_jar():
    data, source = session_store.load()
    if data is None:
        sys.exit(
            "NO_SESSION: run `node scripts/session-capture.mjs --yes` with a shared, "
            "logged-in amazon.es tab. (Most queries do not need one — price, stock, "
            "title and images work anonymously; a session is only required for "
            "delivery promises and account-specific pricing.)"
        )
    jar = {c["name"]: c["value"] for c in data.get("cookies", [])}
    if not any(k in jar for k in ("at-acbes", "sess-at-acbes", "x-acbes")):
        sys.exit("NO_SESSION: stored cookies carry no auth token — re-capture.")
    return jar, data.get("captured_at"), source


def classify(html: str) -> str:
    """Tell apart a good page, a logged-out page, and a bot wall."""
    if "api-services-support@amazon.com" in html or "Type the characters you see in this image" in html:
        return "BLOCKED"
    if 'id="captchacharacters"' in html or "/errors/validateCaptcha" in html:
        return "BLOCKED"
    # A logged-in amazon.es page greets the account holder in the nav.
    if re.search(r"nav-line-1[^>]*>\s*(Hello|Hola)[^<]", html):
        return "OK"
    if re.search(r"(Sign in|Iniciar sesi&oacute;n|Identifícate)\s*</span>", html) and "nav-line-1-container" in html:
        return "STALE"
    # Fall back on structure: results present is good enough to parse.
    return "OK" if 'data-component-type="s-search-result"' in html else "STALE"


def save_jar(jar):
    """Persist the CURRENT cookie values back to the keychain (or warned file).

    2026-08-06, the defect this fixes: amazon.es rotates every auth cookie on
    EVERY response (at-acbes, sess-at-acbes, session-token, session-id,
    x-acbes all arrive in Set-Cookie). The first implementation replayed a
    frozen snapshot and threw the rotations away, so the session died within
    minutes — twice. A session is state, not a constant.
    """
    data, _source = session_store.load()
    if data is None:
        return
    for c in data.get("cookies", []):
        if c["name"] in jar:
            c["value"] = jar[c["name"]]
    data["rotated_at"] = time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
    session_store.save(data)


# One Session for the whole process: it carries the rotated cookies forward
# between requests instead of re-sending the original snapshot each time.
_SESSION = None


def get_session(jar):
    global _SESSION
    if _SESSION is None:
        _SESSION = requests.Session()
        for k, v in jar.items():
            _SESSION.cookies.set(k, v, domain=".amazon.es")
    return _SESSION


def fetch(url: str, jar, tries: int = 3) -> str:
    s = get_session(jar)
    last = None
    for attempt in range(tries):
        try:
            r = s.get(url, impersonate="chrome", headers=HEADERS, timeout=40)
            if r.status_code == 200:
                # Absorb the rotation so the NEXT request uses the fresh token.
                for k, v in r.cookies.items():
                    jar[k] = v
                return r.text
            last = f"HTTP {r.status_code}"
        except Exception as exc:  # network hiccup, retry
            last = str(exc)
        time.sleep(1.5 * (attempt + 1))
    sys.exit(f"BLOCKED: {last}")


def search_url(query: str, next_day: bool, page: int, lang_en: bool) -> str:
    params = {"k": query}
    if next_day:
        params["rh"] = NEXT_DAY_RH
    if page > 1:
        params["page"] = str(page)
    if lang_en:
        params["language"] = "en"
    return "https://www.amazon.es/s?" + urllib.parse.urlencode(params)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--url")
    ap.add_argument("--query")
    ap.add_argument("--next-day", action="store_true", help="apply the Get It Tomorrow refinement")
    ap.add_argument("--page", type=int, default=1)
    ap.add_argument("--lang-en", action="store_true", default=True)
    ap.add_argument("--out")
    ap.add_argument("--sweep", help="comma-separated query variants, run in ONE session")
    ap.add_argument("--pages", type=int, default=1)
    ap.add_argument("--out-dir", help="directory for --sweep page dumps")
    ap.add_argument("--status", action="store_true", help="report session health and exit")
    args = ap.parse_args()

    jar, captured_at, source = load_jar()

    if args.status:
        html = fetch("https://www.amazon.es/", jar)
        state = classify(html)
        print(json.dumps({"session": state, "captured_at": captured_at,
                          "cookies": len(jar), "stored_in": source}))
        sys.exit(0 if state == "OK" else (3 if state == "STALE" else 4))

    # --sweep runs every query inside ONE session, SEQUENTIALLY. Firing the same
    # session token from several processes at once looks like session hijacking
    # and is the other half of why the first design kept getting invalidated.
    if args.sweep:
        variants = [v.strip() for v in args.sweep.split(",") if v.strip()]
        queries = [f"{args.query} {v}".strip() for v in variants] if args.query else variants
        results, t0 = [], time.time()
        for q in queries:
            for page in range(1, args.pages + 1):
                url = search_url(q, args.next_day, page, args.lang_en)
                html = fetch(url, jar)
                state = classify(html)
                if state != "OK":
                    save_jar(jar)
                    sys.exit(f"SESSION_{state}: aborted at '{q}' p{page} — re-run session-capture.mjs.")
                cards = html.count('data-component-type="s-search-result"')
                path = pathlib.Path(args.out_dir or ".") / f"sweep-{len(results):02d}.html"
                path.write_text(html)
                results.append({"query": q, "page": page, "cards": cards, "file": str(path)})
                # A search page that suddenly renders a handful of cards is the
                # signature of a dying session, not a small catalogue.
                if cards < 5:
                    results[-1]["warning"] = "suspiciously few cards — check session health"
        save_jar(jar)
        print(json.dumps({"ok": True, "pages": results, "seconds": round(time.time() - t0, 2)}, indent=1))
        return

    if not args.url and not args.query:
        sys.exit("usage: --query <text> [--next-day] [--page N] | --sweep a,b,c | --url <amazon.es url>")

    url = args.url or search_url(args.query, args.next_day, args.page, args.lang_en)
    t0 = time.time()
    html = fetch(url, jar)
    state = classify(html)
    save_jar(jar)
    if state == "STALE":
        sys.exit("SESSION_STALE: cookies no longer authenticate — re-run session-capture.mjs.")
    if state == "BLOCKED":
        sys.exit("BLOCKED: bot wall — back off, then re-capture cookies.")

    cards = html.count('data-component-type="s-search-result"')
    meta = {"ok": True, "url": url, "bytes": len(html), "cards": cards, "seconds": round(time.time() - t0, 2)}
    if cards < 5:
        meta["warning"] = "suspiciously few cards — check session health"
    if args.out:
        pathlib.Path(args.out).write_text(html)
        meta["out"] = args.out
        print(json.dumps(meta))
    else:
        sys.stderr.write(json.dumps(meta) + "\n")
        sys.stdout.write(html)


if __name__ == "__main__":
    main()
