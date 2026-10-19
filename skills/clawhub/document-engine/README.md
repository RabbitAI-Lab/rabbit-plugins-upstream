# Document Compliance Audit Engine · Document Engine

A deterministic compliance audit engine for Chinese business documents. Pure Python standard library, zero third-party dependencies, fully offline.

## Features

- **Clause-level rule scan**: 15 built-in rules covering generic wording standards, contract risk clauses and compliance red lines (minimum wage / penalty cap / unpaid overtime), regulation duty & permission boundaries, and official-document format standards
- **Document-level audit**: element completeness (6 contract / 6 regulation / 4 official-doc elements), same-assignment contradiction detection, contract rights-duty balance detection, official-document document-number and date checks
- **Responsibility anchoring**: every report binds a named responsibility node and a fully traceable audit log
- **Three report formats**: HTML (self-contained single file, shareable) / JSON (system integration) / Markdown (archival)

## Quick start

```bash
python3 scripts/document_engine.py audit --type contract --input contract.txt --output report.html
python3 scripts/document_engine.py demo --output-dir ./out
```

Document types: `contract`, `regulation`, `official_doc`, `generic`.

## Verdict policy

- A hit is a verdict; no probability estimates
- Scoring: WARNING −5 / CRITICAL −15 / FATAL −30 (100 max, floored at 0)
- Pass condition: score ≥ 60 **and** no FATAL / CRITICAL findings

## Custom rules

Point `--rules-dir` at a directory of JSON rule files; format in [references/RuleCatalog.md](references/RuleCatalog.md).

## License

MIT
