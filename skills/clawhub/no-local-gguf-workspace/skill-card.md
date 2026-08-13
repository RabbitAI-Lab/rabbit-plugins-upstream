## Description:

Operate the carminic-acid Arena workspace at full capability without cloning llama.cpp, building llama binaries, or downloading offline Qwen/DeepSeek GGUF models.

This skill is ready for commercial/non-commercial use.

## Publisher:

[orionshaowswmw](https://clawhub.ai/user/orionshaowswmw)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and operators use this skill to rebuild and operate a constrained Arena workspace while deliberately skipping local GGUF model downloads and llama.cpp builds. It documents the flags, checks, and routing path needed to use stored provider credentials for final answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts may leave the local machine when router or orchestration commands call configured external model providers.

Mitigation: Review the local router and credential files before use, and avoid sending sensitive prompts unless the configured providers are approved.

Risk: Missing skip flags can cause local model downloads and llama.cpp builds that the skill is meant to avoid.

Mitigation: Export SKIP_LOCAL_MODELS=1 and ENSURE_SKIP_LLAMA_BUILD=1 before running the workspace rebuild, then verify llama.cpp and GGUF files are absent.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/orionshaowswmw/skills/no-local-gguf-workspace)
- [Publisher profile](https://clawhub.ai/user/orionshaowswmw)

## Skill Output:

**Output Type(s):** [guidance, shell commands, configuration]

**Output Format:** [Markdown with inline bash commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance assumes existing workspace scripts and stored provider credentials.]

## Skill Version(s):

1.0.0 (source: frontmatter and release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
