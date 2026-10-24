## Description:

Audits a personal Notion space for organization, navigation, and privacy issues, then proposes an information architecture and migration plan without changing content by default.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

Individuals and their assistants use this skill to review a personal Notion workspace, identify structural and sensitivity-boundary problems, and plan a safer, easier-to-navigate layout.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The audit can expose private pages and databases to the agent.

Mitigation: Grant read access only to the Notion content needed for the requested audit.

Risk: Optional structure creation or guide-page updates can change the wrong Notion content.

Mitigation: Keep the audit read-only; before any separate write, confirm the target parent or page and the expected changes.

## Reference(s):

- [Notion Personal Space Audit on ClawHub](https://clawhub.ai/haiyangchenbj/skills/notion-personal-space-audit)
- [Audit Dimensions Checklist](references/audit-checklist.md)

## Skill Output:

**Output Type(s):** [Analysis, Guidance]

**Output Format:** [Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Scope and crawl summary, findings, proposed structure, migration map, and a statement of whether Notion content was changed.]

## Skill Version(s):

1.0.4 (source: frontmatter and server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
