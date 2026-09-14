## Description:

Provides agent access through the dLazy CLI to Claude Sonnet 5 for reasoning, code generation, tool orchestration, and text, image, or video input workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to invoke dLazy's Claude Sonnet 5 wrapper for text generation, coding assistance, reasoning, and multimodal prompt workflows from an agent or shell.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends prompts and parameters to the dLazy hosted API for inference.

Mitigation: Avoid submitting secrets or data that should not be processed by the dLazy service.

Risk: Local image, video, or audio paths passed to the CLI may be uploaded to dLazy media storage.

Mitigation: Pass only media files intended for upload, and review paths before execution.

Risk: The CLI stores or consumes a dLazy API key for authenticated use.

Mitigation: Use a revocable API key, avoid installing or running as root or administrator, and rotate or revoke the key if exposure is suspected.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON envelope containing model outputs, or task status for asynchronous requests]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Supports prompt input plus optional image and video inputs; local media paths passed to the CLI may be uploaded to dLazy-hosted storage.]

## Skill Version(s):

1.2.18 (source: server release metadata; artifact frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
