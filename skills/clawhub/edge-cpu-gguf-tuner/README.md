# ⚙️ edge-cpu-gguf-tuner

**Evidence-first CPU tuning for llama.cpp GGUF inference on constrained machines.**

This release turns the former documentation-only artifact into a small,
stdlib-only, offline helper. It can inspect a host, generate a reproducible
benchmark plan, run a user-authorized local `llama-bench`, parse structured
results, rank prompt/decode/combined throughput with variance-aware confidence,
compare output files, and render a measured runtime command without executing
it.

It deliberately does **not** install llama.cpp, download models, call a cloud
API, modify a source tree, edit its own files, or make a universal claim such
as “physical cores always win.”

## What is included

| Path | Role |
|---|---|
| `SKILL.md` | Compact agent-facing operating contract and workflow. |
| `bin/edge-cpu-tuner` | Portable shell entrypoint; invoke as `sh bin/edge-cpu-tuner` because some installers do not preserve executable bits. |
| `scripts/edge_cpu_tuner.py` | Python 3 standard-library implementation. |
| `scripts/selftest.py` and `selftest.sh` | Deterministic regression tests, including a fake benchmark. |
| `references.json` | Dated evidence ledger, source URLs, retrieved source hashes, claim scope, and unverified-by-design list. |
| `_meta.json` | Package metadata, version `1.2.0`. |
| `.clawhubignore` | Excludes local/generated review material from publishing. |

The private workspace may contain `base/`, `research/`, and `review/` copies used
for audit; those are not functional inputs to the published skill and are
ignored from the package.

## Quick start

The installed directory is the working directory for all commands:

```bash
sh bin/edge-cpu-tuner inspect --json
sh bin/edge-cpu-tuner plan --sweep threads --json
```

`inspect` is read-only. `plan` is also offline and does not open a model or
launch a binary. It reports detected logical/physical CPU counts, memory when
available, platform, and candidate binaries.

To run an explicit local benchmark:

```bash
sh bin/edge-cpu-tuner bench \
  --model /absolute/path/to/model.gguf \
  --binary /absolute/path/to/llama-bench \
  --sweep threads \
  --repetitions 3 \
  --metric tg \
  --out reports/threads.json \
  --json
```

The runner requires an explicit `--binary` for execution; `inspect` may discover
PATH candidates, but `bench` never silently chooses one. It invokes the selected
binary with an argument vector, not a shell. It requests structured JSON output
and records the exact attempts, parsed records, host metadata, selected model
metadata, warnings, and recommendation. The model is opened by `llama-bench`,
not by the wrapper. Use a current, non-privileged llama.cpp binary and keep it
updated. Add `--verify-gguf-magic` for a cheap read-only header check before the
external parser; it is not a substitute for parser safety.

Available controlled sweeps:

```text
baseline  one detected baseline configuration
threads   1, powers of two toward physical cores, and logical cores if different
batch     512, 1024, 2048 (override with --batches)
flash     off, auto, on (override with --flash)
kv        f16/f16, q8_0/f16, f16/q8_0, q8_0/q8_0
context   depth 0, 512, 2048 (override with --depths)
all       the above, capped by --max-configs
```

Use a separate sweep when you need clean causal attribution. `all` is a
convenience list of one-variable configurations, not evidence that every
variable can be changed together.

Re-rank an existing report without rerunning inference:

```bash
sh bin/edge-cpu-tuner recommend \
  --report reports/threads.json --metric tg --json
```

Render a candidate command from the measured winner. This command is displayed
only; it is never launched by the tuner:

```bash
sh bin/edge-cpu-tuner deploy \
  --report reports/threads.json \
  --cli /absolute/path/to/llama-cli \
  --model /absolute/path/to/model.gguf \
  --prompt 'short test prompt' --tokens 128 --json
```

The renderer understands three common executable shapes:

- `llama` → emits `llama cli ...` for the current unified command layout;
- `llama-cli` → emits direct `llama-cli ...` arguments;
- `llama-completion` → emits a legacy direct command only when that exact
  executable was selected.

This is a compatibility renderer, not a promise that every build supports all
flags. Run `selected-cli -h` first and resolve any version-specific option
mismatch rather than guessing.

