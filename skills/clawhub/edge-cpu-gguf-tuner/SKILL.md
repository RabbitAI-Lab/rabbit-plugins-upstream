---
name: edge-cpu-gguf-tuner
description: Evidence-first, offline tuning of llama.cpp GGUF inference on CPU and constrained edge hosts. Inspects CPU topology, renders compatible benchmark plans, optionally runs an explicitly supplied local llama-bench, ranks pp/tg/pg results with variance-aware confidence, verifies output gates, and renders (never executes) a measured command. It does not install llama.cpp, download models, call APIs, or claim universal defaults.
metadata: {"openclaw":{"emoji":"⚙️","version":"1.2.2","offline":true,"entrypoint":"bin/edge-cpu-tuner"}}
---

# edge-cpu-gguf-tuner

Use this skill when a user wants to improve llama.cpp GGUF inference on a CPU-only or constrained machine, especially when thread count, batch size, flash attention, KV-cache type, context depth, model compatibility, or token-generation throughput is in question.

This is an **evidence-first local measurement workflow**, not a collection of universal tuning folklore. The old registry artifact contained results from one 2-vCPU/2-GB environment; those numbers are not defaults here. A recommendation is valid only for the exact host, model, llama.cpp binary/build, benchmark metric, and conditions recorded in its report.

## Non-negotiable operating contract

1. **Offline and no-install:** never install llama.cpp, download a model, call a cloud provider, or modify a source checkout. The tool uses Python's standard library only.
2. **Explicit assets:** inspect and plan without assets. Run a benchmark only after the user supplies a local `llama-bench` executable and a local `.gguf` path. Do not search for or select a model implicitly.
3. **No shell execution:** use the entrypoint or `python3 scripts/edge_cpu_tuner.py`; the runner invokes an argument vector with `shell=False`, a reduced environment, stdin closed, and a timeout. Never paste model paths into a shell command unquoted.
4. **No invented results:** a plan is not a measurement. If the run fails, returns no structured records, or has no clear winner, report that state and do not fill in a number.
5. **Least privilege:** run the user-owned binary as a non-privileged user. A GGUF file and its parser are user-selected binary inputs; path validation is not a sandbox. Keep llama.cpp current and protect reports, which can contain paths and diagnostics.
6. **Compatibility before speed:** check the exact binary's `-h` output before using a rendered command. Current upstream documentation uses `llama cli`; other builds expose `llama-cli` or legacy `llama-completion`. Never assert that one name works everywhere.

## Fast workflow

From the installed skill directory:

```bash
# 1. Read-only host and binary discovery
sh bin/edge-cpu-tuner inspect --json

# 2. Offline plan; no executable or model is opened
sh bin/edge-cpu-tuner plan --sweep all \
  --model /path/to/model.gguf --binary /path/to/llama-bench --json

# 3. Explicit local measurement; choose one metric and keep reports
sh bin/edge-cpu-tuner bench \
  --model /path/to/model.gguf \
  --binary /path/to/llama-bench \
  --sweep threads --repetitions 3 --metric tg \
  --out reports/threads.json --json

# 4. Re-rank an existing report without rerunning inference
sh bin/edge-cpu-tuner recommend --report reports/threads.json --metric tg --json

# 5. Render a candidate command; this never launches inference
sh bin/edge-cpu-tuner deploy --report reports/threads.json \
  --cli /path/to/llama-cli --prompt 'short user prompt' --tokens 128 --json
```

Run separate `bench` invocations for `threads`, `batch`, `flash`, `kv`, and `context` when attributing causality. `all` is convenient but still emits separate configurations; it is not permission to compare unrelated changes. Use `--keep-going` only when partial failures are useful. `--allowed-root` can require the model to be below a chosen directory.

The runner's current benchmark argv uses documented llama-bench options: `-m`, `-p`, `-n`, `-t`, `-b`, `-ub`, `-fa`, `-ctk`, `-ctv`, `-d`, `-r`, and `-o json`. If the exact binary rejects an option, stop and inspect its help or use a compatible binary; do not silently fall back to a guessed flag.

## How to reason about results

- Select `tg` for decode/token-generation throughput, `pp` for prompt processing, or `pg` for prompt-plus-generation. Do not call one metric “overall speed.”
- Upstream `llama-bench` reports average and standard-deviation tokens/sec, and its timings exclude tokenization and sampling. Explain this whenever a user asks about end-to-end latency.
- The default thread plan starts at one, doubles toward detected physical cores, and compares logical cores when they differ. This follows upstream troubleshooting guidance but is not a winning default.
- Keep warm-up, thermal state, CPU governor/frequency, background load, model context depth, and repetition count visible in the report. On a small box, sustained thermal throttling can reverse a short burst result.
- Prefer a measured configuration only when its margin and variance justify it. The tool labels a result `winner`, `provisional_winner`, `no_clear_winner`, or `single_observation`; low confidence means “keep the baseline or rerun,” not “guess.”
- Quantization, KV-cache type, flash attention, batch size, context depth, and architecture interact. Never port a result from one model, quantization, OS, compiler, or llama.cpp commit to another without a new run.
- A benchmark winner may use more memory or have worse latency/quality. Check memory headroom and run a user-approved end-to-end/quality comparison before deployment.

