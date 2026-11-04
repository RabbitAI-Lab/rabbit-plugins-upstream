## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agent operators use this skill to process A2A inbox wakes, review and reply to tasks, communicate with peer agents, and manage peer access. It provides the runtime workflow for an existing endpoint; setup and deployment are handled by a separate skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Webhook testing advice may expose credentials or private messages to public testing services.

Mitigation: Use a receiver you control or a separate test configuration without production credentials or private messages.

Risk: The downloaded CLI and hosted service have not been audited as part of the bundled files.

Mitigation: Prefer a reviewed, fixed CLI version, validate wake commands, and retain the documented human approval controls.

## Reference(s):

- [A2A Exposed on ClawHub](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox setup](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Messaging another agent](references/messaging.md)
- [Pairing requests](references/pairing.md)
- [Inbound tokens](references/tokens.md)
- [Troubleshooting and command reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [None]

## Skill Version(s):

0.8.30 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
