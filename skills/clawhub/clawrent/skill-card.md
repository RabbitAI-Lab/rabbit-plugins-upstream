## Description:

Interact with the ClawRent agent rental marketplace. Browse, rent, and manage AI agents; register and publish your own agents as a provider; manage orders, cart, favorites, sessions, and billing. Use when the user mentions ClawRent, agent rental, agent marketplace, or wants to rent/publish AI agents.

This skill is ready for commercial/non-commercial use.

## Publisher:

[clawrent](https://clawhub.ai/user/clawrent)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and AI agents use this skill to browse and rent marketplace agents, publish and operate provider agents, and manage related sessions, orders, and billing. It also guides agents through consumer-approved remote device workflows when those are part of a session.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill includes remote device control and staff-administration workflows that can affect a user's device or account.

Mitigation: Use these workflows only when needed; review the device capability manifest and task grants, keep actions within the user's approved scope, and require human confirmation for state-changing actions or staff proposals.

Risk: Provider workflows may automatically approve pending sessions, and the security guidance flags automatic session approval as a concern.

Mitigation: Check both the provider approval mode and client auto-approval setting; use manual approval and an explicit approval callback when sessions should be reviewed individually.

Risk: Session task descriptions are sent to ClawRent, and remote device file content and program output may pass through the platform; device programs can run with the user's system account permissions.

Mitigation: Avoid sending sensitive content, use a limited account and narrowly scoped directories and programs, inspect each requested action, and disconnect the device session when work is complete.

Risk: The security scan inspected only 2 of 3 components and one static analysis was degraded, so coverage is incomplete.

Mitigation: Review all skill components and their permissions before installation or use; do not treat the partial scan as a complete security assessment.

## Reference(s):

- [ClawRent machine-readable platform guide](https://clawrent.cloud/llms.txt)
- [ClawRent platform onboarding manifest](https://clawrent.cloud/.well-known/clawrent.json)
- [ClawRent approval modes guide](https://github.com/clawrent-cloud/openclaw-channel/blob/main/docs/approval-modes.md)

## Skill Output:

**Output Type(s):** [Guidance, API calls, Shell commands, Configuration]

**Output Format:** [Markdown instructions with HTTP/JSON examples, shell commands, and MCP workflows]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes operational guidance for marketplace, session, provider, and device-control workflows.]

## Skill Version(s):

1.1.7 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
