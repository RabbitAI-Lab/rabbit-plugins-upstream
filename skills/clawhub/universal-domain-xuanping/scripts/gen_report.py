#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal Domain Risk & Xuan-Ping Review - report generator (generic v1.1, EN)
Reads scan_domain.py JSON + divination.py JSON, produces an 8-dimension RAG
markdown report + a Xuan-Ping (I-Ching) Easter egg.

Universality contract (any domain):
  1. All conclusions are driven by the evidence JSON; this file contains NO
     domain-specific facts (IPs, CDN names, geography, suffix).
  2. Failed evidence degrades to "pending / undetermined"; never "normal / none
     found / no obligation" style affirmative conclusions.
  3. Compliance is a rule hint only; no inference of server location or filing
     obligation, no legal opinion.
  4. No market-value figures, no fabricated traffic; missing data is stated.
  5. The hexagram is an Easter egg, not part of conclusions, not a decision basis.
"""
import sys, json, datetime

def gen(scan, div, domain):
    dns = scan.get('dns', {})
    tls = scan.get('tls', {})
    http = scan.get('http', {})
    content = scan.get('content', {})
    subs = scan.get('subdomains', [])
    whois = scan.get('whois', {})
    ev = scan.get('evidence', {})  # backward compatible: infer from per-dim ok
    tld = scan.get('tld') or (domain.rsplit('.', 1)[-1] if '.' in domain else '')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M')

    def eok(key, fallback):
        return ev.get(key, bool(fallback))

    dns_ok = eok('dns_ok', dns.get('ok', dns.get('v4')))
    tls_ok = eok('tls_ok', tls.get('ok', tls.get('not_after')))
    http_ok = eok('http_ok', http.get('ok', http.get('status')))
    whois_ok = eok('whois_ok', whois.get('ok', whois.get('created')))

    # ---------- Rating: failed evidence always degrades, no inference ----------
    L = {}
    if not dns_ok:
        L['dns'] = ('amber', 'Resolution evidence failed / no resolvable records, manual check needed')
    else:
        L['dns'] = ('green', 'Resolution normal')
    days = tls.get('days_left')
    if not tls_ok:
        L['tls'] = ('amber', 'Certificate not obtained / 443 not open, undetermined (no "no-risk" claim)')
    elif isinstance(days, int) and days > 14:
        L['tls'] = ('green', f'Valid, {days} days remaining')
    elif isinstance(days, int):
        L['tls'] = ('amber', f'Certificate only {days} days remaining')
    else:
        L['tls'] = ('amber', 'Certificate validity could not be parsed, manual check needed')
    missing = http.get('security_missing', []) or []
    core = [s for s in missing if s in ('strict-transport-security', 'content-security-policy', 'x-content-type-options')]
    if not http_ok:
        L['hdr'] = ('amber', 'HTTP response header evidence failed, undetermined')
    elif core:
        L['hdr'] = ('amber', f'{len(core)} core header(s) missing')
    else:
        L['hdr'] = ('green', 'Core security headers present')
    bad = [s for s in subs if str(s.get('http')) in ('404', '530', '000')]
    if not dns_ok:
        L['sub'] = ('amber', 'Base resolution failed, subdomains untested')
    elif bad:
        L['sub'] = ('amber', f'{len(bad)} subdomain(s) anomalous / dangling')
    else:
        L['sub'] = ('green', 'Probed subdomains look normal')
    pk = content.get('private_key_marks', []) or []
    sw = content.get('secret_words', []) or []
    if not http_ok:
        L['content'] = ('amber', 'Homepage content not retrieved, undetermined')
    elif pk:
        L['content'] = ('red', 'Suspected private-key content on homepage, verify immediately')
    elif sw:
        L['content'] = ('amber', 'Password/key words on homepage (may be documentation), manual check needed')
    else:
        L['content'] = ('green', 'No private-key / password-type leak detected')
    L['compliance'] = ('hint', 'Rule hint only; owner must verify server physical location and filing (black box does not decide)')
    age = whois.get('age_years')
    created = whois.get('created')
    if whois_ok and created:
        L['age'] = ('green', f'Registered ~{age} years ({created})')
    else:
        L['age'] = ('amber', 'Registration age could not be evidenced, verify in registrar panel')
    L['value'] = ('amber', 'No authoritative valuation source, no figure given (not an asset-pricing basis)')
    L['traffic'] = ('amber', 'External black box cannot measure real traffic, pending owner-supplied data')

    icon = {'green': '🟢', 'amber': '🟡', 'red': '🔴', 'hint': '⚪'}
    risk_keys = ['dns', 'tls', 'hdr', 'sub', 'content', 'age', 'value', 'traffic']
    reds = sum(1 for k in risk_keys if L[k][0] == 'red')
    yellows = sum(1 for k in risk_keys if L[k][0] == 'amber')

    # ---------- Report ----------
    lines = []
    lines.append(f"# [Risk Review] {domain} - Web Asset Risk Assessment (auto-generated)\n")
    lines.append("- Issued by: Universal Domain Risk & Xuan-Ping Review v1.1 (auto-generated)")
    lines.append(f"- Date: {now}")
    lines.append(f"- Subject: `{domain}` (incl. subdomains) | TLD: `.{tld}`")
    lines.append("- Nature: **read-only evidence** risk assessment; no config changes, no credentials, no panel login")
    lines.append("- Method: DNS (socket) / TLS / HTTP headers / subdomain enumeration / sensitive-content scan / whois, pure external black box")
    lines.append("- Rating: 🔴 Red (red line / irreversible, escalate now) | 🟡 Amber (risk mitigable or evidence incomplete) | 🟢 Green (no major risk found) | ⚪ Hint (rule note, not a risk rating)\n")
    lines.append("---\n")
    lines.append("## 1. Conclusion summary (8 dimensions)\n")
    lines.append("| Dimension | Rating | Conclusion |")
    lines.append("|---|---|---|")
    rows = [
        ("Domain & resolution", L['dns']), ("TLS certificate", L['tls']), ("HTTP security headers", L['hdr']),
        ("Subdomain exposure", L['sub']), ("Sensitive content", L['content']), ("Compliance (filing/privacy)", L['compliance']),
        ("Registration age", L['age']), ("Market value / traffic", L['value']),
    ]
    for name, (s, t) in rows:
        lines.append(f"| {name} | {icon[s]} | {t} |")

    failed = [label for label, ok in [('DNS', dns_ok), ('TLS', tls_ok),
                                      ('HTTP', http_ok), ('whois', whois_ok)] if not ok]
    if reds:
        summary = f"**{reds} red flag(s) - escalate immediately.**"
    elif failed:
        summary = "**Incomplete evidence: " + ", ".join(failed) + " - related dimensions degraded to 'pending'; this report does NOT constitute a complete conclusion. Re-assess after evidence is completed.**"
    elif yellows:
        summary = "**🟡 Mostly amber, no red flags.**"
    else:
        summary = "**🟢 All green (no major risk found within the evidenced scope).**"
    lines.append(f"\n{summary} See per-item evidence and actionable paths below.\n")

    lines.append("## 2. Per-item evidence\n")
    lines.append("### (1) Domain & resolution")
    v4 = dns.get('v4', []) or []
    lines.append(f"- A records: {', '.join(v4) if v4 else 'not obtained'}")
    v6 = dns.get('v6', []) or []
    if v6:
        lines.append(f"- AAAA: {', '.join(v6[:4])}")
    cdn = dns.get('cdn_hint', []) or []
    if cdn:
        lines.append(f"- A records fall in {' / '.join(cdn)} public edge IP range(s) (**suspected** CDN edge, NOT proof of origin location)")
    rd = http.get('redirect')
    if rd:
        lines.append(f"- Redirect: {rd.get('from')} to {rd.get('to')}")
    lines.append(f"- HTTP status: {http.get('status') if http_ok else 'not obtained'} | Server: {http.get('server') or 'not declared'}")
    if not dns_ok:
        lines.append(f"> Resolution evidence failed: {dns.get('error','')} (no fabricated records)")

    lines.append("\n### (2) TLS certificate")
    if tls_ok and tls.get('not_after'):
        lines.append(f"- Issuer: {tls.get('issuer_org') or '-'} / {tls.get('issuer_cn') or '-'}")
        lines.append(f"- Subject: CN={tls.get('subject_cn') or '-'}; SAN: {', '.join(tls.get('san', [])) or '-'}")
        lines.append(f"- Validity: {tls.get('not_before')} ~ {tls.get('not_after')}, **{tls.get('days_left')} days** remaining")
    else:
        lines.append(f"- Certificate not obtained: {tls.get('error') or 'no 443 service'} (no 'no-risk' conclusion)")

    lines.append("\n### (3) HTTP security response headers")
    if not http_ok:
        lines.append(f"- Evidence failed: {http.get('error') or 'no response headers'} (manual check needed)")
    else:
        present = http.get('security_present', {}) or {}
        lines.append(f"- Present: {', '.join(present.keys()) if present else 'none (all 7 unset)'}")
        lines.append(f"- Missing: {', '.join(missing) if missing else 'none'}")
    lines.append("> Note: reflects the site's current live state; when it differs from history, this run is authoritative - annotate the difference, never force alignment to old values.")

    lines.append("\n### (4) Subdomain exposure")
    if subs:
        lines.append("| Subdomain | HTTP | Same IP as base |")
        lines.append("|---|---|---|")
        for s in subs:
            lines.append(f"| {s.get('host')} | {s.get('http')} | {'yes' if s.get('same_as_base') else 'no'} |")
        lines.append("> Only common subdomains that resolved are listed; not listed does NOT imply absence. Enumeration is a finite set, not exhaustive.")
    else:
        lines.append("- No active hosts resolved in this round's common-name enumeration (does not imply no other subdomains)")

    lines.append("\n### (5) Sensitive content")
    if not http_ok:
        lines.append("- Homepage content not retrieved, cannot scan")
    else:
        lines.append(f"- Private-key headers: {sum(x.get('count',0) for x in pk)} | password/key words: {sum(x.get('count',0) for x in sw)}")
        emails = content.get('emails', []) or []
        lines.append(f"- Public emails: {len(emails)}{(' (' + ', '.join(emails[:5]) + ')') if emails else ''} -> common contact channel, **not equivalent to a leak**")
        ext = content.get('external_links', []) or []
        lines.append(f"- External link domains: {len(ext)} -> {', '.join(ext[:10]) if ext else 'none'}")

    lines.append("\n### (6) Compliance note (rule hint only; no legal opinion)")
    lines.append("- **ICP filing**: the obligation depends on the **server's physical location**. An external black box only sees resolved / edge IPs and cannot confirm the origin's location, so this assessment **does NOT decide whether the site has a filing obligation or must display a filing number**.")
    lines.append("  - Rule: server in mainland China -> MIIT ICP filing obligation; server overseas -> no such obligation. **The domain suffix does not change this rule.**")
    lines.append("  - Exceptions: moving the server back to the mainland, or using a CDN with mainland nodes, re-triggers the obligation; news / medical / finance / education and other special-industry qualifications are not waived by overseas hosting.")
    lines.append("  - Owner to verify: server region in the hosting panel, whether a filing exists, and the footer filing number's ownership (**beware misattribution**: a lookup site may show its own filing number, not the target's; if not found, mark 'not found', never guess the number).")
    lines.append("- **Privacy policy**: assess if user data is collected (pure display sites usually do not); determination belongs to regulators / licensed counsel.")

    lines.append("\n### (7) Registration age (automated whois)")
    if whois_ok and whois.get('created'):
        lines.append(f"- Registered: {whois.get('created')} | Expires: {whois.get('expires') or 'not obtained'}")
        lines.append(f"- Age: ~**{whois.get('age_years')} years** | Registrar: {whois.get('registrar') or 'not obtained'}")
        lines.append(f"- Source: {whois.get('source')} (external whois API; the registrar panel is the authoritative ledger)")
    else:
        lines.append(f"- Registration date not obtained: {whois.get('error') or 'API returned no valid data'} (no fabrication; verify in registrar panel)")

    lines.append("\n### (8) Market value / traffic (data-credibility notes)")
    lines.append(f"**Market value**: there is no authoritative domain-valuation source; third-party estimators are algorithmic or unavailable for non-generic terms / niche suffixes (incl. `.{tld}`), and can differ several-fold to tens-of-fold across sites.")
    lines.append("- This report **gives no market-value figure** - for reference, use a third-party estimator yourself; the result is an estimate only, not an asset-pricing basis.")
    lines.append("**Traffic**: an external black box cannot measure a site's real traffic.")
    analytics = content.get('analytics_scripts', []) or []
    lines.append(f"- Homepage analytics-script signatures: {' / '.join(analytics) if analytics else 'none found'} "
                 "-> the owner should read the real value from the analytics / CDN panel; this item is amber pending, **no fabricated 0 or estimate**.")

    lines.append("\n## 3. Red-flag check")
    lines.append(f"- Sensitive content leak: {'suspected private-key content, verify immediately' if L['content'][0] == 'red' else (L['content'][1] if L['content'][0] == 'amber' else 'none found')}")
    lines.append("- Legal red lines (prohibited endorsements / financing promises): text keywords only; determination needs manual review; no legal opinion given.")
    if all([dns_ok, tls_ok, http_ok]):
        lines.append("- Irreversible risk: DNS/TLS/HTTP evidence normal; no irreversible risk found within the tested scope.")
    else:
        miss = [n for n, ok in [('DNS', dns_ok), ('TLS', tls_ok), ('HTTP', http_ok)] if not ok]
        lines.append("- Irreversible risk: **incomplete evidence (" + ", ".join(miss) + "); an irreversible risk cannot be ruled out on this basis** - re-assess after evidence is completed (do not write 'all normal').")

    lines.append("\n## 4. Actionable paths (amber-item suggestions)")
    lines.append("| Priority | Action |")
    lines.append("|---|---|")
    any_action = False
    if http_ok and missing:
        lines.append(f"| Medium | Add missing security headers ({', '.join(missing[:5])}) |"); any_action = True
    if bad:
        lines.append("| Medium | Clean up anomalous / dangling subdomains (404/530/000) |"); any_action = True
    if sw or pk:
        lines.append("| Medium | Manually review homepage password/key words or private-key content |"); any_action = True
    if not whois_ok:
        lines.append("| Medium | Verify registration & expiry dates in the registrar panel |"); any_action = True
    if failed:
        lines.append(f"| Medium | Complete {', '.join(failed)} evidence, then re-assess this report |"); any_action = True
    lines.append("| Medium | Compliance: owner verifies server region and filing obligation in the hosting panel |"); any_action = True
    lines.append("| Low | Schedule certificate renewal by expiry and monitor" + (" (currently in a CDN edge range; check platform auto-renewal works)" if cdn else "") + " |")
    lines.append("| Low | Traffic: add analytics or supply real data from the panel |")
    if not any_action:
        lines.append("| - | No action items within the evidenced scope |")

    lines.append("\n## 5. Boundaries & discipline")
    lines.append("- Pure external black-box read-only evidence; no panel login, no credentials, no configuration changes.")
    lines.append("- Failed evidence always degrades to 'pending / undetermined'; never filled with 'normal / no risk / no obligation'.")
    lines.append("- Subdomains are a finite enumeration and whois is a third-party API; the registrar / DNS / hosting panel is the authoritative ledger.")
    lines.append("- Compliance is a rule hint only, not a legal opinion; no inference of server physical location or filing obligation.")
    lines.append("- No market-value figure, no fabricated traffic; the hexagram is an Easter egg, not part of conclusions, not a decision basis.")

    # ---------- Xuan-Ping Easter egg ----------
    lines.append("\n---\n")
    lines.append("## Appendix: Xuan-Ping Domain Divination (I-Ching)\n")
    lines.append(f"> **{div.get('signature', '-')}**\n")
    lines.append(f"- Hexagram text: {div.get('gua_ci', '-')}")
    lines.append(f"- Reading: {div.get('fortune', '-')}")
    lines.append(f"- Method: {div.get('method', '-')}")
    lines.append(f"- WARNING: {div.get('disclaimer', 'For entertainment only, not a decision basis.')}\n")
    lines.append("*-- Universal Domain Risk & Xuan-Ping Review, auto-generated (conclusions rest on evidence)*")

    return "\n".join(lines) + "\n"

def main():
    if len(sys.argv) < 3:
        print("Usage: gen_report.py <scan.json> <divination.json> [output.md]", file=sys.stderr)
        sys.exit(1)
    scan = json.load(open(sys.argv[1], encoding='utf-8'))
    div = json.load(open(sys.argv[2], encoding='utf-8'))
    domain = scan.get('domain') or div.get('domain', '')
    report = gen(scan, div, domain)
    if len(sys.argv) > 3 and sys.argv[3].endswith('.md'):
        open(sys.argv[3], 'w', encoding='utf-8').write(report)
        print(f"Report written to {sys.argv[3]}")
    else:
        print(report)

if __name__ == '__main__':
    main()
