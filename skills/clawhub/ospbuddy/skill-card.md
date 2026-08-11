## Description:

OpsBuddy guides agents through connecting an external operations-monitoring MCP service so users can query asset discovery, health checks, diagnostics, logs, alerts, and remediation suggestions in natural language.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hatjs880328s](https://clawhub.ai/user/hatjs880328s)

### License/Terms of Use:

MIT-0

## Use Case:

External users and operations engineers use this skill to connect OpsBuddy to OpenClaw and ask natural-language questions about monitoring data, service health, alerts, logs, and likely fault causes. The skill focuses on connection guidance and safe credential handling rather than directly installing or storing MCP credentials for the user.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The downloaded MCP configuration contains a plaintext API key.

Mitigation: Keep the token out of chat, add it only through OpenClaw's MCP configuration flow, and revoke and reissue it through the OpsBuddy portal if it leaks.

Risk: Monitoring platform credentials are managed through OpsBuddy's external gateway.

Mitigation: Install only when that data flow is intended, review the downloaded MCP configuration before enabling it, and manage platform credentials through the OpsBuddy portal.

## Reference(s):

- [ClawHub OpsBuddy Listing](https://clawhub.ai/hatjs880328s/skills/ospbuddy)
- [OpsBuddy Portal](https://ywdz.lxiai.com/)

## Skill Output:

**Output Type(s):** [guidance, markdown, configuration]

**Output Format:** [Markdown guidance with inline JSON configuration examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided OpsBuddy MCP token; the skill instructs users not to paste credentials into chat.]

## Skill Version(s):

1.0.8 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
