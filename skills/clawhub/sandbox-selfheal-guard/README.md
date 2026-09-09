# 🛡️ sandbox-selfheal-guard

Anti-stuck / anti-snapshot-wipe guard for local-LLM agent sandboxes:
self-verifying preflight, byte+`GGUF`-magic model checks, circuit-broken
downloads, capability-detected rebuilds, measured-throughput timeouts, prompt
cache, and EMA self-tuning budgets. Prevents "agent thinks forever" hangs when
snapshots evict `~/llama.cpp/build` or `*.gguf`.

**Authoritative instructions: `SKILL.md`.** Facts/URLs/bytes: `manifest.json`.
Changes + evidence: `CHANGELOG.md`. Install:

```bash
npx --yes clawhub@latest install @orionshaowswmw/sandbox-selfheal-guard
```

Consent-first: everything is read-only until the human enables `SELFHEAL_MODE=fix`.

Quick check after install: `SELFHEAL_MODE=fix sh scripts/test_selfheal.sh` — 29 hermetic tests
(temp HOME only; no network, real HOME, models, or sudo).
