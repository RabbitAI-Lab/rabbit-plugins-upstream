## Description:

Audit a personal Notion hub and its nested pages and databases to identify mixed content types, empty placeholders, weak navigation, and sensitivity-boundary problems, then produce a practical information-architecture redesign and migration map.

This skill is ready for commercial/non-commercial use.

## Publisher:

[haiyangchenbj](https://clawhub.ai/user/haiyangchenbj)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to audit a personal Notion workspace or page, inspect nested pages and inline databases, and receive a safer, more searchable information-architecture redesign and migration plan.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Auditing a Notion space can expose sensitive personal content to the agent.

Mitigation: Scope the Notion integration to the page or workspace intended for audit and report inaccessible or uncertain areas explicitly.

Risk: Structure creation could alter the user's workspace if authorized too broadly.

Mitigation: Require a separate explicit confirmation before any structure creation and limit authorized changes to empty navigation pages and usage instructions.

Risk: Reports could disclose access tokens or credential-like content.

Mitigation: Never include access tokens in reports or logs, and flag credential-like content for relocation instead of reproducing it.

## Reference(s):

- [Audit Dimensions Checklist](references/audit-checklist.md)
- [ClawHub Skill Page](https://clawhub.ai/haiyangchenbj/skills/notion-personal-space-audit)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Markdown report with scope summary, current-state tree, signal-light findings, proposed architecture, migration table, phased migration order, and no-change declaration.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only by default; any structure creation requires separate explicit authorization and is limited to empty navigation pages and usage instructions.]

## Skill Version(s):

1.0.3 (source: frontmatter and server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
