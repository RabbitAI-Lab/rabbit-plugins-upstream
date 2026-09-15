## Description:

Chatwork (go.chatwork.com). Use this skill for Chatwork requests including reading, creating, updating, and deleting data through the OOMOL Chatwork connector.

This skill is ready for commercial/non-commercial use.

## Publisher:

[oomol](https://clawhub.ai/user/oomol)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to let an agent operate Chatwork through an OOMOL-connected account, including room, member, message, contact, profile, and task workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: First-time setup can lead an agent to execute unverified remote installer scripts.

Mitigation: Review before installing, avoid automatic installer-pipe execution, and prefer a verified or package-manager installation of oo.

Risk: Free-form Chatwork message data can make command payload construction unsafe if not handled carefully.

Mitigation: Inspect the live action schema before constructing payloads and pass structured JSON through a file or safely quoted argument.

Risk: Chatwork write or delete actions can change or remove workspace data.

Mitigation: Require explicit user confirmation for every write or destructive Chatwork action, including the exact target and payload.

## Reference(s):

- [Chatwork skill page](https://clawhub.ai/oomol/skills/oo-chatwork)
- [Chatwork homepage](https://go.chatwork.com)
- [OOMOL oo CLI](https://github.com/oomol-lab/oo-cli)
- [oo CLI install guide](https://cli.oomol.com/install-guide.md)
- [Chatwork icon](https://static.oomol.com/logo/third-party/Chatwork.svg)

## Skill Output:

**Output Type(s):** [Shell commands, Configuration, Guidance]

**Output Format:** [Markdown with inline shell commands and JSON payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses live connector schema inspection before constructing action payloads.]

## Skill Version(s):

1.0.3 (source: release evidence and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
