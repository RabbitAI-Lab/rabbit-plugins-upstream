## Description:

Provides access to the dLazy hosted Claude Sonnet 5 CLI for text generation, reasoning, coding, and complex tool orchestration with optional image and video inputs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to invoke dLazy's hosted Claude Sonnet 5 CLI for text generation, coding, reasoning, and multimodal prompt workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Prompts and local image, video, or audio files passed to the CLI may be uploaded to the dLazy hosted service.

Mitigation: Use only data approved for third-party hosted processing and review inputs before invoking the skill.

Risk: Generated assets may be hosted by dLazy.

Mitigation: Avoid submitting sensitive content unless hosted outputs are acceptable under the user's data-handling requirements.

Risk: Using dLazy login or saved authentication stores an API key locally.

Mitigation: Protect the local user account, rotate or revoke keys from the dLazy dashboard when needed, or provide DLAZY_API_KEY per invocation instead of saving credentials.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-claude-sonnet-5)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [JSON responses and agent-facing text, often with shell commands or generated content from the hosted model]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May return generated output URLs; async invocations can return a task identifier for polling.]

## Skill Version(s):

1.2.22 (source: server release evidence; artifact frontmatter lists 1.2.7)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
