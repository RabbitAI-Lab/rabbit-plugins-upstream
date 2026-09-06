## Description:

元信MCP exposes YottaMeta's yotta-verify pre-install security scanner as a stdio MCP server with tools for scan verdicts, audited badges, CI gate checks, and JSON or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers and agent operators use this skill to scan agent skills, plugins, MCP servers, local directories, tarballs, or npm packages before installation. It returns deterministic static-scan verdicts, findings, badges, CI gate results, and reports for human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence marks the release suspicious because it asks agents to edit MCP configuration and persistent agent memory across sessions.

Mitigation: Review before installation; avoid automatic writes to AGENTS.md or global memory, and make any persistent configuration change manually.

Risk: The skill can register an MCP server through an unpinned npx command, which may resolve to a changing package version.

Mitigation: Prefer a manually pinned local configuration or a pinned package version after reviewing the downloaded artifact.

Risk: Offline behavior depends on scan target type; npm package scans may require downloading a public package before analysis.

Mitigation: For offline or reproducible review, scan local directories or already-downloaded tarballs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [npm package @yottameta/yotta-verify-mcp](https://www.npmjs.com/package/@yottameta/yotta-verify-mcp)
- [trust-checklist.md](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [MCP tool responses and Markdown guidance with JSON reports, Markdown reports, badge output, and CI gate status]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan conclusions are static-analysis signals for human confirmation; the skill may propose MCP configuration and persistent memory changes.]

## Skill Version(s):

0.3.0 (source: evidence release, SKILL.md frontmatter, CHANGELOG.md, and package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
