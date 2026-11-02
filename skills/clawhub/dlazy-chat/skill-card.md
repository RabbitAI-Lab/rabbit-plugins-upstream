## Description:

Supports project-scoped, multi-turn conversations with the dLazy sandbox agent and helps users discover available skills and projects.

This skill is ready for commercial/non-commercial use.

## Publisher:

[dlazyai](https://clawhub.ai/user/dlazyai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill to start or continue conversational, multi-turn work in a dLazy project and discover available skills and projects.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad activation could send ordinary conversation content to dLazy without clear user intent.

Mitigation: Activate only for explicit dLazy requests or an already authorized dLazy project.

Risk: Prompts and selected attachments are sent to dLazy, and work may consume account credits.

Mitigation: Review prompts and files before sending, protect the organization API key, and review the pinned CLI before installation.

## Reference(s):

- [dLazy](https://dlazy.com)
- [dLazy CLI package on npm](https://www.npmjs.com/package/@dlazy/cli)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Conversational text streamed through the CLI]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Project-scoped multi-turn replies.]

## Skill Version(s):

1.2.38 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
