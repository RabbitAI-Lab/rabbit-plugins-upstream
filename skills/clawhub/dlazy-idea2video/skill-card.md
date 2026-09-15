## Description:

Turn a user's idea into a video-production workflow that plans story, characters, scenes, shots, keyframes, generated shot videos, and final concatenation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to turn a creative idea into a staged video-generation plan, review or adjust the plan, and expand it into canvas shapes for execution with dLazy models.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks agents to install and run a third-party CLI while handling prompts, selected media files, generated outputs, and an API key.

Mitigation: Install only if the dLazy CLI is trusted; prefer npx or an isolated local install, review the CLI source or package first, avoid administrator privileges, and rotate the API key if exposure is suspected.

Risk: Persistent credentials may be written to the local dLazy CLI configuration.

Mitigation: Use per-session DLAZY_API_KEY when appropriate, restrict local file permissions, and revoke or rotate organization API keys from the dLazy dashboard when needed.

Risk: The source contains conflicting workflow instructions that could affect how an agent sequences generation steps.

Mitigation: Require explicit user confirmation at planning gates and review generated plans before executing CLI commands or writing canvas shapes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy homepage](https://dlazy.com)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration]

**Output Format:** [Markdown with structured planning steps, model selections, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce canvas shape instructions and dLazy-hosted media URLs after authenticated CLI execution.]

## Skill Version(s):

1.3.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
