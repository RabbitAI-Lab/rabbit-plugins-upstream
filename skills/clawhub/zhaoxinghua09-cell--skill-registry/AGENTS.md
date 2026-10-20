# AGENTS.md — skill-registry

Machine-readable entry for AI agents.

## Purpose
One command to know exactly what skills you have.

## Invocation
```bash
python scripts/registry.py <skills-dir> [--out registry.json] [--md registry.md]
```

## Output contract
- Structured JSON via `--json`; exit 0 = PASS, 1 = FAIL (fail-closed).
- Never publishes or deletes; analysis only.

## Rules
- No placeholders in outputs.
