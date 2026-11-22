#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal Domain Risk & Xuan-Ping Review - read-only black-box scanner (generic v1.1)
Input: any domain. Output: structured JSON (DNS / TLS / HTTP headers / subdomains /
sensitive content / whois registration age / CDN-range hints).

Universality contract:
  - No domain-specific constants; all facts are driven by collected evidence.
  - Unavailable data stays empty and is marked "evidence failed"; never fabricated,
    never filled with defaults.
  - CDN attribution is only a "suspected" hint from public IP ranges; it never
    asserts the origin location / hosting geography.
  - Pure external read-only: no config changes, no credentials, no panel login.
"""
import sys, json, socket, ssl, re, ipaddress
from datetime import datetime, timezone
import requests

TIMEOUT = 12

# Generic common subdomains only (no business-specific names; probe results ARE the evidence, no assumed existence)
COMMON_SUBS = ["www", "api", "mail", "webmail", "m", "app", "dev", "admin",
               "status", "cdn", "img", "static", "blog", "shop", "test",
               "staging", "docs", "ftp", "ns1", "ns2", "origin", "assets"]

# Public CDN edge IPv4 ranges (for "suspected" hints only; NOT origin location)
# A hit only means the A record falls in a public edge range; it cannot be used to infer the server physical location.
CDN_RANGES = {
    "Cloudflare": [
        "104.16.0.0/13", "172.64.0.0/13", "162.158.0.0/15", "173.245.48.0/20",
        "103.21.244.0/22", "141.101.64.0/18", "108.162.192.0/18",
        "190.93.240.0/20", "188.114.96.0/20", "197.234.240.0/22",
        "198.41.128.0/17", "131.0.72.0/22",
    ],
}

def norm_domain(d):
    d = d.strip().lower()
    d = re.sub(r'^https?://', '', d)
    d = re.sub(r'^www\.', '', d)
    d = d.split('/')[0].split('?')[0]
    return d

def detect_cdn(ips):
    """Return a "suspected CDN" hint from public IP ranges. Empty list on no hit (never concludes "not CDN")."""
    hits = []
    for name, ranges in CDN_RANGES.items():
        nets = [ipaddress.ip_network(r) for r in ranges]
        for ip in ips or []:
            try:
                addr = ipaddress.ip_address(ip)
                if addr.version == 4 and any(addr in n for n in nets):
                    if name not in hits:
                        hits.append(name)
            except ValueError:
                pass
    return hits

def get_a(domain):
    try:
        infos = socket.getaddrinfo(domain, None)
        v4 = sorted({i[4][0] for i in infos if ':' not in i[4][0]})
        v6 = sorted({i[4][0] for i in infos if ':' in i[4][0]})
        return {"v4": v4, "v6": v6, "cdn_hint": detect_cdn(v4), "ok": bool(v4 or v6)}
    except Exception as e:
        return {"v4": [], "v6": [], "cdn_hint": [], "ok": False, "error": str(e)}

def get_tls(domain, port=443):
    try:
        ctx = ssl.create_default_context()
        with socket.create_connection((domain, port), timeout=TIMEOUT) as sock:
            with ctx.wrap_socket(sock, server_hostname=domain) as ssock:
                cert = ssock.getpeercert()
        san = [t[1] for t in cert.get('subjectAltName', ()) if t[0] == 'DNS']
        nb = datetime.strptime(cert['notBefore'], '%b %d %H:%M:%S %Y %Z').replace(tzinfo=timezone.utc)
        na = datetime.strptime(cert['notAfter'], '%b %d %H:%M:%S %Y %Z').replace(tzinfo=timezone.utc)
        days = (na - datetime.now(timezone.utc)).days
        issuer = dict(x[0] for x in cert.get('issuer', ()))
        subject = dict(x[0] for x in cert.get('subject', ()))
        return {"subject_cn": subject.get('commonName'), "issuer_org": issuer.get('organizationName'),
                "issuer_cn": issuer.get('commonName'), "san": san,
                "not_before": nb.strftime('%Y-%m-%d'), "not_after": na.strftime('%Y-%m-%d'),
                "days_left": days, "ok": True}
    except Exception as e:
        return {"ok": False, "error": str(e)}

def get_http_headers(domain):
    security = ["strict-transport-security", "content-security-policy", "x-content-type-options",
                "referrer-policy", "permissions-policy", "x-frame-options", "x-xss-protection"]
    try:
        r = requests.get(f"https://{domain}/", timeout=TIMEOUT, allow_redirects=True,
                         headers={"User-Agent": "Mozilla/5.0 universal-domain-xuanping/1.1"})
        h = {k.lower(): v for k, v in r.headers.items()}
        found = {s: h[s] for s in security if s in h}
        missing = [s for s in security if s not in h]
        redirect = {"from": r.history[0].status_code, "to": r.url} if r.history else None
        return {"status": r.status_code, "server": h.get('server'), "redirect": redirect,
                "security_present": found, "security_missing": missing,
                "body": r.text[:200000], "final_url": r.url, "ok": True}
    except Exception as e:
        return {"status": None, "ok": False, "error": str(e),
                "security_present": {}, "security_missing": [], "body": "", "final_url": None}

def scan_subdomains(domain, base_ips):
    """Enumerate generic common subdomains. Skip on evidence failure; never conclude "does not exist"."""
    results = []
    base_set = set(base_ips or [])
    for sub in COMMON_SUBS:
        host = f"{sub}.{domain}"
        try:
            ips = sorted({i[4][0] for i in socket.getaddrinfo(host, None)})
        except Exception:
            continue  # unresolvable = not recorded, never treated as "absent / no asset"
        code = None
        try:
            rr = requests.get(f"https://{host}/", timeout=6, allow_redirects=True,
                              headers={"User-Agent": "Mozilla/5.0 universal-domain-xuanping/1.1"})
            code = rr.status_code
        except requests.RequestException:
            code = "000"  # resolved but unreachable, recorded as-is
        results.append({"host": host, "ips": ips, "http": code,
                        "same_as_base": bool(set(ips) & base_set)})
    return results

def content_scan(body):
    findings = {"emails": [], "private_key_marks": [], "secret_words": [],
                "external_links": [], "analytics_scripts": []}
    b = body or ''
    for m in re.findall(r'[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}', b):
        if m not in findings['emails']:
            findings['emails'].append(m)
    # Private-key header = high risk; password/api_key words = needs attention (may be documentation; human determination required)
    pk = re.findall(r'-----BEGIN [A-Z ]*PRIVATE KEY-----', b)
    if pk:
        findings['private_key_marks'].append({"label": "private-key header", "count": len(pk)})
    for pat, label in [(r'api[_-]?key\s*[:=]', 'api_key word'),
                       (r'(secret|password|passwd)\s*[:=]', 'password word')]:
        hits = re.findall(pat, b, re.I)
        if hits:
            findings['secret_words'].append({"label": label, "count": len(hits)})
    links = re.findall(r'https?://([A-Za-z0-9.-]+)', b)
    for l in links:
        if l not in findings['external_links']:
            findings['external_links'].append(l)
    for kw in ['gtag', 'googletagmanager', 'google-analytics', 'analytics',
               'hm.js', 'hm.baidu', 'clarity', 'plausible', 'umami']:
        if kw in b.lower():
            findings['analytics_scripts'].append(kw)
    return findings

def parse_date(s):
    """Accept Unix timestamp (int/float) / ISO8601 / 'YYYY-MM-DD HH:MM:SS' / 'DD-Mon-YYYY'.
    api.whois.vu returns integer timestamps for some gTLDs and strings for .cn, so all must be handled."""
    if s is None or s == '':
        return None
    # Numeric timestamp (int/float or pure-digit string)
    if isinstance(s, (int, float)) or (isinstance(s, str) and re.fullmatch(r'\d{9,13}', s.strip())):
        try:
            ts = int(s)
            if ts > 10**12:  # milliseconds
                ts //= 1000
            return datetime.fromtimestamp(ts, timezone.utc).strftime('%Y-%m-%d')
        except (ValueError, OSError, OverflowError):
            return None
    s = str(s).strip()
    m = re.match(r'(\d{4}-\d{2}-\d{2})', s)
    if m:
        return m.group(1)
    m = re.match(r'(\d{2})-([A-Za-z]{3})-(\d{4})', s)  # 02-Sep-2006
    if m:
        try:
            return datetime.strptime(s[:11], '%d-%b-%Y').strftime('%Y-%m-%d')
        except Exception:
            return None
    return None

def whois_lookup(domain):
    """Prefer structured fields (created/expires), fall back to multi-format regex.
    Compatible with .com / .cn / other suffixes. Missing -> ok=False, no fabrication."""
    try:
        r = requests.get(f"https://api.whois.vu/?q={domain}", timeout=TIMEOUT)
        if r.status_code != 200 or not r.text.strip().startswith('{'):
            return {"ok": False, "error": "whois API returned no valid data (verify manually in the registrar panel)"}
        d = r.json()
        raw = d.get('whois', '') or ''

        def grab(labels):
            for label in labels:
                m = re.search(rf'^\s*{label}\s*:\s*(.+)$', raw, re.I | re.M)
                if m:
                    return m.group(1).strip()
            return None

        # 1) Structured fields (most gTLDs provide these directly)
        created = parse_date(d.get('created'))
        expires = parse_date(d.get('expires'))
        # 2) Raw regex fallback (.cn / registrars differ in format)
        created = created or parse_date(grab([
            'Creation Date', 'Registration Time', 'Registered on', 'Created Date',
            'Registration Date', 'Domain Registration Date', 'created']))
        expires = expires or parse_date(grab([
            'Registry Expiry Date', 'Expiration Time', 'Expiry Date', 'Expires On',
            'Expiration Date', 'paid-till', 'Registrar Registration Expiration Date']))
        registrar = d.get('registrar') or grab([
            'Sponsoring Registrar', 'Registrar Name', 'Registrar'])
        name_servers = d.get('name_servers') or re.findall(
            r'^\s*(?:Name Server|nserver|Nserver)\s*:\s*(.+)$', raw, re.I | re.M)

        age = None
        if created:
            try:
                cd = datetime.strptime(created, '%Y-%m-%d')
                age = round((datetime.now() - cd).days / 365.25, 1)
            except Exception:
                pass
        ok = bool(created)
        return {"ok": ok, "source": "api.whois.vu", "registrar": registrar,
                "created": created, "expires": expires, "age_years": age,
                "statuses": d.get('statuses', []), "name_servers": name_servers,
                "error": None if ok else "Could not parse registration date (verify in the registrar panel)"}
    except Exception as e:
        return {"ok": False, "error": f"whois query failed: {type(e).__name__} (manual check needed)"}

def main():
    if len(sys.argv) < 2:
        print(json.dumps({"error": "Usage: scan_domain.py <domain>"}, ensure_ascii=False))
        sys.exit(1)
    domain = norm_domain(sys.argv[1])
    out = {"domain": domain,
           "scanned_at": datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC'),
           "tld": domain.rsplit('.', 1)[-1] if '.' in domain else ''}
    out['dns'] = get_a(domain)
    out['tls'] = get_tls(domain)
    hdr = get_http_headers(domain)
    out['http'] = {k: v for k, v in hdr.items() if k != 'body'}
    out['content'] = content_scan(hdr.get('body', ''))
    out['subdomains'] = scan_subdomains(domain, out['dns'].get('v4', []))
    out['whois'] = whois_lookup(domain)
    # Evidence completeness: lets the report layer degrade, avoiding "evidence failed but reported normal"
    out['evidence'] = {
        "dns_ok": bool(out['dns'].get('ok')),
        "tls_ok": bool(out['tls'].get('ok')),
        "http_ok": bool(hdr.get('ok')),
        "whois_ok": bool(out['whois'].get('ok')),
    }
    print(json.dumps(out, ensure_ascii=False, indent=2))

if __name__ == '__main__':
    main()
