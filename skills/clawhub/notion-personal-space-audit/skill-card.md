## Description:

Audit a personal Notion hub and its nested pages and databases to identify structural, navigational, and sensitivity issues, then produce an information architecture redesign and migration map; the audit is read-only unless a change is explicitly authorized.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

People organizing a personal Notion workspace use this skill to inspect a hub and its nested pages or databases, identify information architecture and sensitivity issues, and plan a clearer structure and migration. It produces an audit report without changing Notion content unless a change is explicitly authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read and summarize Notion content outside the selected personal hub; the security review is partial and its evidence is incomplete.

Mitigation: Confirm the target and crawl scope with the user, keep the audit within that scope, and describe unreviewed or inaccessible areas as uncertain.

## Reference(s):

- [Audit Dimensions Checklist](references/audit-checklist.md)
- [ClawHub skill release](https://clawhub.ai/haiyangchenbj/skills/notion-personal-space-audit)
- [Publisher profile](https://clawhub.ai/user/haiyangchenbj)

## Skill Output:

**Output Type(s):** [Markdown, Guidance]

**Output Format:** [Markdown audit report with findings, a proposed information architecture, a migration map, and phased recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; no Notion content is changed unless explicitly authorized.]

## Skill Version(s):

1.0.5 (source: frontmatter, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
