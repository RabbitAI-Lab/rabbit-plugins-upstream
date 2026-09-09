# Evidence — standards research behind ruleset 2.0.0 (verified 2026-09-06)

Every claim the engine makes is anchored below. The rule set is deliberately a
**curated, verifiable subset** — we only ship checks we can compute offline
with confidence, and we only cite control IDs that exist in the static
registry.

## OWASP Top 10 for LLM Applications — 2025 edition (citation base)

Stable numbering used by this skill:

| ID | Title | Used by |
|---|---|---|
| LLM01 | Prompt Injection | (registry; reserved for future prompt-surface checks) |
| LLM02 | Sensitive Information Disclosure | SEC-01 |
| LLM03 | Supply Chain Vulnerabilities | DEP-01, MODEL-01 |
| LLM06 | Excessive Agency | NET-01 |

⚠️ **Edition caveat**: OWASP later published a renumbered 2026 edition
(e.g. 2026's LLM03 = Excessive Agency, LLM04 = Supply Chain). This skill cites
**2025** explicitly everywhere — `OWASP-LLM-2025:*` — so refs never become
ambiguous. Bumping editions requires a deliberate registry + ruleset change,
not silent drift.

## OWASP Agentic AI Security — Agentic AI Top 10 (AG01–AG10)

Also grounded during research. Cited:
- **AG04 Insufficient Guardrails** → NET-01 (egress beyond declared boundary).
- **AG07 Repudiation & Audit Gaps** → SEC-01 evidence handling + the
  hash-chained audit trail itself is an AG07 countermeasure.

## NIST SSDF — SP 800-218

- **PW.4** (reuse well-secured software; verify component integrity) → DEP-01:
  unpinned ranges make builds unverifiable/non-reproducible.
- **PS.3** (secure practices: provenance/documentation) → LIC-01.

## CycloneDX 1.5 (ECMA-424) — SBOM shape

Verified structure implemented by `sbom`:
`bomFormat:"CycloneDX"`, `specVersion:"1.5"`, `version:int`,
`serialNumber:"urn:uuid:…"`, `metadata.timestamp` (ISO-8601 UTC),
`metadata.component{type:"application",name,version,bom-ref}`,
`components[]{type:"library",name,version,bom-ref,purl}`,
`dependencies[]{ref,dependsOn[]}`.
Package URLs follow the purl spec: `pkg:npm/%40scope/name@ver`,
`pkg:pypi/name@ver` (lowercased), `pkg:golang/mod@ver`.

## Why SBOMs (regulatory grounding, not marketing)

- **US EO 14028 / CISA-NTIA "minimum elements"**: SBOM expected for federal
  suppliers; CycloneDX and SPDX both satisfy. → `CISA-MIN-ELEMENTS` ref on
  LIC-01/MODEL-01.
- **EU Cyber Resilience Act**: moving toward CycloneDX 1.6+ / SPDX 3.0.1+ for
  CE-marked software — forward pressure to keep the generator upgradable.

## Honest scope — what this skill does NOT do

- **Not a certification.** SOC 2, ISO/IEC 27001, CMMC, and the EU AI Act's
  conformity assessments require accredited auditors and organizational
  controls; no offline linter can grant them. v1 claimed them; v2 removed that.
- **Not a vuln database client.** No network = no CVE lookup; DEP-01 flags
  *unverifiable* (unpinned) deps, which is computable offline and always safe
  to act on. Feed the emitted SBOM to Trivy/Grype/OSV for CVE matching.
- **Pattern coverage is enumerated, not exhaustive**: SEC-01 ships 6 regexes
  (OpenAI-style `sk-…`, GitHub `gh*_[…]`, Slack `xox[baprs]-…`, AWS `AKIA…`,
  GCP `AIza…`, PEM private-key blocks). Everything else is out of scope; add
  patterns by bumping RULESET_VERSION and the selftest together.

## Anti-hallucination mechanism

`CONTROL_REGISTRY` is a literal dict in `bomscan.py`. Before `scan` returns,
the engine asserts every finding ref ∈ registry — else exit 2. The selftest
re-asserts it against `doctor`'s serialized registry (catches serialization
drift). An agent reading output can trust that **every cited control appeared
in the locally-executable registry**, not in model memory.

