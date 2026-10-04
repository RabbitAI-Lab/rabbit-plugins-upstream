## Description:

Reviews MCP tool names and descriptions for command execution, file writing, network access, and credential exposure, then suggests least-privilege access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); All rights reserved (documentation and theory)

## Use Case:

Developers and engineers can review a third-party MCP server's tool list before connecting it to an agent and decide which tools to authorize.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad shell, file-write, and network permissions could expose local data if granted unnecessarily.

Mitigation: Run the scanner locally with only the permissions needed for the selected tool list; grant write or network access only when explicitly required.

Risk: Keyword checks on tool names and descriptions cannot establish whether a server is safe.

Mitigation: Review flagged tools and the server's actual behavior before connecting it; disable or isolate high-risk tools by default.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/zhaoxinghua09-cell/skills/mcp-security-scan)
- [Publisher homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON risk report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Per-tool risk ratings, high-risk tool count, and least-privilege advice]

## Skill Version(s):

1.0.3 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
