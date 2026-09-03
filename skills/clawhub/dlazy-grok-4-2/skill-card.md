## Description:

Efficient text generation, dialogue QA, and logical reasoning using the Grok 4.2 text model.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent users can use this skill to call a hosted dLazy CLI integration for text generation, conversational question answering, and reasoning tasks with Grok 4.2.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill is presented as text generation, but the artifact also describes media upload handling and hosted media URLs.

Mitigation: Review the data flow before installation and use it only when prompt, file upload, and hosted output handling match the intended task.

Risk: Prompts and parameters are sent to a third-party hosted dLazy API endpoint for inference.

Mitigation: Avoid sending sensitive or regulated data unless the deployment policy allows use of the dLazy service.

Risk: Authentication can persist a dLazy API key in a local CLI configuration file.

Mitigation: Use organization-scoped keys, rotate or revoke keys when needed, and prefer per-invocation environment variables when persistent local storage is not desired.

Risk: The skill depends on installing or running a third-party npm CLI package.

Mitigation: Review the pinned CLI package and source before installation, and use npx for on-demand execution when a persistent global binary is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/dlazyai/skills/dlazy-grok-4-2)
- [dLazy CLI source](https://github.com/dlazy-ai/cli)
- [dLazy CLI npm package](https://www.npmjs.com/package/@dlazy/cli)
- [dLazy website](https://dlazy.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command output examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires npm or npx, a dLazy API key, and network access to dLazy-hosted API and file endpoints.]

## Skill Version(s):

1.3.10 (source: server release evidence; artifact frontmatter lists 1.3.4)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
