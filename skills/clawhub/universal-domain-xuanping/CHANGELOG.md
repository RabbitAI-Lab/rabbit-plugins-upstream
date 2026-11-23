# CHANGELOG

## 1.2.1 (2026-11-23)

- **U4 - region-first ICP judgment**: added a `hosting` suspected-region hint (from matched CDN ranges, "suspected" only, NOT proof of origin). Judge server region before ICP: overseas (incl. suspected overseas CDN edge) usually has no ICP filing obligation, so an absent filing number on the page is normal - NOT a risk, no urging, no action item; mainland -> owner verifies; region unknown -> neutral self-check.
- Removed the previous unconditional "no filing number on page -> please verify whether filed" urging; a missing number alone never yields an amber rating.
- Compliance-publicity hint text and the actionable-paths section updated accordingly; compliance stays a permanent ⚪ hint, excluded from RAG scoring.

## 1.2.0 (2026-11-23)

- **U3 - compliance-publicity read-only evidence**: added ICP / public-security filing-number regex, privacy policy / terms / disclaimer keywords, Set-Cookie, and HTTP->HTTPS redirect checks. All report page 'present / absent' facts only; absence != violation / no obligation, no legal opinion.
- HTTPS enforcement probe corrected to check the ACTUAL SERVICE HOST (final_url netloc), not the input bare domain (a bare domain may redirect to https while the www host does not - opposite conclusions).
- Added `compliance` / `http_https` / `hosting` fields and matching evidence-completeness flags; extended the compliance dimension and its rule notes.

## 1.1.0 (2026-11-22)

- **Universalization refactor**: all conclusions driven by evidence JSON; removed every site-specific fact (hard-coded IP / CDN name / server geography / suffix).
- Failed evidence degrades to "pending / undetermined"; never "normal / none found / no obligation".
- Compliance is now a permanent rule-hint item; no decision on any site's filing obligation.
- Fixed whois Unix-second timestamp parsing for gTLDs; fixed the red-flag count unpack bug.
- Subdomain enumeration made purely generic; public emails no longer false-positive red; CDN auto-renewal hint made conditional.
- Added the deterministic I-Ching "Xuan-Ping" divination Easter egg (SHA256 -> 64 hexagrams + moving line); entertainment only, not part of conclusions.
- No market-value figure (no authoritative source); traffic marked "pending owner-supplied data".

## 1.0.0

- Initial: 8-dimension RAG assessment, single-site regression passed (later universalized in 1.1.0).
