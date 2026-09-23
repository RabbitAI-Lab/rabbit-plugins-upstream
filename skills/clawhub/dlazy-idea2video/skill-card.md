## Description:

Turns an idea into a video-production workflow that gathers requirements, builds a story, character, scene, and shot plan, expands it into canvas shapes, and can run dLazy CLI generation steps after user confirmation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

External users, creators, and developers use this skill to turn a creative idea into a structured video-generation plan and canvas workflow. It supports requirement gathering, plan review, adjustment, canvas expansion, and confirmed dLazy CLI execution for generated media.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires dLazy account authentication and can store an API key in the local dLazy CLI configuration.

Mitigation: Use the dLazy login flow or an environment variable intentionally, protect the local configuration file, and rotate or revoke the key from the dLazy dashboard when needed.

Risk: Prompts and selected local media paths may be sent to dLazy API and file services for cloud generation.

Mitigation: Avoid sensitive prompts or local media unless upload to dLazy services is intended.

Risk: The workflow includes terminal CLI execution after user confirmation.

Mitigation: Review each command before execution and prefer a pinned npx invocation or reviewed CLI installation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-idea2video)
- [dLazy website](https://dlazy.com)
- [@dlazy/cli npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy CLI repository](https://github.com/dlazy-ai/cli)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with structured plan summaries, inline shell commands, and canvas workflow instructions.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May produce dLazy-hosted media URLs after the user confirms CLI execution.]

## Skill Version(s):

1.3.22 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
