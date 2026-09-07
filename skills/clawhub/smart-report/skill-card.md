## Description:

Turns CSV, TSV, TXT, Excel, and JSON data files into single-file interactive HTML reports with ECharts visualizations, narrative analysis, and numeric traceability, and can also batch-generate standalone chart HTML files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT

## Use Case:

Developers and analysts use this skill to convert local tabular datasets into data reports, weekly or monthly summaries, analysis documents, reviews, presentation material, and chart deliverables. It is intended for offline report assembly with traceable numeric claims and optional static document exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Automatic transform code may be unsafe or misleading when used with confidential workspaces, untrusted prompts, or sensitive nearby files.

Mitigation: Use the skill only with trusted datasets and prompts, and inspect generated transform code before running it in sensitive workspaces.

## Reference(s):

- [Smart Report skill page](https://clawhub.ai/neuhanli/skills/smart-report)
- [REFERENCE.md](artifact/references/REFERENCE.md)
- [REPORT.md](artifact/references/REPORT.md)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, files]

**Output Format:** [Markdown guidance with JSON configuration, shell commands, generated interactive HTML reports, standalone chart HTML files, and optional DOCX or PPTX exports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Runs locally and offline; generated transform code is reviewed by the skill sandbox but should not be treated as a hard security boundary.]

## Skill Version(s):

1.1.1 (source: evidence release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
