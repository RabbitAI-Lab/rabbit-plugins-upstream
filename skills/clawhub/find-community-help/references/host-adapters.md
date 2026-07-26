# Host Adapters

Optional. Skip for normal manual use.

## Shared policy

- Semantic trigger required; delivery windows are not triggers
- Public-only by default
- Chat-visible, current-response scoped
- Do not read old suggestion channels later
- Host owns quiet windows, rate limits, and any search execution

## Host notes

- **OpenClaw**: heartbeat/task-end/scheduled only after semantic gate; keep redacted and quiet
- **Hermes / Codex-style**: progressive disclosure; keep `disable-model-invocation`; manual invoke for one-off plans
- **Any host**: this package is Markdown-only; no runtime scripts ship with the skill
