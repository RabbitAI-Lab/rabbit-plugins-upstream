## Description:

Provides four stdio MCP tools for pre-install static scanning of agent skills and packages, including scan findings, audit badges, CI gates, and JSON or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers use the MCP server in an MCP client or workflow to review authorized skills and packages before installation, inspect findings, and optionally create a CI gate or report. Scan conclusions are advisory and require human review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Scanning some package sources can run untrusted code before the check completes.

Mitigation: Prefer the reviewed local Python scanner with an existing, isolated target, and avoid automatic package retrieval until its sources are restricted and package scripts are disabled.

Risk: Badges and clean scan results may be mistaken for proof that a target is safe.

Mitigation: Treat results as advisory and review the findings and included source inspection; remote packages were not executed during that review.

Risk: Installation settings and report or memory changes can affect user files.

Mitigation: Pin the scanner release, choose a specific installation destination, and approve report paths, configuration, or memory changes before applying them.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-verify-mcp)
- [Pre-install trust checklist](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown, Files]

**Output Format:** [Structured MCP responses, JSON or Markdown reports, and optional SVG badges]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scan results describe one target at a time; report files are written only when requested.]

## Skill Version(s):

0.4.6 (source: target metadata, frontmatter, package.json, CHANGELOG)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
