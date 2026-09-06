## Description:

Evidence-first, offline tuning of llama.cpp GGUF inference on CPU and constrained edge hosts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to plan and evaluate local llama.cpp GGUF CPU inference settings on constrained hosts. It helps inspect host topology, create compatible benchmark plans, parse explicit local llama-bench results, rank pp/tg/pg metrics, verify output gates, and render a measured command without executing inference.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A user-supplied llama.cpp benchmark binary and local GGUF model are native/local assets that the wrapper cannot sandbox.

Mitigation: Use only a trusted, maintained llama.cpp benchmark binary and a controlled local GGUF file, run as a non-root user, and verify the exact binary before benchmarking.

Risk: Generated reports can contain local paths and diagnostics.

Mitigation: Treat reports as sensitive and avoid putting secrets in prompts, paths, environment variables, or report names.

Risk: Very large subprocess output can stress memory-constrained hosts because one output cap is not fully incremental.

Mitigation: Keep benchmark output caps and timeouts bounded, prefer small controlled sweeps, and monitor constrained hosts during runs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/edge-cpu-gguf-tuner)
- [llama.cpp README](https://github.com/ggml-org/llama.cpp/blob/master/README.md)
- [llama.cpp build documentation](https://github.com/ggml-org/llama.cpp/blob/master/docs/build.md)
- [llama-bench README](https://github.com/ggml-org/llama.cpp/blob/master/tools/llama-bench/README.md)
- [llama.cpp token generation performance tips](https://github.com/ggml-org/llama.cpp/blob/master/docs/development/token_generation_performance_tips.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance and JSON-oriented summaries with shell command arrays or previews]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports and recommendations are host-, model-, binary-, build-, metric-, and condition-specific; deployment commands are rendered for review and are not executed by the skill.]

## Skill Version(s):

1.2.2 (source: server release metadata, SKILL.md frontmatter, and _meta.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
