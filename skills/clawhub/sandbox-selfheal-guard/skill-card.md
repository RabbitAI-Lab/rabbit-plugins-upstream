## Description:

Sandbox Selfheal Guard helps agents check and repair local llama.cpp/GGUF sandboxes that can hang after binaries or model files disappear.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to run bounded preflight checks, guarded local inference, model verification, cache inspection, and consent-gated repairs for local llama.cpp/GGUF sandboxes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Fix mode can make system-level and persistent local changes, including package installation, code rebuilds, model downloads, cache or state writes, and npx shim creation.

Mitigation: Keep SELFHEAL_MODE in check mode by default and enable SELFHEAL_MODE=fix only after explicit human review of the proposed repair.

Risk: Rebuilding code from an untrusted llama.cpp checkout can introduce supply-chain risk.

Mitigation: Use only trusted llama.cpp remotes for rebuilds and avoid override settings unless the checkout has been separately reviewed.

Risk: Mutable installer commands and remote model downloads can change what is installed over time.

Mitigation: Prefer pinned installer commands and rely on manifest-listed model URLs with byte, GGUF magic, and sha256 verification.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/orionshaowswmw/skills/sandbox-selfheal-guard)
- [Artifact README](artifact/README.md)
- [Artifact changelog](artifact/CHANGELOG.md)
- [Model and repair manifest](artifact/manifest.json)
- [Qwen3 0.6B GGUF model artifact](https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF/resolve/main/Qwen_Qwen3-0.6B-Q4_K_M.gguf)
- [Qwen2.5 0.5B Instruct GGUF model artifact](https://huggingface.co/second-state/Qwen2.5-0.5B-Instruct-GGUF/resolve/main/Qwen2.5-0.5B-Instruct-Q5_K_M.gguf)
- [Qwen2.5 Coder 0.5B GGUF model artifact](https://huggingface.co/bartowski/Qwen2.5-Coder-0.5B-Instruct-GGUF/resolve/main/Qwen2.5-Coder-0.5B-Instruct-Q4_K_M.gguf)
- [DeepSeek-R1 Distill Qwen 1.5B GGUF model artifact](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF/resolve/main/DeepSeek-R1-Distill-Qwen-1.5B-Q4_K_M.gguf)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and local script outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce local diagnostics, bounded inference output, cache statistics, and repair guidance depending on SELFHEAL_MODE.]

## Skill Version(s):

3.0.13 (source: server release evidence; artifact frontmatter and manifest report 3.0.8)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
