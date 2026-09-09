# Operations — bomscan.py command reference

All commands print JSON to stdout (nothing to stderr except hard errors) and
run fully offline. `DIR` is the project tree under audit.

## doctor

    python3 scripts/bomscan.py doctor

`agent_bom.doctor.v1`: python version, `spec` (CycloneDX 1.5), `ruleset`
version, the full static `controls` registry (every control ref the engine is
*allowed* to cite), and supported manifests. Use it to sanity-check an install.

## sbom — CycloneDX 1.5 generation

    python3 scripts/bomscan.py sbom DIR [-o OUT.json] [--name N --version V]

Parses per tree: `package.json` (+ `package-lock.json` — **locked versions win
over ranges** in the emitted purl), `requirements.txt` (PEP-508 env-markers
like `pkg==1.0; python_version<"3.9"` are stripped so purls stay valid),
`pyproject.toml` (PEP 621 `[project] dependencies=[...]` arrays **and**
Poetry `[tool.poetry.dependencies]` tables), `go.mod` (`require x v` lines and
`require ( ... )` blocks; `replace`/`retract` handled by GO-01, not the SBOM).
Emits raw CycloneDX 1.5 JSON (ECMA-424 shape):

- `bomFormat/specVersion/version/serialNumber (urn:uuid)`
- `metadata.timestamp`, `metadata.component` (root application; `--name`/
  `--version` override, else package.json name/version, else dir basename;
  bom-ref `root:name@version`)
- `components[]` — `type:library`, `bom-ref` (**deduped across manifests** —
  CycloneDX requires uniqueness), `purl`
  (`pkg:npm/…`, `pkg:pypi/…`, `pkg:golang/…`; npm scope `@` → `%40`)
- `dependencies[]` — root → all components

Unpinned deps get a bare purl (`pkg:pypi/requests`, `pkg:pypi/zope.interface`)
— a visible signal that pairs with rule `DEP-01`. With `-o`, prints small
`agent_bom.sbom.v1` summary JSON and writes the document to `OUT.json`;
unwritable output paths exit **3**, they do not crash or silently pass.

## scan — verifiable rule engine

    python3 scripts/bomscan.py scan DIR [--fail-severity INFO|LOW|MEDIUM|HIGH|CRITICAL]

`agent_bom.scan.v1`: `summary` counts per severity, `verdict`
(`PASS/WARN/FAIL`), full `findings[]` with `rule`, `severity`, `control_refs`,
`title`, `evidence {file,line}`, `remediation`, plus the `controls` registry.
**Exit 4 iff verdict FAIL** (i.e. any finding at/above `--fail-severity`,
default HIGH).

| Rule | What it verifies | Severity | Control refs |
|---|---|---|---|
| SEC-01 | committed secrets (OpenAI/GitHub/Slack/AWS/GCP key patterns, private-key block headers); **zero-character redaction** `[REDACTED len=N sha256:TAG]` | HIGH | OWASP-LLM-2025:LLM02, OWASP-AGENTIC:AG07 |
| DEP-01 | unpinned deps: npm anything that isn't exact `x.y.z` (npm treats `"1.2"` as a range); pip lines without `==`; pyproject deps via the SBOM parser (PEP-621 arrays + Poetry tables) | MEDIUM | OWASP-LLM-2025:LLM03, NIST-SSDF:PW.4 |
| NET-01 | URLs (http/https/ftp/sftp/ssh/git/ws/wss **+ IP literals**) vs hosts declared in SKILL.md `metadata.network.outbound`. Boundary-safe match: `u==h or u.endswith("."+h)`; `outbound:[*]` collapses to "nothing declared" (strict) | MEDIUM | OWASP-LLM-2025:LLM06, OWASP-AGENTIC:AG04 |
| MODEL-01 | model artifacts (.gguf/.safetensors/.bin/.pt/.pth/.ckpt/.onnx/.h5) in tree without declared provenance | LOW | OWASP-LLM-2025:LLM03, CISA-MIN-ELEMENTS |
| LIC-01 | no LICENSE*/LICENCE*/COPYING file in tree | LOW | NIST-SSDF:PS.3, CISA-MIN-ELEMENTS |
| GO-01 | go.mod `replace`/`retract` directives — local-path forks redirect module resolution | LOW | OWASP-LLM-2025:LLM03, NIST-SSDF:PW.4 |

