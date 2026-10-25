---
name: document-engine
slug: document-engine
version: 1.0.2
displayName: Document Compliance Audit Engine
description: "Deterministic, offline compliance audit engine for Chinese business documents (contracts / regulations / official docs / generic). Pure Python standard library, zero third-party dependencies, no network, no LLM. Pipeline: segmentation -> clause-level rule scan -> document-level audit (completeness / consistency / rights-duty balance / official-doc format) -> responsibility anchoring -> scoring -> HTML / JSON / Markdown report. All verdicts are deterministic (a hit is a verdict); no probability estimates are ever emitted. Ships 15 built-in rules (generic + per-type) and supports external rule directories via --rules-dir. Fully local: reads only the input file you pass, writes only the report file you name."
required_commands:
  - python3
metadata:
  openclaw:
    required_binaries:
      - python3
    emoji: "📄"
    homepage: "https://github.com/nohn3043-arch/Story-engine"
    envVars: []
---

# Document Compliance Audit Engine · Document Engine

Deterministic compliance auditing for Chinese business documents: **pure rule base, zero third-party dependencies, fully offline, Python standard library only**.
Feed it one document (contract / regulation / official doc / generic) and get a score, a findings list (with severity, matched snippet, and fix suggestion) plus a traceable audit chain. Reports come in HTML / JSON / Markdown.

> **Verdict policy**: every verdict is deterministic — a hit is a verdict; no probability estimates are ever emitted. Scoring: WARNING −5 / CRITICAL −15 / FATAL −30; any FATAL or CRITICAL finding fails the audit (and the total score must be ≥ 60 to pass).

## When to use

- Review contracts, regulations, official documents, or generic Chinese business documents and need a reproducible findings list
- Run in an offline / intranet environment where no external API or LLM may be called
- Need structured (JSON) audit output for system integration, or a visual (HTML) report for sharing
- Need clause-level scanning against a custom rule base (`--rules-dir`)

## Declared Capability Scope

| Capability | Scope | Note |
|---|---|---|
| Document types | contract / regulation / official_doc / generic | set via `--type` |
| Clause-level rule scan | 15 built-in rules (3 generic + 5 contract + 3 regulation + 3 official_doc) | keyword hits + regex hits |
| Document-level audit | completeness / consistency / rights-duty balance (contracts) / official-doc format | cross-paragraph checks |
| Responsibility anchoring | every report binds a named responsibility node (Compliance-Core / ComplianceAuditor) plus a full trace | `trace` inside the report |
| Report formats | HTML (single file, shareable) / JSON (system integration) / Markdown (archival) | `--format`, or inferred from `--output` extension |
| Custom rules | `--rules-dir` pointing at an external JSON rule directory | format in references/RuleCatalog.md |
| Network / LLM / subprocess | **none** | no network requests, no external models, no child processes |

## How to run

The script lives at `scripts/document_engine.py` (single file, embedded rule base).

```bash
# 1) Audit a contract, HTML report out
python3 scripts/document_engine.py audit --type contract --input contract.txt --output report.html

# 2) Audit a regulation, JSON out (for system integration)
python3 scripts/document_engine.py audit --type regulation --input policy.txt --format json

# 3) List the rule base for a type
python3 scripts/document_engine.py list-rules --type contract

# 4) Built-in demo (three sample documents with compliance issues, all three report formats)
python3 scripts/document_engine.py demo --output-dir ./out

# 5) Use a custom rule directory
python3 scripts/document_engine.py audit --type contract --input contract.txt --rules-dir ./my_rules
```

The verdict is also printed to stdout: score, pass/fail, finding count, severity distribution, and every finding.

## Requirements

| Dependency | Version | Purpose |
|---|---|---|
| Python | 3.8+ | the only runtime (stdlib: argparse / json / re / uuid / dataclasses / datetime / pathlib / typing) |
| Third-party packages | none | zero dependencies |
| Network | not required | fully offline |
| Environment variables | none | no environment variable is read |

## Security & Privacy

- **Pure local computation**: reads only the file given by `--input`, writes only the file named by `--output`; no network access, no data upload.
- **No credential access**: does not read environment variables, config files, SSH keys, tokens, or passwords.
- **No subprocesses**: no shell invocation, no external commands, no dynamic code evaluation.
- **No randomness in verdicts**: only the timestamp and the trace-chain UUID are generated at runtime; every audit verdict and score is reproducible for the same input.

## File structure

```
document-engine/
├── SKILL.md                        # this file
├── README.md                       # project readme
├── scripts/
│   └── document_engine.py          # single-file engine (embedded rule base + CLI + demo)
├── references/
│   ├── RuleCatalog.md              # rule catalog (incl. custom rule JSON format)
│   └── UsageGuide.md               # detailed usage and report field reference
└── examples/
    ├── sample_contract.txt         # sample input (with several compliance issues)
    └── sample_report.md            # sample output (Markdown report)
```
