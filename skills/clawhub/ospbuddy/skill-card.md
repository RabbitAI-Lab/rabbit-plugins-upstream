## Description:

OpsBuddy helps users configure an API-key-protected MCP connection for an intelligent operations assistant that supports monitoring integration, asset discovery, fault diagnosis, log search, alert analysis, and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hatjs880328s](https://clawhub.ai/user/hatjs880328s)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, and IT teams use this skill to connect OpsBuddy to WorkBuddy through an MCP configuration, then use the portal for monitoring platform integration and operations workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may expose an OpsBuddy MCP token in the assistant conversation and persist it in ~/.workbuddy/mcp.json.

Mitigation: Place the config locally when possible, redact secrets from chat, set restrictive file permissions, and know how to revoke or rotate the token before enabling the server.

Risk: The server security verdict is suspicious because token-handling safeguards are not adequate.

Mitigation: Review the skill before installation and enable it only after confirming that local storage and token rotation practices meet your security requirements.

## Reference(s):

- [OpsBuddy ClawHub Skill Page](https://clawhub.ai/hatjs880328s/skills/ospbuddy)

## Skill Output:

**Output Type(s):** [text, configuration, guidance]

**Output Format:** [Markdown guidance with JSON configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May write or merge an MCP server entry in ~/.workbuddy/mcp.json after the user supplies a token-bearing config.]

## Skill Version(s):

1.0.2 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
