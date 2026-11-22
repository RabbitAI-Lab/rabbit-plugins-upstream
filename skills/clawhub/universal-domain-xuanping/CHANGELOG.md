# CHANGELOG

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
