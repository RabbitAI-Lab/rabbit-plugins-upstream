## Description:

OpsBuddy helps users connect OpenClaw to a third-party ops MCP service for monitoring platform management, asset discovery, real-time monitoring, diagnosis, log search, alert analysis, and remediation guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[hatjs880328s](https://clawhub.ai/user/hatjs880328s)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, SREs, and operations teams use this skill to connect OpenClaw to OpsBuddy and understand how to manage monitoring platforms, discover assets, inspect system health, diagnose incidents, search logs, analyze alerts, and obtain remediation guidance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Connecting OpenClaw to the third-party OpsBuddy gateway may expose monitoring data and platform credentials configured on the portal.

Mitigation: Review the portal's trust model and access controls before connecting production systems, and grant only the access required for the intended operations workflow.

Risk: The downloaded MCP config contains a plaintext API key.

Mitigation: Keep the token out of chat, add it only through OpenClaw MCP settings, and revoke and reapply for the key if it leaks.

## Reference(s):

- [OpsBuddy ClawHub skill page](https://clawhub.ai/hatjs880328s/skills/ospbuddy)
- [OpsBuddy portal](https://ywdz.lxiai.com/)
- [Publisher profile](https://clawhub.ai/user/hatjs880328s)

## Skill Output:

**Output Type(s):** [guidance, configuration, markdown]

**Output Format:** [Markdown guidance with an optional JSON configuration template]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-managed OpsBuddy MCP token; the skill should not collect API keys or write MCP configuration files.]

## Skill Version(s):

1.0.6 (source: evidence.release.version and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
