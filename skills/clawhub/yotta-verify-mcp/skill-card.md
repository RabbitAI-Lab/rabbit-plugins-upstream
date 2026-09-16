## Description:

元信MCP yotta-verify-mcp exposes YottaMeta's pre-install static security scanner as a stdio MCP server with tools for scans, audited badges, CI gates, and JSON or Markdown reports.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Developers, agent operators, and security reviewers use this skill to run pre-install static trust scans on agent skills, plugins, and MCP servers before deciding whether to install or promote them.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review says package-name targets may contact npm even though the skill describes local or offline scanning.

Mitigation: Use local directories or pre-fetched tarballs when network-free operation is required, and confirm expected npm retrieval behavior before scanning package-name targets.

Risk: The security review says scans of untrusted local directories can read outside the selected root through symlinks.

Mitigation: Avoid scanning untrusted directories that contain symlinks until the symlink-root escape is fixed; prefer vetted archives or inspect symlinks before scanning.

Risk: The security guidance says the installer can persist itself into agent skill directories.

Mitigation: Avoid global installation unless every listed agent should see the skill, and review target paths before allowing installer or configuration writes.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-verify-mcp)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-verify-mcp)
- [trust-checklist](references/trust-checklist.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [MCP tool results, JSON or Markdown reports, badge output, and CLI or configuration snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Returns scan verdicts and findings for human review; install decisions remain user-confirmed.]

## Skill Version(s):

0.4.2 (source: SKILL.md frontmatter, package.json, CHANGELOG, ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
