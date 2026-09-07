# References: Self-improvement loop (load when an exercise ends or a gate fails)

The skill keeps a durable, versioned memory of what went wrong so repeated
failures do not repeat. Storage: feedback.jsonl (append-only, JSONL, one
event per line) in the skill root. Reports: templates/arena_improvement_report.md.

## Protocol
1. After every failed gate (validator FAIL, below-floor, blocked approval,
   aborted exercise), the Scribe logs one line:

      python3 tools/self_improve.py log --event "<short_snake_case>" \
          --area {validate|approval|floor|mode|skill|incident} \
          --context "key=value; key=value"   # redacted; no secrets

2. Before re-running a previously failed check, prime from memory:

      python3 tools/self_improve.py learn --area floor

3. At the end of an exercise or incident, generate the report:

      python3 tools/self_improve.py report
      # writes improvement_report.md from templates/arena_improvement_report.md

4. Apply at most the top actionable items to SKILL.md/references in the next
   version bump; record what changed in CHANGELOG.md (the changelog is the
   long-term memory: every entry cites the feedback evidence).

## Event vocabulary (closed list; add via report review, not ad hoc)
gate_fail · below_floor · approval_blocked · roe_missing · mode_mismatch ·
abort_triggered · redaction_gap · doc_stale · user_confusion · perf_issue

## Rules
- Never log secrets, tokens, prompts, or PII into feedback.jsonl (redaction
  first).
- feedback.jsonl is local-only; it is never uploaded by the skill.
- A report without a version bump is a draft; a version bump without a
  changelog entry is a violation (selftest enforces changelog presence).
