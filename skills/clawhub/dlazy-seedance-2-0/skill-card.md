## Description:

Provides an agent-facing wrapper for dLazy's hosted Seedance 2.0 video generation CLI, supporting text prompts, image, video, and audio references, plus first- and last-frame generation modes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to generate videos through dLazy's hosted Seedance 2.0 CLI from prompts and optional image, video, audio, first-frame, or last-frame inputs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and referenced media files are sent to dLazy-hosted services for generation.

Mitigation: Use the skill only with prompts and image, video, or audio files that are appropriate to upload to dLazy.

Risk: Authentication can store a dLazy API key in the local CLI configuration.

Mitigation: Confirm trust in dLazy before login, rotate or revoke keys when needed, or provide the key per invocation with DLAZY_API_KEY.

Risk: The skill depends on a pinned third-party npm CLI.

Mitigation: Review the pinned dLazy CLI package before installing or use npx for on-demand execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-seedance-2-0)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [shell commands, configuration, text, markdown, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON response examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can return hosted media URLs, async task identifiers, or downloaded media files when the save option is used.]

## Skill Version(s):

1.3.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
