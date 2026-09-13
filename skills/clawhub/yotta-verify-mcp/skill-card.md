## Description:

Yotta-verify-mcp exposes a local stdio MCP server that statically scans agent skills, plugins, and MCP servers before installation and returns verdicts, badges, CI gates, and JSON or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent operators, and security reviewers use this skill to add pre-install static trust checks to MCP clients and agent workflows before installing or using third-party skills, plugins, or MCP servers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Persistent MCP or agent configuration changes may remain active beyond the initial session.

Mitigation: Review configuration changes before installing and prefer a one-time local Python invocation unless persistent registration is intended.

Risk: Automatic global memory or policy edits can create broad recurring behavior.

Mitigation: Require explicit user approval before modifying global memory, AGENTS.md, or equivalent agent policy files.

Risk: The unpinned npx -y configuration can fetch package code at runtime.

Mitigation: Pin the package version or use the local Python script path when reproducibility or change control is required.

Risk: Report output paths could place generated files outside the intended review area.

Mitigation: Permit report outputs only inside a dedicated workspace directory.

Risk: Npm package-name scans may involve network package download activity despite offline positioning.

Mitigation: Treat npm target scans as network activity and use directory or tarball scans when a fully offline review is required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-verify-mcp)
- [Trust checklist](references/trust-checklist.md)
- [Yotta Verify CLI reference](https://github.com/YottaMeta/yotta-verify)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [MCP tool results, JSON or Markdown reports, badge output, configuration snippets, and command guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports may be written to a caller-selected path; scanned-code execution and runtime sandboxing are outside the skill's stated scope.]

## Skill Version(s):

0.4.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
