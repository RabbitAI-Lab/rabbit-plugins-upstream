## Description:

Tunes llama.cpp GGUF inference for CPU-only and edge systems by guiding benchmark sweeps for threads, flash attention, KV-cache format, batch size, and quant selection.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to tune llama.cpp GGUF models on CPU-only VPS, container, SBC, sandbox, or other low-resource edge systems.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Benchmarking and local inference commands can consume CPU, memory, and time on constrained systems.

Mitigation: Review commands before running them, start with short benchmark repetitions, and monitor system resources during sweeps.

Risk: Optional model or llama.cpp downloads may introduce unverified third-party artifacts.

Mitigation: Verify downloaded models and llama.cpp sources separately before using them.

## Reference(s):

- [README.md](README.md)
- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/edge-cpu-gguf-tuner)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces local benchmarking and tuning recommendations; it does not execute commands on its own.]

## Skill Version(s):

1.1.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
