---
name: sandbox-selfheal-guard
version: 3.0.8
author: orionshaowswmw
license: MIT
description:
categories: ["Agent Lifecycle categories: ["Agent Lifecycle categories: ["Agent Lifecycle & Governance"] Keep local GGUF/llama.cpp agent sandboxes from hanging after snapshot eviction. Use when: inference hangs or "thinks forever", binaries/models vanished from ~/llama.cpp or failed byte-checks, npx stalls on closed stdin, or sudo might prompt interactively. Governance"] Governance"]
tags: [reliability, sandbox, self-healing, anti-hang, timeout, llama.cpp, gguf, cpu-inference, error-recovery, prompt-cache]
metadata: {"openclaw":{"emoji":"🛡️"}}
---

# sandbox-selfheal-guard 🛡️ v3.0.4

Sandboxes (Arena 128 MB/10k-file snapshots, containers) evict binaries and GGUF
models; small scripts survive and call missing files → agents appear to "think
forever". This skill's scripts detect and repair that **without ever hanging**.

## Consent model (read first — this skill can change a system, so it asks first)

Default `SELFHEAL_MODE=check`: fully **read-only — zero persistent writes**;
probes report to stderr only, and repairs surface as `DRY: would ...` lines.
In `fix` mode events persist to `~/.selfheal/selfheal.log`. Run
repairs ONLY after the human consents: prefix commands with
`SELFHEAL_MODE=fix `. Exact system effects (nothing else is touched):

| Effect | Where | When |
|---|---|---|
| writes | none in check mode; `~/.selfheal/` (log, state, cache), `~/.shim/npx`, model dir (`$SELFHEAL_MODELS_DIR`) in fix mode | fix mode only |
| network | `huggingface.co` only, exact URLs + sha256 pins in `manifest.json` | fix mode, circuit-broken, hash-verified after download |
| system packages | `sudo -n apt-get` (never interactive, stamp-throttled) | fix mode, only if binary missing |
| prompt content | processed locally, stored only in local cache (fix mode) | never sent anywhere |

## Operating protocol (run top-to-bottom; stop at first success)

1. `sh scripts/selfheal_runner.sh preflight` → rc 0 healthy, rc 5 degraded (log has reason), never hangs. Read-only.
2. Answer with `SELFHEAL_MODE=fix sh scripts/run_guarded.sh "PROMPT" ROLE N` (ROLE = `scout`/`spark`/`forge`/`sage`/`auto`; `auto` + ≤8 words = light-swarm scout path **and N is clamped to ≤96**; words = `wc -w` whitespace tokens). In `check` mode this still runs inference if a model already exists, but downloads/heals only with consent.
3. Only if the human's question needs deep reasoning: ROLE=sage (slowest model, longest budget).
4. If output looks stale/wrong: `python3 scripts/prompt_cache.py stats` to inspect; delete `~/.selfheal/cache/` to reset.
5. After any rebuild/model change: `sh scripts/selfheal_tune.sh` → budgets re-derive from *measured* t/s.
6. Verify health anytime: `sh scripts/test_selfheal.sh` (hermetic, never touches real $HOME).

## Files (load only what you need — progressive disclosure)

| File | Load when |
|---|---|
| `manifest.json` | you need model bytes/URLs/roles/timeouts — it is the single source of truth |
| `scripts/selfheal_runner.sh` | you call functions directly (`run_with_timeout`, `selfheal_ensure_model`) |
| `scripts/run_guarded.sh` | one full guarded call: cache → preflight → timeout → fallback |
| `scripts/prompt_cache.py` | cache hits must skip inference entirely |
| `scripts/selfheal_tune.sh` | budgets should match *this* host's real speed |
| `scripts/test_selfheal.sh` | after any edit of this skill |

## Model routing (defaults; budgets auto-scale from measured t/s)

| Role | File | Speed | Use for |
|---|---|---|---|
| scout | Qwen_Qwen3-0.6B-Q4_K_M | ~34 t/s | casual/light-swarm |
| spark | Qwen2.5-0.5B-Instruct-Q5_K_M | ~30 t/s | general instruct |
| forge | Qwen2.5-Coder-0.5B-Instruct-Q4_K_M | ~31 t/s | code |
| sage | DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M | ~14 t/s | deep reasoning only |

Timeout budget = base + n × ms/token, scaled by measured t/s, hard-capped
(150 s light roles, 300 s sage). Inference runs under `timeout --kill-after=5`.
Fallback chain: primary flags → minimal-flags retry → scout → exit 2.

## Hard rules

1. MUST run every inference under `timeout(1)`; if `timeout` is unavailable, refuse (do not run unbounded).
2. MUST verify models by exact bytes **and** leading `GGUF` magic before use (size-only checks accept 15-byte HTML error pages); every **download is additionally sha256-pinned** against `manifest.json` (HF LFS oids — content-addressed, defeats upstream mutation). Deep re-verify of existing files: `SELFHEAL_DEEP_VERIFY=1`.
3. NEVER loop-download a failing model: circuit breaker = 3 failures → suppress downloads 30 min → degrade to another role and tell the human.
4. MUST feature-detect optional flags (`-fa`, `--no-warmup`) from `--help`; never assume.
5. NEVER use interactive `sudo` on stdin-closed sandboxes; use `sudo -n` or skip+warn.
6. MUST log heal events (rebuilds, downloads, breaker trips, cache only) to `$SELFHEAL_HOME/selfheal.log`; state lives outside the package so upgrades keep it.
7. Report **measured** numbers only (t/s, sizes). If unmeasured, say "default (unmeasured)" — NEVER invent a number. All remote facts are in `manifest.json.evidence` with verification method + date.
8. Exit codes are the contract: 0 ok · 2 inference failed · 3 model unavailable · 4 binary unavailable · 5 degraded. Branch on them; do not scrape prose. (`run_guarded.sh` collapses failures after its final fallback to rc 2.)
9. Default mode is `check` (report-only). MUST obtain explicit human consent before `SELFHEAL_MODE=fix`; NEVER silently enable it.
10. MUST rebuild llama.cpp only from a trusted git remote (`github.com/ggml-org/llama.cpp`) — building unverified source is a supply-chain hole. Consent override: `SELFHEAL_LLAMA_ANY_REMOTE=1`.

## Self-improvement loop

`run_guarded.sh` appends wall-clock per call to `state/history.jsonl`;
`selfheal_tune.sh` measures real generation speed per role and EMA-updates
`state/state.json`; `selfheal_budget()` prefers EMA over manifest defaults →
timeouts get *tighter and more accurate* with use, and drift is visible in the
log. Human can reset: delete `~/.selfheal/state/state.json`.

## Compatible agents/models

Any agent runtime with a POSIX shell + coreutils (timeout, curl, wc); python3
optional (only enables JSON manifest parsing, cache, EMA — scripts degrade to
compiled-in defaults without it). No model-specific prompting idioms anywhere;
all commands are copy-paste literal. Works sourced from sh/bash/zsh.
