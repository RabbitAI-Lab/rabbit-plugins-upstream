## Description:

Checks authorization, endpoint, and authentication for an authorized A2A Agent Card with a read-only diagnostic before connecting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[kadopi](https://clawhub.ai/user/kadopi)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators use this skill before connecting to an A2A agent they own or are explicitly authorized to reach. It helps check the Agent Card, endpoint, and authentication declaration for connection readiness.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Agent Card and authorized target URL data is sent to a disclosed third-party MCP service.

Mitigation: Use the skill only when you are comfortable sharing those inputs with the publisher-operated service.

Risk: Checks against systems without permission can create authorization or compliance risk.

Mitigation: Run diagnostics only for agents and target URLs you own or are explicitly authorized to test.

Risk: The diagnostic may be mistaken for a full security assessment.

Mitigation: Treat results as connection readiness guidance and perform separate security review before relying on an agent in sensitive workflows.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/kadopi/agent-card-health-check-skill)
- [ClawHub skill page](https://clawhub.ai/kadopi/skills/agent-card-health-check)
- [MCP Service Card](https://agent-card-health-check.kadopi.workers.dev/.well-known/agent-card.json)
- [MCP Registry entry](https://registry.modelcontextprotocol.io/?q=io.github.kadopi%2Fagent-card-health-check)
- [Product page](https://aegis-sales-bot.kadopi.workers.dev/products/agent-card-health-check)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown or plain text diagnostic guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only connection readiness check; not a full security assessment.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
