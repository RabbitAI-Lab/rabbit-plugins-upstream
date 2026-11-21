## Description:

Use when woken by an a2a-exposed wake (an A2A endpoint webhook, a pairing request, or a scheduled check), when reading or replying on the A2A endpoint, when told to connect to an A2A agent URL (such as https://name.a2a.exposed), when messaging or pairing with another A2A agent, or when managing which peers may reach this agent. Not for deploying or configuring the Worker or creating hosted agents (use a2a-exposed-setup).

This skill is ready for commercial/non-commercial use.

## Publisher:

[telegraphic-dev](https://clawhub.ai/user/telegraphic-dev)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to handle A2A endpoint wakes, read and reply to tasks, message or pair with peers, and manage peer access. It covers the runtime workflow rather than Worker deployment or hosted agent setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review flags repeated unpinned package commands.

Mitigation: Review each package and command before execution, and use a reviewed, pinned version when practical.

Risk: The security review reports instructions that extend beyond the skill's stated runtime scope.

Mitigation: Keep use focused on runtime inbox, messaging, and pairing tasks; review setup or deployment actions against the companion setup guidance and obtain the required human approval.

Risk: Security scan coverage was partial, with one file only partly inspected.

Mitigation: Review the full skill and reference files before relying on instructions that were not fully covered by the scan.

## Reference(s):

- [A2A Exposed project documentation](https://github.com/telegraphic-dev/a2a-exposed)
- [Hosted inbox guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/getting-started.md#hosted-inbox)
- [Hosted connector checklist](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/mcp.md#hosted-connector)
- [HTTP relay guide](https://github.com/telegraphic-dev/a2a-exposed/blob/main/docs/http-relay.md)
- [Messaging reference](references/messaging.md)
- [Pairing reference](references/pairing.md)
- [Troubleshooting reference](references/troubleshooting.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API calls, Configuration instructions]

**Output Format:** [Markdown guidance with shell commands and API/MCP request instructions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Context dependent; includes task handling, peer messaging, and access-management workflows.]

## Skill Version(s):

0.8.74 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
