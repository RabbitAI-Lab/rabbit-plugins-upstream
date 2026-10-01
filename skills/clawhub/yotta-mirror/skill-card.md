## Description:

元镜 yotta-mirror turns structured score or answer sheets and item-to-knowledge maps into reproducible local learning-diagnostics reports with evidence-backed weak-point findings, student layers, review items, and Markdown or JSON output.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

External educators, instructional teams, and automation developers use this skill to analyze class assessment data locally, find weak knowledge points and borderline students, and produce evidence-backed reports for teaching improvement. It is not intended for student ranking, admissions prediction, or replacing teacher judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes student assessment data, and reports may contain sensitive educational records.

Mitigation: Run it only in controlled local directories and keep source data, reports, and archived JSON under the same access controls used for student records.

Risk: The --anonymize option uses reproducible pseudonyms and should not be treated as full anonymization for external sharing.

Mitigation: Review shared reports for re-identification risk, remove unnecessary student-level detail, and treat anonymized outputs as controlled educational data.

Risk: Installer behavior can target broad agent or directory locations.

Mitigation: Prefer explicit --agent or --dir installation, review the target directory before installing, and avoid global installation unless required.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/yottameta/skills/yotta-mirror)
- [Publisher profile](https://clawhub.ai/user/yottameta)
- [Project homepage](https://github.com/YottaMeta/yotta-mirror)
- [Input data format](references/data-format.md)
- [Report and JSON contract](references/report-format.md)
- [Data boundaries and privacy](references/privacy.md)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [Markdown and JSON reports with supporting shell commands and configuration guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Local deterministic analysis; generated_at is expected to vary between runs.]

## Skill Version(s):

0.1.0 (source: frontmatter, package.json, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