The engine `assert`s every emitted `control_ref` ∈ registry (trip → exit 2):
**a hallucinated control citation is a hard-stop, not a cosmetic bug.**

Scope honesty for SEC-01/NET-01: SEC-01 scans text extensions only (no binary
parsers — a credential embedded inside a `.docx`/`.onnx` blob is out of scope);
NET-01 only governs schemes with a host part (data:/file: aren't egress).

## report — verdict + audit entry

    python3 scripts/bomscan.py report DIR [-o OUT.json] [--fail-severity SEV]

Runs sbom+scan, emits `agent_bom.report.v1` (`verdict`, `summary`,
`report_sha256`, SBOM component-count synopsis). With `-o`: full report to
`OUT.json` + full SBOM sidecar `OUT.json.sbom.json` (unwritable → exit 3).
Appends a hash-chained record to `${AGENT_BOM_AUDIT:-DIR/.agent_bom_audit.jsonl}`
— created `O_NOFOLLOW` (symlink-swap safe) with mode 0600 set via `fchmod` at
create time (no looser-perm window): `{ts,seq,target,ruleset,summary,prev,hash}`,
`hash = SHA256(record-without-hash)`, `prev = previous record's hash`
(genesis = 64 zeros), `seq` = monotonic record index for forensic gap-spotting.
If the ledger is unwritable the run proceeds with a stderr warning and is
explicitly *unaudited* (no silent audit skip). Exit 4 on FAIL.

**Audit-chain guarantees, stated plainly.** The chain is **keyless tamper
evidence**: `audit --verify` proves no existing record was modified, deleted
from the middle, or reordered. It does **not** stop an attacker with
read+write on this file from truncating the tail or appending
forged-but-consistent records — that needs an external anchor: snapshot
`tail -1 .agent_bom_audit.jsonl | sha256sum` somewhere the attacker can't
reach (CI artifact, git notes) after each gating run. Point
`AGENT_BOM_AUDIT` only at paths you own; it is a relocation convenience, not
a trust boundary.

## trend — self-improving signal

    python3 scripts/bomscan.py trend DIR

Compares the last two audited runs for the same target: `open_prev`,
`open_now`, `net`, verdicts, `direction` = IMPROVED (net<0) / UNCHANGED /
REGRESSED (net>0). **REGRESSED exits 1** — wire it after `report` in CI to
fail builds that add findings. Fewer than 2 runs → honest note, exit 0.

## audit — inspect / verify the chain

    python3 scripts/bomscan.py audit DIR [--verify]

Without `--verify`: dumps parsed entries. With: recomputes every hash+link;
prints `chain_ok`, `entries`, `bad_lines[]`; **exit 4 on any tamper**.

## Recipes

**CI gate** (fail on HIGH+, and on any regression):

    python3 scripts/bomscan.py report "$PWD" >/dev/null || exit 1  # rc 4 = FAIL
    python3 scripts/bomscan.py trend  "$PWD" >/dev/null || exit 1  # rc 1 = REGRESSED

**Pre-publish audit of a skill folder:**

    python3 scripts/bomscan.py scan ~/.clawhub/skills/<slug> --fail-severity MEDIUM

**SBOM for a downstream scanner:**

    python3 scripts/bomscan.py sbom . -o sbom.json   # then: trivy sbom sbom.json …

## Notes

- Skips `.git`, `node_modules`, `__pycache__`, `.venv`/`venv`, `dist`, `build`,
  `.cache`, `coverage`, `out`, `target`, `.next` etc. — intentional: secrets
  inside a developer's local `.venv` are outside a repo-compliance signal;
  audit the *tree under review*, not the machine's residue.
- The engine excludes files ending in `bomscan.py` from SEC-01 — its own
  regex literals are not findings.
- `trend`/`audit` key runs by **absolute path of DIR**; rename a dir → history
  restarts.
