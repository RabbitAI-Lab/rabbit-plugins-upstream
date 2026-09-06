## Description:

Keep local GGUF/llama.cpp agent sandboxes from hanging after snapshot eviction when inference stalls, binaries or models are missing, npx waits on closed stdin, or sudo might prompt interactively.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and engineers use this skill to preflight and repair local-LLM sandboxes that may lose llama.cpp binaries or GGUF model files after snapshot eviction. It provides guarded shell workflows for timeout-bounded inference, consent-gated repair, prompt caching, model verification, and host-specific tuning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fix mode can install system packages, create a persistent npx shim, download large model files, rebuild local llama.cpp code, and cache prompts or outputs.

Mitigation: Keep the default check mode for read-only inspection and enable SELFHEAL_MODE=fix only with explicit consent, especially when sudo privileges are available.

Risk: Local model and llama.cpp trust boundaries remain important because the skill can use existing binaries, models, and source checkouts.

Mitigation: Review the llama.cpp checkout and binaries before repair, keep rebuilds limited to trusted remotes, and use SELFHEAL_DEEP_VERIFY=1 to recheck existing model hashes.

Risk: Prompt content and generated outputs may be retained in a local cache when fix mode is enabled.

Mitigation: Avoid fix mode for sensitive prompts unless local retention is acceptable, and clear ~/.selfheal/cache when cached outputs should no longer be retained.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/orionshaowswmw/skills/sandbox-selfheal-guard)
- [Qwen3 0.6B GGUF model artifact](https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF/resolve/main/Qwen_Qwen3-0.6B-Q4_K_M.gguf)
- [Qwen2.5 0.5B Instruct GGUF model artifact](https://huggingface.co/second-state/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/Qwen2.5-0.5B-Instruct-Q5_K_M.gguf)
- [Qwen2.5 Coder 0.5B GGUF model artifact](https://huggingface.co/bartowski/Qwen2.5-Coder-0.5B-Instruct-GGUF/resolve/main/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf)
- [DeepSeek R1 Distill Qwen 1.5B GGUF model artifact](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance, Text]

**Output Format:** [Markdown with inline shell commands and operational guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses exit codes and stderr status messages for health and repair outcomes; fix mode may create local logs, state, caches, shims, downloads, and builds after consent.]

## Skill Version(s):

3.0.8 (source: server release metadata, SKILL.md frontmatter, manifest.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
