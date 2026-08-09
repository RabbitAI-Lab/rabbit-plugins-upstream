## Description:

Anti-stuck and anti-snapshot-wipe guard for agentic sandboxes with a self-healing runner, byte-verified GGUF manifest, native CPU rebuilds, hard timeouts, binary fallbacks, prompt-cache integration, and light-swarm mode.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to add bounded self-healing checks around local sandbox inference workflows so missing binaries, missing model files, and long-running calls fail or recover predictably.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence flags the release as suspicious because it can make root-level package changes, alter the user's home PATH, and download large model files.

Mitigation: Install only in a disposable or tightly scoped sandbox, review the script first, and require explicit approval for sudo, PATH changes, and home-directory writes.

Risk: The self-heal runner can download large GGUF model files and relies on byte-size checks rather than stronger model integrity verification.

Mitigation: Preinstall dependencies and models manually where possible, pin trusted sources, and verify model integrity with stronger hashes before use.

Risk: Repair commands and logs can modify or expose local environment details, dependencies, credentials, or workspace state.

Mitigation: Use least privilege, keep backups, protect logs, avoid production hosts, and inspect outputs and exit codes after every repair run.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/sandbox-selfheal-guard)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)
- [Qwen2.5 0.5B Instruct GGUF](https://huggingface.co/second-state/Qwen2.5-0.5B-Instruct-GGUF)
- [Qwen3 0.6B GGUF](https://huggingface.co/bartowski/Qwen_Qwen3-0.6B-GGUF)
- [DeepSeek R1 Distill Qwen 1.5B GGUF](https://huggingface.co/bartowski/DeepSeek-R1-Distill-Qwen-1.5B-GGUF)
- [Qwen2.5 Coder 0.5B Instruct GGUF](https://huggingface.co/bartowski/Qwen2.5-Coder-0.5B-Instruct-GGUF)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May trigger local repair steps, model downloads, timeout-wrapped inference calls, and self-heal logging when used by an agent.]

## Skill Version(s):

2.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
