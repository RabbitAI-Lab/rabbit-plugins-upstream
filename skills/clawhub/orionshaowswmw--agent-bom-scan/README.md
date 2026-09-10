# 🔍 Agent Bom Scan

**Categories:** security  
**Public tags:** #security, #sbom, #dependency-scanning, #cve, #supply-chain

## ✨ Functionalities

A **working** BOM vulnerability scanner (v2.0.0 full rebuild of the v1.x
hollow package):

- Parses 8 lockfile formats into a BOM: `package-lock.json` (v1+v2/v3),
  `requirements.txt`, `Pipfile.lock`, `go.sum`, `Cargo.lock`,
  `Gemfile.lock`, `composer.json`, `pom.xml`
- Matches versions against an embedded, versioned, **OSV-verified** advisory
  DB (34 records; curated subset for offline use)
- CVSS 3.1 base scores computed at runtime from the vector (formula verified
  against NVD ground truth)
- Offline by default (zero network, socket-layer proof in the self-test);
  explicit `--mode online` queries `api.osv.dev` with name+version+ecosystem
  only (batch endpoint, MAL- malicious-package records flagged)
- Provenance-stamped, machine-readable findings (`findings.json`,
  `bom_report.md`) + key=value summary
- Self-improvement feedback loop (`tools/bom_improve.py`)
- 12-group offline self-test with functional fixtures and expected advisory
  ids (`tools/bom_selftest.py`)

The v1.x package advertised these capabilities with no implementation
("Follow the skill instructions to use this skill") and contained
contradictory privacy claims (fully-offline in SKILL.md, network queries in
README) — the registry's own skill card flagged the inconsistency. v2.0.0
makes every claim verifiable.

## 🚀 Usage

Install the skill from ClawHub:

```bash
npx --yes clawhub@latest install @orionshaowswmw/agent-bom-scan
```

Representative commands (all local, deterministic, stdlib-only):

```bash
# Scan an authorized project (offline, curated DB)
python3 scripts/bom_scan.py scan /path/to/project --severity-floor high
# -> key=value summary + bom_scan_out/{bom.json,findings.json,bom_report.md}

# Build a BOM only (no matching, no network)
python3 scripts/bom_scan.py bom /path/to/project

# Full coverage (explicit; sends name+version+ecosystem to api.osv.dev)
python3 scripts/bom_scan.py scan /path/to/project --mode online

# Self-check + full package self-test
python3 scripts/bom_scan.py check
python3 tools/bom_selftest.py
```

Exit codes: 0 CLEAN, 10 FINDINGS, 2 usage, 3 fatal.

## 🔐 Permissions & Requirements

• Read access to the project's lockfile/manifest files only
• python3.8+ (standard library only — nothing is pip-installed)
• Network access **only** in explicit `--mode online`, to `api.osv.dev`
  (name + version + ecosystem per package; nothing else)

All permissions above are capability requirements, not blanket
authorization. Grant only what the selected workflow needs, scope filesystem
access to the assessed project, and do not elevate privileges.

## 🔒 Security & Privacy

- **Offline mode (default): no network calls at all.** The self-test runs a
  scan with the socket layer disabled to prove it.
- **Online mode (explicit opt-in):** only `name`, `version`, `ecosystem`
  per package leave the machine, to `api.osv.dev`. Never sent: file paths,
  lockfile contents, source code, hashes, credentials, hostnames.
- No credentials are stored or sent by the skill.
- The advisory DB is a curated subset (34 OSV-verified records): a clean
  offline result is *no data*, not *no vulnerabilities*. Use online mode for
  a real clearance.
- **Data handling:** the skill reads only lockfile/manifest files of the
  project you point it at; it must not collect unrelated data.
- **Storage/logging:** reports and `feedback.jsonl` live in your working
  area and may contain sensitive dependency details; protect them.
- **Secrets:** API keys, tokens, passwords, and credentials must never be
  embedded in the skill or logged; the scanner's own scans for them in its
  self-test.
- **Risks and mitigation:** scan only projects you are authorized to assess;
  review every finding's provenance (advisory id + range + db hash) before
  acting.

## ✅ Verification Hash

TREE-SHA256-v1 over all package files except `README.md` and server-managed
files (`_meta.json`, `.clawhub/`), generated at publish time:

**Artifact SHA-256 (TREE-SHA256-v1):** `68197b411f90d878ab64a6d7f18e60a5293c4c12786ce84dc8f6c9349ce34b1a`

Run from the installed skill directory:

```bash
python3 - <<'PY'
from pathlib import Path
import hashlib
root = Path('.')
excluded_parts = {'.git', '.clawhub', '__pycache__', '.pytest_cache'}
excluded_names = {'readme.md', 'skill-card.md', '_meta.json', '.published', '.ds_store'}
files = sorted(
    (p for p in root.rglob('*') if p.is_file()
     and not any(part in excluded_parts for part in p.relative_to(root).parts)
     and p.name.lower() not in excluded_names),
    key=lambda p: p.relative_to(root).as_posix(),
)
h = hashlib.sha256()
h.update(b'TREE-SHA256-v1\0')
for p in files:
    rel = p.relative_to(root).as_posix().encode('utf-8')
    data = p.read_bytes()
    h.update(rel); h.update(b'\0')
    h.update(str(len(data)).encode('ascii')); h.update(b'\0')
    h.update(data); h.update(b'\0')
print(h.hexdigest())
PY
```

The printed digest must exactly match the value above. A mismatch means a
functional file, script, configuration, or metadata file differs from the
published artifact; review before use.
