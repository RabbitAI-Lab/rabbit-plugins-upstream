---
name: sandbox-selfheal-guard
version: 1.1.0
description: >
  Anti-stuck/anti-snapshot-wipe guard for agentic sandboxes (Arena.ai Agent Mode,
  OpenClaw, and similar containerized agent environments). Detects missing
  binaries, GGUF models, apt packages, and npx shims caused by snapshot
  size-cap eviction and automatically self-repairs before work proceeds.
  Provides per-call hard timeouts, byte-verified model downloads, native-CPU
  rebuild, binary fallback chains, and light-swarm mode so the agent never
  silently hangs. Use in any agent sandbox where build artifacts, model files,
  or system packages may disappear between turns due to filesystem snapshot
  limits.
author: orionshaowswmw
license: MIT
tags:
  - reliability
  - agent-safety
  - sandbox
  - self-healing
  - anti-hang
  - timeout
  - snapshot-wipe
  - llama.cpp
  - cpu-inference
  - error-recovery
allowed-tools:
  - Read
  - Write
  - Edit
  - Bash
  - Grep
  - Glob
---

# sandbox-selfheal-guard 🛡️⚡

**Problem solved:** Agent sandboxes (Arena.ai Agent Mode, OpenClaw, containerized
agent runners) often evict large binaries — compiled build dirs, multi-GB model
files, even apt packages — when the workspace snapshot cap is exceeded (e.g.
128 MB / 10k-file limit on Arena). The agent's shell scripts still exist (small
text files survive) but they silently invoke missing binaries → the agent
appears to "think forever" and the user has to manually stop it.

## Symptoms you are hitting this
- Agent appears to "think forever" with no output
- Previously-working scripts suddenly produce "No such file or directory"
- `cmake`/`g++` disappear between turns
- `llama.cpp/build/bin/*` vanish (`build/` is commonly on excluded-paths lists)
- GGUF models > ~100 MB get evicted by snapshot-size cap
- npx hangs on first run (missing `--yes` shim for non-interactive stdin)

## Core recipe: pre-flight self-heal + per-call timeout

Build a single sourced shell library (`selfheal_runner.sh`) that every model
invocation must go through. It performs a pre-flight checklist BEFORE running
the model:

1. **apt packages** — verify `cmake`, `g++`, `curl` exist; `apt-get install` if missing
2. **npx shim** — ensure `~/.shim/npx` exists with `--yes` flag (prevents interactive hang)
3. **llama.cpp binaries** — verify `llama-completion` is executable; if not,
   reconfigure (with `-DLLAMA_NATIVE=ON -DCMAKE_BUILD_TYPE=Release -DLLAMA_BUILD_SERVER=OFF`)
   and rebuild all four targets (`llama-simple`, `llama-completion`, `llama-bench`,
   `llama-simple-chat`) in parallel
4. **GGUF models** — verify each model file exists AND has exact expected byte size
   (size manifest below); if missing or truncated, redownload with `curl -sSL`
5. **Auth tokens** — verify `~/.clawhub/TOKEN` exists; re-login if needed

Then wrap every model call in a **hard `timeout`** scaled to model speed and
token budget, so even a wedged binary returns control:
- r1 (1.5B deep, ~13 t/s): budget = 45s + n/10
- q3/fast/code (0.5–0.6B, ~30 t/s): budget = 30s + n/20
- Absolute cap: 300s

Add a **binary fallback chain**: try `llama-completion` (full tuning flags) first,
fall back to `llama-simple` (simple argv interface) if unavailable; exit code
2 if nothing works so the agent reports failure instead of hallucinating.

## Optimal CPU llama.cpp params (control-variable sweep)

Measured on 2 vCPU Intel Xeon @ 2.60 GHz with AVX-512. Native build gives
+7–10% prompt processing over generic march.

| Param | Best | Why |
|---|---|---|
| `-t` (threads) | **= physical cores (2)** | t=4 oversubscribes; tg drops 42% |
| `-fa` (flash-attn) | **on** | pp +11%, tg +19% on small models |
| `-ctk/-ctv` (KV cache type) | **f16 (default)** | q8_0 slows pp by 35–50% on CPU |
| `-b` (batch) | default 2048 | no-op on CPU (±2.4% noise) |
| quant choice | newer-arch Q4_K_M > older Q5_K_M | architecture > quant level for speed |
| build flags | `-DLLAMA_NATIVE=ON` | AVX512/VNNI gives +7-10% pp |

Invocations use: `llama-completion -m model.gguf --prompt "..." -n N -t 2 -fa on --ctx-size 4096`

## Model byte-size manifest (verification!)

| File | Exact bytes | Role |
|---|---|---|
| Qwen2.5-0.5B-Instruct-Q5_K_M.gguf | 420,086,080 | SPARK (fast independent take) |
| Qwen3-0.6B-Q4_K_M.gguf | 484,220,320 | SCOUT (fast draft) |
| DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf | 1,117,320,800 | SAGE (deep verify) |
| Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf | 397,808,288 | FORGE (coding spec) |

Mismatch = redownload (truncated/corrupted). Always stat+compare, don't just check existence.

## Anti-hang rules for agents

1. **Never** run model inference without a `timeout` wrapper
2. **Always** verify binary exists + exec bit before invoking
3. **Always** verify model byte size, not just existence (partial downloads are silent)
4. **Light-swarm mode** (SCOUT only, 80–120 tokens) for casual chat; full swarm for substantive work
5. **Swarm agents get independent timeouts** so a slow SAGE can't hang the SCOUT/SPARK results
6. If self-heal triggers (rebuild/redownload), log to `/tmp/selfheal.log` and continue — never silently hang
7. Always give the user visible progress (a spinner, echo, or phase header) before long operations

## Reference implementation

A 180-line bash library implementing the full recipe lives in
`selfheal_runner.sh` at this workspace; downstream runners (`run_swarm.sh`,
`run_thinking_model.sh`, `run_light_swarm.sh`) source it instead of calling
llama.cpp binaries directly. See benchmark_results.md for full sweep data.

Authored in the field (Arena Agent Mode, 2026-07) during diagnosis of
user-reported "agent stops responding" errors. Root cause was snapshot-size-cap
eviction of 2.4 GB of GGUF models and compiled binaries between turns, with
scripts silently calling missing binaries.