## Quality and deployment gate

`deploy` emits a command object with `executed: false`, the selected argv, a shell-rendered preview, and warnings. It does not alter files or launch the model. Confirm the exact CLI's help first, then run it yourself if desired.

For a deterministic output check, capture the baseline and candidate outputs using the exact same prompt, model, seed/temperature settings supported by that CLI, and token limit. Compare them locally:

```bash
sh bin/edge-cpu-tuner verify-output \
  --baseline /tmp/baseline.txt --candidate /tmp/candidate.txt \
  --mode bytes --json
```

`identical: false` means reject the candidate for an identity-gated change; it does not prove which output is semantically better. A byte-identical output is not a proof of correctness, safety, or quality. If the CLI is nondeterministic, document that and use a human/automated quality test rather than pretending identity is meaningful.

## Machine-readable contract

Every JSON response has a versioned `schema`. Important schemas are:

- `edge-cpu-gguf-tuner.host.v1` — host topology and discovered binaries.
- `edge-cpu-gguf-tuner.plan.v1` — offline configurations and argv arrays.
- `edge-cpu-gguf-tuner.report.v1` — exact host/model/binary metadata, attempts, parsed records, warnings, ranked metrics, and recommendation.
- `edge-cpu-gguf-tuner.command.v1` — an unexecuted deployment argv and compatibility warnings.
- `edge-cpu-gguf-tuner.quality-gate.v1` — hashes, sizes, identity decision, and explicit rejection/pass state.
- `edge-cpu-gguf-tuner.error.v1` — safe error text and exit code.

Agents should preserve these fields when summarizing:

```text
status: plan | measured | failed | no_clear_winner
host: physical/logical CPUs, memory, architecture
model_and_build: exact path/size, binary path/version, optional model hash
metric: pp | tg | pg
recommendation: configuration, tokens_per_second, standard deviation, confidence
provenance: report path plus source/evidence scope
warnings: compatibility, thermal/noise, memory, quality, or failed attempts
next_action: one explicit rerun/verification step, or “none”
```

Be concise by default. Do not repeat the entire report when a compact JSON object or table answers the question; expand only when the user asks for methodology or troubleshooting.

## Compatibility and build evidence

The evidence ledger in `references.json` records retrieval date, source URLs, SHA-256 digests, claim scope, and whether a statement is upstream documentation or a local test. Current upstream references establish that:

- the README quick start uses unified `llama cli`, while upstream build examples also show `llama-cli`;
- `llama-bench` supports pp/tg/pg, repetitions, JSON/JSONL output, context depth, separate batch/ubatch, and `-fa on|off|auto`;
- benchmark timings exclude tokenization and sampling;
- excessive thread counts can oversaturate a CPU, so measuring from one thread upward is safer than blindly using every logical CPU;
- a baseline CPU build is `cmake -B build` followed by `cmake --build build --config Release`.

Those sources do **not** authorize this skill to build/install anything, and they do not prove a performance result on the user's hardware. The historical registry copy is retained only in the private workspace's `base/` directory, not as an authority for this skill.

## Self-improvement without self-modification

The safe feedback loop is evidence accumulation, not autonomous code editing:

1. save reports with the exact host/model/build metadata;
2. repeat after a controlled change or environment change;
3. use `recommend` to re-rank records and compare the new report to the old one;
4. update the user's chosen runtime command only after the quality/memory gate;
5. rerun after a llama.cpp update, model/quantization change, hardware migration, or thermal/power change.

The skill never rewrites its own source, fetches “better” models, or learns from unverified model-generated suggestions. The deterministic regression suite is `sh selftest.sh`; its fake benchmark is only a parser/control-flow test and must never be reported as real throughput.

## Failure and exit semantics

- `0`: successful inspection/plan/render/quality pass, or a benchmark with structured records (even if warnings are present).
- `1`: benchmark produced no records or partial results; inspect `warnings` and rerun deliberately.
- `2`: invalid user input or missing explicit asset.
- `124`: subprocess timeout; stop and inspect model/binary/runtime conditions.
- `127`: executable could not be launched.
- `130`: user interruption.

## References

- `references.json` — machine-readable evidence ledger and source hashes.
- `README.md` — full operational guide, threat model, schemas, and test checklist.
- `scripts/edge_cpu_tuner.py` — stdlib-only implementation.
- `scripts/selftest.py` / `selftest.sh` — deterministic static/behavioral smoke tests.
