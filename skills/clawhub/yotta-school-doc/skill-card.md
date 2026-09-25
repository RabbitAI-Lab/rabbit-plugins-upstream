## Description:

Yotta-school-doc helps agents locally create reproducible school document skeletons and check existing drafts for missing fields, structure gaps, date problems, attachment mismatches, placeholders, student personal data, sensitive wording, overclaims, and incomplete meeting action items.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

School staff, education administrators, and automation maintainers use this skill to draft document skeletons from structured facts and to validate notices, parent letters, requests, reports, summaries, meeting minutes, plans, and briefings before review or CI gating.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installer scripts can persistently copy the skill into multiple agent skill directories and may overwrite existing yotta-school-doc folders without confirmation.

Mitigation: Install with an explicit --agent or --dir target, avoid broad installs unless intended, pin or review the package source, and inspect existing target folders before installation.

Risk: Rule-based student personal information checks can miss sensitive data or flag benign content.

Mitigation: Treat privacy findings as prompts for human review, and have school staff verify public documents before signing or publication.

Risk: The skill identifies structural gaps and risky wording but does not provide legal, compliance, inspection, or ideological-review conclusions.

Mitigation: Route final drafts through the school's normal approval chain and verify all facts, dates, numbers, document numbers, attachments, and conclusions before issuance.

## Reference(s):

- [Homepage](https://github.com/YottaMeta/yotta-school-doc)
- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-school-doc)
- [Privacy and usage boundaries](references/privacy.md)
- [Report format contract](references/report-format.md)
- [Document type and facts contract](references/types-format.md)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-school-doc)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON document skeletons, Markdown or JSON check reports, and CLI guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are deterministic for the same facts and rule pack except for generated timestamps.]

## Skill Version(s):

0.1.2 (source: SKILL.md frontmatter, package.json, release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
