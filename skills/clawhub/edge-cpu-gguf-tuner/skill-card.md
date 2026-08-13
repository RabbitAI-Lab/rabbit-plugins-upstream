## Description:

Tunes llama.cpp GGUF inference on CPU-only and edge machines with low core counts or limited RAM, focusing on measured settings for threads, flash attention, KV cache type, batch size, quant choice, and mmap behavior.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to benchmark llama.cpp GGUF models on CPU-only VPS, container, SBC, sandbox, or other constrained edge machines and select measured settings that maximize local tokens per second.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Local builds and benchmarks can consume substantial CPU and RAM on constrained machines.

Mitigation: Run benchmarks in a dedicated working directory with selected GGUF model files and monitor resource use during builds and tests.

Risk: Elevated privileges may broaden the impact of local command mistakes.

Mitigation: Use least privilege and avoid elevated privileges unless you independently determine they are necessary for the local setup.

Risk: Benchmark logs and generation output can contain prompts, model paths, or derived results.

Mitigation: Inspect output and log locations, protect generated logs, and remove sensitive prompt material before sharing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/edge-cpu-gguf-tuner)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline bash code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Benchmark recommendations should be validated on the target CPU and model before deployment.]

## Skill Version(s):

1.1.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
