## Description:

MCP Security Scan helps agents inspect MCP server tool lists for command execution, file write, network egress, and credential exposure risks before connection, then report ratings and least-privilege guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zhaoxinghua09-cell](https://clawhub.ai/user/zhaoxinghua09-cell)

### License/Terms of Use:

MIT

## Use Case:

Developers and security reviewers use this skill before connecting a third-party MCP server to an agent. It scans a provided tool list for four common risk classes and returns risk ratings with least-privilege recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The documented global install path can retrieve changed upstream content and make the skill persistent across future agent sessions.

Mitigation: Install from a pinned release or commit, verify downloaded files against reviewed hashes, and avoid global installation unless broad availability is intended.

Risk: The scanner is local and narrow, so it should not be treated as a complete security review of an MCP server.

Mitigation: Review the tool definitions and bundled script before use, then apply the reported high-risk findings as inputs to isolation and least-privilege decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zhaoxinghua09-cell/skills/mcp-security-scan)
- [Project homepage](https://zhaoxinghua09-cell.github.io/lgd-hub/)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Plain text or JSON risk report with command-line usage examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic local scan of an MCP tools JSON input; no third-party runtime dependencies are described in the artifact.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
