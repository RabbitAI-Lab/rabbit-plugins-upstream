## Description:

Security checkup for this agent. Scores the machine 0-100 (exposed gateway, plaintext secrets, risky skills and MCP servers, broad tool scopes) and gives exact fixes. Use when asked to check, harden or score the agent's security, before installing a skill or MCP server, or on a weekly heartbeat.

This skill is ready for commercial/non-commercial use.

## Publisher:

[securemyagent](https://clawhub.ai/user/securemyagent)

### License/Terms of Use:

MIT-0

## Use Case:

Agent operators and developers use SecureMyAgent to assess and harden their agent setup, review a skill or MCP server before installation, and receive findings with concrete remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The weekly routine uploads security findings without clearly requiring your permission, even though online reporting is described as optional.

Mitigation: Use local checkup without --upload unless you explicitly choose online reporting; make that choice cover recurring checks, understand that status and score become public, and review the pinned package before relying on its redaction claims.

## Reference(s):

- [SecureMyAgent](https://securemyagent.ai)
- [SecureMyAgent documentation](https://securemyagent.ai/docs)
- [SecureMyAgent security reporting](https://securemyagent.ai/security)
- [ClawHub skill page](https://clawhub.ai/securemyagent/skills/securemyagent)

## Skill Output:

**Output Type(s):** [Analysis, Guidance, Shell commands]

**Output Format:** [Markdown security summary with a score, findings, and remediation steps]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The checkup can also return JSON when requested.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
