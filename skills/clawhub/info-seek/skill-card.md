## Description:

Infoseek is an end-to-end content intelligence and research workflow that discovers sources, scores relevance and credibility, extracts content, detects contradictions, merges cross-source findings, and produces structured Markdown research reports with optional archives.

This skill is ready for commercial/non-commercial use.

## Publisher:

[gyint](https://clawhub.ai/user/gyint)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and agent operators use Infoseek to automate industry research, trend analysis, competitor intelligence, market research, technical research, content collection, report generation, and long-running local knowledge-base workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Optional HTTP, SSE, or REST server modes may expose local files or credential-management controls too broadly.

Mitigation: Prefer stdio/local operation; do not expose network server modes until authentication is mandatory, CORS is narrowed, and file reads are disabled or restricted to an import directory.

Risk: Provider keys and local research artifacts may be stored in user directories or a system keyring.

Mitigation: Review storage locations such as ~/.infoseek, ~/infoseek-archives, and any system keyring before adding provider keys or running archival workflows.

Risk: Key-management tools can rotate, revoke, and report on provider credentials.

Mitigation: Require separate administrator authorization before enabling credential-management tools in shared or network-accessible deployments.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/gyint/skills/info-seek)
- [Configuration](references/configuration.md)
- [External Dependencies](references/external-deps.md)
- [Network Boundary Report](references/network-boundary-report.md)
- [Risk Register](references/risk-register.md)
- [Compliance Audit Report](references/compliance-audit-report.md)
- [API Keys](references/api-keys.md)
- [Credential Tools](references/credential-tools.md)
- [Infoseek MCP Integration Contract](references/Infoseek_MCP集成契约_v1.5.md)
- [Anchor Score Contract](references/Infoseek_Anchor_Score评分契约_v2.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown reports, JSON tool responses, text extracts, shell commands, configuration snippets, and optional local archive files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can stream research progress and can optionally archive reports under an Infoseek archive directory.]

## Skill Version(s):

2.2.0 (source: SKILL.md frontmatter, package.json, CHANGELOG, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
