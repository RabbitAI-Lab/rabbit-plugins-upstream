## Description:

Turns AI video ads into a pass, fix, or block compliance report with rule references, suggested changes, and platform disclosure guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[vargai](https://clawhub.ai/user/vargai)

### License/Terms of Use:

MIT

## Use Case:

External sellers and marketers use the skill to review finished AI video ads before publishing, check claims and depictions against available evidence and platform rules, and prepare a report with fixes and disclosure guidance. The report is a review aid, not legal advice.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitting confidential or unauthorized footage may expose sensitive material.

Mitigation: Use only media and URLs authorized for VARG, and check its privacy terms before submitting confidential footage.

Risk: Platform rules and legal requirements can change, and some cited rule summaries rely on secondary sources.

Mitigation: Treat the report as a checklist and confirm legal or platform conclusions against current authoritative sources.

Risk: Remote services and the optional broader plugin bundle were not inspected in the release review.

Mitigation: Prefer the single-skill installation and reviewed versions.

## Reference(s):

- [Rules reference](artifact/references/rules.json)
- [Example compliance report](artifact/references/example-report.md)
- [VARG documentation](https://varg.ai/how-to)
- [VARG MCP connection](https://mcp.varg.ai/mcp)
- [ClawHub skill page](https://clawhub.ai/vargai/skills/ai-ad-compliance-check)

## Skill Output:

**Output Type(s):** [Analysis, Markdown, Compliance guidance]

**Output Format:** [Markdown report with timed findings, rule references, recommended fixes, and platform disclosure guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are organized as pass, fix, or block items and include a suggested rewrite or reshoot where applicable.]

## Skill Version(s):

1.0.1 (source: server-resolved release metadata; artifact frontmatter reports 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
