## Description:

Check authorization, endpoint, and authentication of an A2A Agent Card with a read-only diagnostic before connecting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kadopi](https://clawhub.ai/user/kadopi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill before connecting to an A2A agent they own or are explicitly authorized to reach, to check whether the Agent Card, endpoint, and authentication declaration are ready for connection.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can send Bearer credentials for an authenticated agent endpoint to an external MCP service.

Mitigation: Prefer unauthenticated checks or a dedicated short-lived, narrowly scoped diagnostic token; do not use normal production credentials unless the organization has approved that trust boundary.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/kadopi/skills/agent-card-health-check)
- [MCP Service Card](https://agent-card-health-check.kadopi.workers.dev/.well-known/agent-card.json)
- [Product Page](https://aegis-sales-bot.kadopi.workers.dev/products/agent-card-health-check)
- [Source](https://github.com/kadopi/my-projects/tree/main/apps/agent-card-health-check)
- [MCP Registry Search](https://registry.modelcontextprotocol.io/?q=io.github.kadopi%2Fagent-card-health-check)

## Skill Output:

**Output Type(s):** [text, guidance]

**Output Format:** [Markdown text with diagnostic result interpretation and a minimal owner action]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports connection readiness and missing or mismatched configuration; does not label the target safe or unsafe.]

## Skill Version(s):

0.1.1 (source: server release evidence, created 2026-09-16)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
