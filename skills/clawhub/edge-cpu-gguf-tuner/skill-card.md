## Description:

Offline helper for evidence-first tuning of llama.cpp GGUF inference on CPU-only and constrained edge hosts, using local inspection, benchmark planning, optional user-supplied llama-bench runs, variance-aware ranking, output checks, and unexecuted command rendering.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan, measure, and explain local llama.cpp GGUF CPU tuning on constrained hosts. It helps compare controlled benchmark sweeps and render a candidate runtime command after local evidence and quality checks.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Benchmark execution uses a user-supplied local llama-bench binary and model file, which may carry local execution or parser risk.

Mitigation: Use trusted, current local binaries and models, run as a non-root user, and supply assets explicitly rather than allowing implicit selection.

Risk: Generated reports can contain local paths, host diagnostics, benchmark output, and tuning context.

Mitigation: Store reports in a controlled location and review them before sharing outside the target environment.

Risk: Benchmark throughput is host-, model-, build-, and metric-specific and does not prove end-to-end latency, memory fit, safety, or output quality.

Mitigation: Rerun measurements after any relevant environment change and apply memory and output-quality gates before using a rendered command.

Risk: A benchmark binary that emits excessive output or hangs can disrupt local measurement workflows.

Mitigation: Avoid benchmark binaries that may emit unbounded output and use deliberate timeouts and scoped benchmark runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/edge-cpu-gguf-tuner)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [llama.cpp README](https://github.com/ggml-org/llama.cpp/blob/master/README.md)
- [llama.cpp build documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
- [llama-bench README](https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md)
- [llama.cpp token generation performance tips](https://github.com/ggml-org/llama.cpp/blob/master/docs/development/token_generation_performance_tips.md)
- [Artifact evidence ledger](references.json)
- [Artifact README](README.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown prose with inline shell commands and JSON-shaped summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local benchmark plans, measured recommendations, unexecuted command previews, warnings, and next-step guidance.]

## Skill Version(s):

1.2.5 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