## Distributed-review adjudication ledger (4 expert lenses, 2026-09-06)

**Adopted (13)** — all merged and covered by the 34-check selftest:

1. requirements.txt env-marker corrupted purls → markers stripped pre-parse;
   URL/VCS/`-e` lines skipped in the SBOM (still DEP-01-flagged).
2. pyproject PEP-621 `dependencies=[...]` arrays were invisible → parser
   extended (arrays + Poetry tables); DEP-01 now asks the SBOM parser (single
   source of truth) for UNPINNED pyproject comps.
3. go.mod regex fragile/comment-prone → line-based parser; `// indirect`,
   `module`/`go`/`toolchain` lines handled.
4. go.mod `replace`/`retract` unflagged → new **GO-01** LOW rule.
5. NET-01 `endswith` blessed `badexample.com` under declared `example.com` →
   boundary match `u==h or u.endswith("."+h)`.
6. `outbound: [*]` wildcard silently allowed all egress → wildcard/empty
   declared hosts collapse to "nothing declared" (strict, not lax).
7. IP-literal URLs bypassed NET-01 → IPv4 literals now detected and flagged.
8. only http(s) scanned → schemes extended to ftp/sftp/ssh/git/ws/wss.
9. SEC-01 redaction leaked first4…last2 of the secret (oracle) → zero-char
   `[REDACTED len=N sha256:TAG]`; selftest scans output for any 8-char window
   of the fixture secret.
10. audit file had a create→chmod looser-perm race + symlink-swap write
    primitive → `os.open(O_NOFOLLOW)` + atomic `fchmod(0600)` at create.
11. keyless-chain limits (append/tail-truncate under full local compromise)
    were implicit → monotonic `seq` added + explicit limit docs + out-of-band
    head-hash snapshot recipe.
12. npm DEP-01 heuristics missed `>=` ranges/tags/git/file specs → "pinned =
    exact `x.y.z` only" predicate.
13. Duplicate `bom-ref`s across manifest files violated CycloneDX uniqueness
    (poison for downstream tools) → dedupe + collision-safe
    `root:name@version`; output-write failures now exit 3 (was a crash).

Also corrected from review: manifest `control_registry` range claim
(`LLM01..LLM10` → the actual four), LIC filename variants, docs-claim
"unique bom-ref".

**Rejected (8)** — with reasons, so they are not re-litigated:

- *go.mod block form never matches* — disproven by the passing cobra-in-block
  fixture test (the multiline regex worked); only the legitimate tightening
  (#3) was kept.
- *pyproject regex "catastrophic backtracking"* — reviewer self-withdrew;
  anchored linear regex, no nested quantifiers.
- *walk_files symlink loops forever* — `os.walk(followlinks=False)` default
  does not recurse symlinked dirs; cycles impossible.
- *suppress file paths from exception text* — paths are operator-visible by
  necessity (findings must be actionable); secrets, not paths, were the leak
  surface (fixed via #9).
- *drop `evidence.file/line` to avoid an "oracle"* — file:line is the
  remediation contract; zero-char redaction removes the sensitive part.
- *HMAC-sign the audit chain with an external key* — turns a zero-config
  offline tool into key-management machinery; replaced by documented
  out-of-band head-hash anchoring (#11).
- *extract secrets from binary formats (.docx/.onnx metadata)* — out of
  scope for a text-tree scanner; documented in operations.md scope honesty.
- *follow `-r` requirement includes recursively* — include graphs can leave
  the audited tree; documented as skipped rather than half-implemented.
