## Description:

Audits a personal Notion hub and its nested pages and databases to identify mixed content, empty placeholders, weak navigation, and sensitivity-boundary issues, then produces a read-only information-architecture redesign and migration map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to have an agent audit a personal Notion workspace or page, including nested pages and inline databases, and produce practical recommendations for safer organization, searchability, sensitivity boundaries, and migration planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may read personal or sensitive Notion content within the selected audit scope.

Mitigation: Keep the Notion integration scoped to only the pages that should be reviewed, and install the skill only when that access is acceptable.

Risk: Optional structure creation could be mistaken for content migration or editing.

Mitigation: Require separate explicit approval for structure creation and limit it to empty navigation pages and usage instructions; do not move, delete, rename, or rewrite existing content.

Risk: Ambiguous or inaccessible Notion content could lead to incorrect organization recommendations.

Mitigation: Mark inaccessible or uncertain areas explicitly and place ambiguous content in pending review instead of forcing a classification.

Risk: Access tokens or credential-like content could appear in reports or logs.

Mitigation: Never expose access tokens in user-facing output, reports, or logs, and flag credential-like content for relocation.

## Reference(s):

- [Audit Dimensions Checklist](references/audit-checklist.md)
- [ClawHub skill page](https://clawhub.ai/haiyangchenbj/skills/notion-personal-space-audit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown audit report with findings, proposed information architecture, migration table, phased migration order, and a declaration that no Notion content was changed.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include optional empty navigation-page setup guidance only after explicit user authorization.]

## Skill Version(s):

1.0.2 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
