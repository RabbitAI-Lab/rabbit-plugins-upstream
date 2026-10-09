## Description:

Creates reproducible school-document skeletons from structured facts and checks existing drafts for missing information, inconsistent dates, attachments, student personal data, and wording that needs review.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

School staff and document workflow developers use this skill to draft document structures from supplied facts, review existing school notices and reports for deterministic gaps, and gate automated checks. Human reviewers remain responsible for final approval and safeguarding student information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation can write the skill into agent skill directories beyond the intended project.

Mitigation: Preview installation with --dry-run and prefer a pinned package version with --agent or --dir instead of global installation.

Risk: School documents can contain student personal information, and deterministic checks may miss sensitive content.

Mitigation: Keep documents in controlled local files and manually review privacy findings and the final draft before sharing.

Risk: A generated skeleton or check report may be mistaken for an approved or complete school document.

Mitigation: Confirm missing facts and route the final document through the school's approval process.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/yottameta/skills/yotta-school-doc)
- [Project homepage (listed in skill metadata; import provenance unavailable)](https://github.com/YottaMeta/yotta-school-doc)
- [Privacy guidance](references/privacy.md)
- [Document types and facts format](references/types-format.md)
- [Report format](references/report-format.md)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Guidance]

**Output Format:** [Markdown or JSON document skeletons and check reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports identify findings with source-line evidence; skeletons mark missing facts for completion.]

## Skill Version(s):

0.1.3 (source: frontmatter, package.json, server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
