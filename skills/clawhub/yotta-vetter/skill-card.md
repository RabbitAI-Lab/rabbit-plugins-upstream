## Description:

A pre-install review protocol that combines a four-phase source, code, permissions, and risk checklist with a lightweight scanner and a deep-scan handoff.

This skill is ready for commercial/non-commercial use.

## Publisher:

[yottameta](https://clawhub.ai/user/yottameta)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and people evaluating skills use this protocol before installation to review source, code patterns, permissions, and risks and produce a structured report. A human reviews the findings and confirms the final decision.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing an upgrade can overwrite existing skill files.

Mitigation: Use a reviewed, version-pinned package and confirm the intended agent or destination directory.

Risk: A scan may cover an unintended folder or symlink target.

Mitigation: Scan only the intended skill folder and review its symlinks.

Risk: A clean scan is only a preliminary result and cannot make the final installation decision.

Mitigation: Retain human review and confirm the decision after reviewing the report.

Risk: This artifact review does not cover future npm releases or the separate deep-scanning tool.

Mitigation: Review the exact release being used and assess the companion deep-scanning tool separately when needed.

## Reference(s):

- [Project homepage](https://github.com/YottaMeta/yotta-vetter)
- [Four-phase vetting checklist](references/checklist.md)
- [Vetting report template](references/vetting-report-template.md)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON, Shell commands]

**Output Format:** [Text, Markdown, or JSON vetting reports, with shell commands for an optional deep-scan handoff]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports support human review; conclusions require human confirmation.]

## Skill Version(s):

0.2.8 (source: frontmatter, CHANGELOG, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