## Quality gate

When a tuning change is expected to preserve deterministic output, capture the
same model/prompt/seed/temperature/token-limit output using the exact CLI and
compare the files locally:

```bash
sh bin/edge-cpu-tuner verify-output \
  --baseline /tmp/baseline.txt \
  --candidate /tmp/candidate.txt \
  --mode bytes --json
```

The response contains both SHA-256 hashes, byte counts, `identical`, and a
`pass` or `reject_candidate` decision. Byte identity is only a reproducibility
gate. It is not a semantic-quality proof. If the runtime is nondeterministic,
document that and use a human or automated quality evaluation instead of
pretending an identity check is meaningful.

## Current upstream evidence, carefully scoped

The ledger in [`references.json`](references.json) records the exact retrieved
source hashes and dates. The main supported facts are:

| Fact | Scope | How the tool uses it |
|---|---|---|
| Upstream quick start documents unified `llama cli`. | Current upstream README at retrieval date; installed builds vary. | `deploy` emits the `cli` subcommand only for an executable named `llama`. |
| `llama-bench` supports pp/tg/pg, repetitions, JSON/JSONL output, context depth, separate `-b`/`-ub`, and `-fa on|off|auto`. | Current upstream benchmark documentation; exact binary still wins. | `bench` requests `-o json` and keeps the metric type visible. |
| `llama-bench` timings exclude tokenization and sampling. | Upstream benchmark documentation. | Reports and agent summaries must not call benchmark t/s end-to-end latency. |
| Excessive thread counts can oversaturate a CPU; upstream recommends starting at one and scaling toward a bottleneck. | Upstream troubleshooting note, not a default result. | The default plan compares a small topology-aware candidate set. |
| CPU build baseline is CMake configure followed by a Release build. | Upstream build guide. | Documentation only; this skill never builds or installs. |

The ledger explicitly lists claims that are **not** made: no universal best
thread count, quantization, KV-cache type, flash-attention state, batch size,
context size, or model architecture; no promise that a benchmark winner has
best latency, quality, or memory use; and no assumption that a selected binary
is safe to run with privileges.

## Methodology

1. **Inspect:** record topology, available memory fields, platform, and binary
   candidates. A container can hide physical topology; the source field remains
   visible.
2. **Baseline:** use the exact model and exact benchmark binary that matter.
   Capture the selected metric (`pp`, `tg`, or `pg`) and repetitions.
3. **Change one variable:** thread, batch, flash attention, KV types, or context
   depth. Keep prompt/generation sizes and other flags constant.
4. **Repeat and observe variance:** a three-repetition sweep is a starting point,
   not a confidence interval. Increase repetitions on noisy VMs or thermally
   limited SBCs. Watch sustained frequency/temperature and background load.
5. **Rank conservatively:** the tool stores average and standard deviation,
   calculates a coefficient of variation, and lowers confidence when the margin
   is small, the result is noisy, or there is only one configuration.
6. **Validate separately:** check memory headroom, end-to-end latency, and
   output/quality. A `tg` winner is not automatically a `pp` or `pg` winner.
7. **Render, review, deploy manually:** `deploy` produces argv and a quoted
   preview, but never runs inference.

A saved report is a local evidence record. Re-run after changing the model,
quantization, context, build commit/compiler, OS, CPU power state, thermal
conditions, or background workload.

## JSON contracts

Responses are versioned so an agent can consume them without scraping prose:

- `edge-cpu-gguf-tuner.host.v1`
- `edge-cpu-gguf-tuner.plan.v1`
- `edge-cpu-gguf-tuner.report.v1`
- `edge-cpu-gguf-tuner.command.v1`
- `edge-cpu-gguf-tuner.quality-gate.v1`
- `edge-cpu-gguf-tuner.error.v1`

A measured report includes:

```json
{
  "schema": "edge-cpu-gguf-tuner.report.v1",
  "host": {"physical_cpus": 2, "logical_cpus": 4},
  "model": {"path": "/models/example.gguf", "size_bytes": 123},
  "binary": {"path": "/opt/llama-bench", "version": "..."},
  "benchmark": {"sweep": "threads", "repetitions": 3},
  "records": [{"test_type": "tg", "avg_tokens_per_second": 12.3}],
  "invalid_records": 0,
  "recommendation": {
    "metric": "tg",
    "status": "winner",
    "confidence": "high",
    "configuration": {"threads": 2}
  },
  "warnings": []
}
```

