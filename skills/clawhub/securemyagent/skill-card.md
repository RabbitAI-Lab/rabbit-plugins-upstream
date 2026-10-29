## Description:

Security checkup for this agent. Scores the machine 0-100 (exposed gateway, plaintext secrets, risky skills and MCP servers, broad tool scopes) and gives exact fixes. Use when asked to check, harden or score the agent's security, before installing a skill or MCP server, or on a weekly heartbeat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securemyagent](https://clawhub.ai/user/securemyagent)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use SecureMyAgent to score and review an agent's local security setup, check skills and MCP servers before installation, and get suggested hardening steps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The weekly routine requests uploads of security findings without clearly requiring permission, and scores and status may be publicly queryable.

Mitigation: Start with the local checkup. Require explicit permission before uploads or recurring reporting, explain that scores and status are publicly queryable, and approve fixes and the persistent Guard hook separately.

## Reference(s):

- [SecureMyAgent documentation](https://securemyagent.ai/docs)
- [Guard documentation](https://securemyagent.ai/docs/guard)
- [SecureMyAgent security reporting](https://securemyagent.ai/security)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands, Configuration instructions]

**Output Format:** [Markdown with a security score, findings, recommendations, and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Single-stream report with optional setup and remediation steps.]

## Skill Version(s):

1.4.0 (source: evidence.json release.version)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
