## Description:

Audits a personal Notion hub and nested pages or databases to identify mixed content types, empty placeholders, weak navigation, and sensitivity-boundary issues, then produces an information-architecture redesign and migration map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to audit a personal Notion workspace or page, inspect nested pages and databases, diagnose usability and privacy-boundary problems, and produce a practical migration plan before any structural change is authorized.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The agent may access selected Notion pages and nested content that contain personal or sensitive material.

Mitigation: Grant access only to pages intended for audit, keep the integration scoped to those pages, and avoid storing secrets in Notion pages selected for inspection.

Risk: The audit report may surface sensitive findings from the inspected workspace.

Mitigation: Review the generated Markdown report before sharing it or authorizing any follow-up structure creation.

Risk: Authorized structure creation could exceed the intended audit scope if permission is too broad.

Mitigation: Require explicit authorization before any write action and limit creation to empty navigation pages and usage instructions.

## Reference(s):

- [Audit Dimensions Checklist](references/audit-checklist.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with audit findings, proposed information architecture, migration table, phased migration order, and declaration that no Notion content was changed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; structure creation is limited to empty navigation pages only after explicit user authorization.]

## Skill Version(s):

1.0.3 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
