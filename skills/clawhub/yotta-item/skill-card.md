## Description:

Assembles reproducible exam papers from a local item bank and blueprint, then checks papers for points, section, difficulty, coverage, and time gaps.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT

## Use Case:

Educators and exam-design teams use the skill to select existing questions from a local bank according to a blueprint and to identify gaps in assembled or existing papers. It supports human review and does not generate question text or answers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A reported scoring bug may leave an assembled paper with incorrect scoring.

Mitigation: Run check with the blueprint and --gate findings=1 after assembly, then manually verify the paper against the blueprint.

Risk: Installation can affect files in the selected agent directory, and an unpinned npx release was not inspected.

Mitigation: Choose one agent or an explicit installation directory, preview with --dry-run, and use reviewed local installer files or an exact verified package release.

Risk: Template generation overwrites its three named files in the target directory.

Mitigation: Generate templates in an empty directory.

## Reference(s):

- [Bank format and validation](references/bank-format.md)
- [Blueprint format and validation](references/blueprint-format.md)
- [Report format and findings](references/report-format.md)
- [Privacy and content boundaries](references/privacy.md)
- [Project homepage](https://github.com/YottaMeta/yotta-item)
- [npm package](https://www.npmjs.com/package/@yottameta/yotta-item)

## Skill Output:

**Output Type(s):** [Files, JSON, Markdown]

**Output Format:** [JSON paper and findings data, Markdown reports, and JSON starter templates]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local deterministic selection; a fixed seed reproduces item selection. Outputs reference bank items and report findings without generating question text or answers.]

## Skill Version(s):

0.1.2 (source: frontmatter, CHANGELOG, package.json, released 2026-11-01)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
