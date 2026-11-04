## Description:

元公 creates reproducible school-document skeletons from rule packs and structured facts, and checks existing drafts for missing fields, date and attachment issues, placeholders, student personal information, sensitive wording, overclaims, and incomplete meeting actions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

School document authors and administrators use this skill to create structured drafts and check existing notices, reports, meeting minutes, and related documents. Developers can also use its deterministic checks in batch workflows or CI.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installation may overwrite existing files or customized skill content.

Mitigation: Choose one installation destination, preview changes with --dry-run, and back up customized installations before replacing files.

Risk: Generated reports may quote student personal information from source documents.

Mitigation: Protect reports and use an appropriate internal channel when they contain student information.

Risk: A generated template may interact with files already in its output directory.

Mitigation: Generate templates in a fresh directory.

## Reference(s):

- [Document type and facts format](references/types-format.md)
- [Report format and findings](references/report-format.md)
- [Privacy and use boundaries](references/privacy.md)
- [Project repository](https://github.com/YottaMeta/yotta-school-doc)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-school-doc)

## Skill Output:

**Output Type(s):** [Markdown, JSON, Validation guidance]

**Output Format:** [Markdown or JSON document skeletons and validation reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Deterministic findings include line evidence where available; missing facts remain explicit placeholders.]

## Skill Version(s):

0.1.4 (source: SKILL.md frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
