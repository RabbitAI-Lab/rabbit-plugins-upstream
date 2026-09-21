## Description:

元信MCP yotta-verify-mcp exposes YottaMeta's pre-install static security scanner as a stdio MCP server for scanning skills, packages, and MCP servers before installation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, security reviewers, and agent operators use this skill to check agent skills, packages, and MCP servers before installation, generate audited badges, enforce CI gates, and review JSON or Markdown reports. Its results are advisory and require human confirmation before install or block decisions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Security evidence marks the release suspicious because offline behavior claims, installer persistence, and scanner coverage have review-worthy gaps.

Mitigation: Install only after reviewing installer targets, prefer a single explicit install target, and treat scan results as advisory rather than complete assurance.

Risk: Global or broad install modes can persist the tool across multiple agent environments.

Mitigation: Avoid global install mode unless intentionally needed; use a local directory or explicit agent target and confirm configuration writes before applying them.

Risk: Scanning untrusted archives or npm package specs can introduce handling and provenance uncertainty.

Mitigation: Prefer local directory or tarball scans for offline review and manually confirm the source, version, and authorization for each scanned target.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [Project Homepage](https://github.com/YottaMeta/yotta-verify-mcp)
- [npm Package](https://www.npmjs.com/package/@yottameta/yotta-verify-mcp)
- [Trust Checklist](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [MCP tool responses, JSON or Markdown reports, local SVG badge output, and configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs include scan verdicts, severity summaries, findings, CI gate status, and advisory installation guidance.]

## Skill Version(s):

0.4.3 (source: server release metadata, SKILL.md frontmatter, package.json, skill-manifest.json, server.json, CHANGELOG released 2026-09-19)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
