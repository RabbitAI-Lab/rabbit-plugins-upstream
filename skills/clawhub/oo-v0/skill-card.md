## Description:

Enables agents to operate v0 through the OOMOL oo CLI connector for reading, creating, updating, and deleting v0 account data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to manage v0 chats, projects, deployments, environment variables, webhooks, billing, plans, scopes, and user information through a connected OOMOL account.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can change or delete v0 account data through write and destructive actions.

Mitigation: Confirm the exact payload and expected effect before write actions, and require explicit approval before destructive actions.

Risk: The security summary flags broad activation and remote installer instructions as reasons for review before installation.

Mitigation: Use the skill only for intentional v0 account operations, and avoid remote installer commands unless the installer source and integrity have been independently verified.

Risk: Connector action contracts may change over time.

Mitigation: Inspect the live connector schema before running an action so payloads match current v0 contracts.

## Reference(s):

- [v0 homepage](https://v0.dev)
- [oo CLI](https://github.com/oomol-lab/oo-cli)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Configuration instructions, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON connector responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: server release and SKILL.md metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
