# AGENTS.md — prompt-injection-guard

Machine-readable entry for AI agents.

## Purpose
Fail-closed prompt injection / malicious-instruction scanner with threat taxonomy.

## Invocation
```bash
python scripts/prompt_guard.py <file|text> [--json] [--badge out.svg]
```

## Output contract
- Structured JSON available via `--json` (fields: verdict, score, sha256_8, hits).
- Exit code: 0 = PASS, 1 = FAIL (fail-closed).

## Rules
- Static analysis only; never executes external commands.
- FAIL verdict requires human decision before proceeding.
- No placeholders in outputs.