The example is schema shape only, not a real benchmark result. The tool never
creates a fake result when a run fails. Exit codes are documented in `SKILL.md`.

## Security and privacy boundary

Implemented controls:

- no network libraries or API credentials;
- no package/model/source downloads;
- no `shell=True`, shell interpolation, `os.system`, or `eval`;
- explicit regular-file checks for user-selected assets;
- model extension check by default, with an explicit opt-out for compatibility
  tests (`--allow-non-gguf`);
- optional `--allowed-root` containment check for model paths;
- argv execution with stdin closed, timeout, and a reduced environment;
- dynamic-loader injection and Python startup variables are not inherited;
- stdout/stderr from each benchmark is capped (`--max-output-bytes`, 8 MiB by default),
  stderr is truncated, and credential-shaped strings are redacted in the report;
- report serialization is capped (`--max-report-bytes`, 10 MiB by default) and
  written atomically; report writes occur only when the user supplies `--out`.

The wrapper cannot sandbox an external native executable or guarantee that a
malformed GGUF/parser is safe. Run as a non-root user, use a maintained
llama.cpp build, keep model files in a controlled directory, and treat reports
as sensitive because paths and diagnostics may be recorded. Do not pass
secrets in prompts, paths, environment variables, or report names.

## Build/install boundary

No build is performed by this skill. If a user separately maintains a llama.cpp
checkout, current upstream documentation describes this CPU baseline:

```bash
cmake -B build
cmake --build build --config Release
```

That reference is not an instruction for this agent to install anything. Build
flags, compiler choices, target paths, and executable names vary by OS,
architecture, and llama.cpp version. Inspect the resulting exact binaries
before using them.

## Verification and debugging gate

Run the complete local test suite after changes:

```bash
sh selftest.sh
python3 -m py_compile scripts/edge_cpu_tuner.py scripts/selftest.py
```

The regression suite tests host planning, topology candidates, JSON and CSV
parsing, conservative ranking, shell-argument safety, a fake benchmark
integration, report persistence, re-ranking, and the output quality gate. The
fake benchmark is synthetic control-flow data and must never be quoted as
throughput.

Recommended manual gates when a real user asset is available:

- **static:** compile and inspect dependencies; confirm no network/download or
  credential code;
- **behavioral:** `inspect`, `plan`, invalid paths, non-GGUF rejection, and
  structured error JSON;
- **functional:** one explicit local `llama-bench` run with a bounded timeout;
- **compatibility:** exact binary `-h`, `llama-cli`, unified `llama cli`, and
  legacy binary variants as available;
- **performance:** repeated pp/tg/pg runs under documented thermal/background
  conditions, with failed/empty records retained;
- **security:** non-privileged execution, path containment where needed,
  report review, and no secrets in environment or output.

## Release notes

### 1.2.2

- Updated all usage examples to invoke shell entrypoints through `sh`, because
  cold ClawHub installs may not preserve executable permission bits.
- Verified a cold-installed copy with the bundled self-test and host inspection.

### 1.2.1

- Removed all private provider-review helpers from the publish tree; review tooling
  remains outside the skill and the package now contains only the offline tuner,
  tests, evidence ledger, documentation, license, metadata, and skill card.
- Kept the same functional surface and security boundary as 1.2.0.

### 1.2.0

- Replaced incomplete documentation-only workflow with a portable, stdlib-only
  offline CLI and deterministic tests.
- Added host topology inspection, one-variable benchmark planning, structured
  llama-bench parsing, variance-aware ranking, report persistence, and explicit
  confidence states.
- Added safe output comparison and non-executing deployment rendering for
  unified/direct/legacy CLI layouts.
- Replaced universal historical tuning claims with a dated evidence ledger and
  host/model/build-qualified recommendations.
- Added security controls, machine-readable schemas, failure semantics, and
  no-download/no-network boundaries.
