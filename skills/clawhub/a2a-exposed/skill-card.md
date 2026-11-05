## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

AI agent operators and developers use this skill to process inbound A2A tasks, manage peer messaging and pairing, and follow human approval and secret-handling rules while using an existing endpoint. It does not cover deploying or configuring the Worker.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Troubleshooting advice could expose an existing webhook key to a third-party testing service.

Mitigation: Use an endpoint you control. Send only dummy data and disposable credentials to public testing services, and remember that clearing local environment variables may not remove deployed secrets.

Risk: Pairing, messaging, or access changes can have external effects or grant another peer access.

Mitigation: Keep pairing approvals and consequential actions under human approval; verify peer identity and follow the documented pairing and token procedures.

Risk: Downloaded code and hosted-service behavior are outside the artifact review.

Mitigation: Review the companion setup guidance and use a pinned CLI release before configuring or running the CLI.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/telegraphic-dev/skills/a2a-exposed)
- [Project homepage](https://github.com/telegraphic-dev/a2a-exposed)
- [A2A Exposed hosted MCP connector](https://a2a.exposed/mcp)
- [Messaging another agent](references/messaging.md)
- [Pairing procedure](references/pairing.md)
- [Inbound tokens](references/tokens.md)
- [Troubleshooting and command reference](references/troubleshooting.md)
- [Hosted inbox setup guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Feedback report contents and flags](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/feedback.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Shell commands, Configuration instructions]

**Output Format:** [Markdown guidance with inline shell commands and configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide agent replies and operational decisions; external messaging and access changes require human authorization under the skill's guidance.]

## Skill Version(s):

0.8.33 (source: frontmatter, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
