## Description:

Reviews MCP server tool lists for command execution, file writes, network access, and credential exposure, then suggests least-privilege access.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT (Python code only); documentation and theory: all rights reserved

## Use Case:

Developers and security reviewers use this skill before connecting an MCP server to identify risky tool permissions and decide which tools to enable.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A local lexical scan may miss unsafe behavior or flag harmless tool descriptions.

Mitigation: Review high-risk results and tool behavior manually before granting access.

Risk: Broad agent tool permissions could allow more access than the review needs.

Mitigation: Avoid granting Write, WebFetch, or broad Bash access unless needed for the review.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/zhaoxinghua09-cell/skills/mcp-security-scan)
- [Publisher's LGD hub](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [Text, JSON, Guidance]

**Output Format:** [Plain text or JSON scan results with agent-facing guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Tool-level risk labels, high-risk count, and least-privilege advice]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata; bundled version labels differ)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
