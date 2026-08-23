## Description:

Smart Charts reads user-supplied tabular data files, helps agents analyze data characteristics, recommends chart types, and generates offline interactive ECharts HTML visualizations.

This skill is ready for commercial/non-commercial use.

## Publisher:

[neuhanli](https://clawhub.ai/user/neuhanli)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external users use this skill to inspect local CSV, TSV, TXT, Excel, or JSON data, select appropriate chart forms, and produce shareable offline HTML visualizations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can execute AI-generated Python transform code in the user's environment, and the security evidence rates this containment as weak.

Mitigation: Use transform-code workflows only on trusted datasets, inspect generated transform code for unexpected file or network operations, and run the skill in an isolated environment for sensitive data.

Risk: The skill reads local data files supplied by the user and writes local HTML outputs.

Mitigation: Provide only intended input files, review output locations, and install only when local file access and HTML generation are acceptable for the data being processed.

## Reference(s):

- [Smart Charts Reference](artifact/references/REFERENCE.md)
- [ClawHub Skill Page](https://clawhub.ai/neuhanli/skills/smart-charts)

## Skill Output:

**Output Type(s):** [text, code, shell commands, files, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI status; generated artifacts are self-contained HTML files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reads local data files up to 100 MB and writes offline ECharts HTML outputs; no network access is required.]

## Skill Version(s):

6.1.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
