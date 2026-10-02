## Description:

Scans an agent's skills, MCP configuration, tool permissions, and data access for prompt-injection, tool-boundary, and data-isolation risks, then provides hardening reports and guardrails.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agent operators scan environments they own or are authorized to inspect, prioritize hardening work, and create defensive guardrails. The scan does not replace a human security review or provide runtime enforcement.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A global install can change skill directories across supported agent profiles.

Mitigation: Install only into agent skill directories you control; avoid the global option unless those changes are intended.

Risk: Scanning broad directories may read sensitive files while classifying risks.

Mitigation: Scan narrowly scoped, authorized directories and restrict access to generated reports and audit logs.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-agent-hardening)
- [ClawHub release](https://clawhub.ai/yottameta/skills/yotta-agent-hardening)
- [Detection items](references/detection-items.md)
- [Guardrails template](references/guardrails-template.md)
- [Report template](references/report-template.md)
- [Tutorial](references/tutorial.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Configuration guidance]

**Output Format:** [Plain-text, JSON, or Markdown reports and Markdown guardrails]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scans do not modify target files; audit logs and requested reports are written separately.]

## Skill Version(s):

0.2.7 (source: frontmatter, package.json, ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
