# Quota-Aware Provider Registry — design notes

**Session date:** 2026-07-16
**Status:** Spec written, not yet implemented.
**Spec location:** `/home/chpo/.hermes/skills/adversarial-spec/spec.md`

## Core principle

The adversarial pipeline (code-loop, spec, plan) is a **model-agnostic orchestration
framework**. It knows roles (dev, review, verify, arbiter, writer, challenger) but
never knows what "Claude" or "Codex" are. Provider selection is entirely external.

## Architecture

```
User's config                         Pipeline runtime
┌──────────────────────┐              ┌─────────────────────┐
│ providers.yaml       │  --provider-config   │ quota.py            │
│                      │ ──────────────────→  │                     │
│ dev:                 │              │  - load_config()     │
│   - alias: claude    │              │  - check_quotas()    │
│     cmd: "..."       │              │  - select_best()     │
│   - alias: codex     │              │  - cache (30s TTL)   │
│     cmd: "..."       │              │                     │
│ review:              │              │ runner.py            │
│   - alias: claude    │              │  - run_phase()       │
│     cmd: "..."       │              │    → check quota     │
│   - alias: deepseek  │              │    → pick cmd        │
│     cmd: "..."       │              │    → execute         │
└──────────────────────┘              │    → log to report   │
                                      └─────────────────────┘
```

## Key design decisions

1. **Config is 100% external.** No skill ships a default `.adversarial-providers.yaml`.
   The config file lives at `~/.config/adversarial/providers.yaml` by default,
   overridable via `--provider-config` flag or `ADVERSARIAL_PROVIDER_CONFIG` env var.

2. **Roles are fixed — providers are not.** The pipeline knows about these roles:
   dev, review, verify, arbiter, writer, challenger. The user maps each role to
   as many provider commands as they want, in preference order.

3. **Quota check before every phase.** `check-ai-quota.py --json` is called once
   per cache TTL (default 30s) in parallel for all known providers. Returns a
   state per alias: OK, DRAINING, RATE-LIMITED, KEY_INVALID, UNKNOWN.

4. **Fallback is automatic, not manual.** If the first provider in the chain is
   RATE-LIMITED, the resolver picks the next one automatically. The user no longer
   has to manually check quotas and edit `--review-cmd` mid-pipeline.

5. **Explicit CLI flags override config.** `--dev-cmd "codex ..."` bypasses quota
   checking for that role entirely. This preserves backward compatibility and allows
   one-off overrides without editing the YAML.

6. **`{workdir}` placeholder substitution.** Commands that need `--cwd` (like
   claude-tmux) use `{workdir}` in the config, which the resolver replaces with
   the actual workdir at runtime.

## User config (chpo's personal setup)

Stored at `/home/chpo/.config/adversarial/providers.yaml`:

| Role | Primary | Fallback 1 | Fallback 2 |
|------|---------|------------|------------|
| dev | Codex | GLM-5.2 | — |
| review | Claude Sonnet (tmux) | DeepSeek V4 Pro | GLM-5.2 |
| challenger | Claude Sonnet (tmux) | DeepSeek V4 Pro | — |
| arbiter | Claude Sonnet (tmux) | — | — |
| writer | Codex | GLM-5.2 | — |

## Quota checker gap

`check-ai-quota.py` (in adversarial-code-review/scripts/) supports `--claude`,
`--codex`, `--gemini` flags. GLM (Z.AI) and DeepSeek quota functions exist in
`quota_api.py` (the plugin) but are NOT wired into the CLI wrapper yet.
Until wired, those providers are treated as UNKNOWN (used anyway with a warning).

## v2 ideas (not in scope for initial implementation)

- Automatic retry after quota reset
- Quota-aware step scheduling (reorder steps to fit within windows)
- Cost-aware provider selection (prefer cheaper when within quota)
- Cross-pipeline quota coordination (two concurrent pipelines)
- HTML quota dashboard
