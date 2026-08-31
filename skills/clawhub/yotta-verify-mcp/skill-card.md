## Description:

元信MCP yotta-verify-mcp exposes YottaMeta's yotta-verify pre-install static scanner as a stdio MCP server with tools for scan verdicts, audited badges, CI gates, and JSON or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to add pre-install trust scanning to MCP clients, agent workflows, or CI gates before installing skills, plugins, or MCP servers. The skill returns scanner verdicts, reports, and badges for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent setup guidance may alter future agent behavior or client configuration beyond the current session.

Mitigation: Require explicit user approval before writing permanent memory, AGENTS.md, global memory, or MCP client configuration.

Risk: The offline claim does not fully apply when scanning npm package names because npm package resolution fetches public packages.

Mitigation: Prefer local directory or pinned tarball scans when offline behavior or reproducibility matters; avoid npx latest for routine use.

Risk: Global multi-agent installation can place the skill in multiple agent directories.

Mitigation: Use a local, explicit MCP configuration path or a single intended agent directory unless broad installation is deliberately approved.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-verify-mcp)
- [Trust Checklist](references/trust-checklist.md)
- [Yotta Verify CLI Reference](https://github.com/YottaMeta/yotta-verify)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Configuration, Guidance]

**Output Format:** [JSON and Markdown reports, SVG badge content, MCP tool responses, and inline shell or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [MCP tools include scan_skill, generate_badge, gate_check, and get_report; report and badge tools can optionally write files.]

## Skill Version(s):

0.2.3 (source: frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
