## Description:

Analyzes channel and partner incentive notice spreadsheets, diagnoses weak areas, generates reports, warning lists, visual dashboards, and supports policy document analysis and retrieval.

This skill is ready for commercial/non-commercial use.

## Publisher:

[zxx580353-creator](https://clawhub.ai/user/zxx580353-creator)

### License/Terms of Use:

MIT-0

## Use Case:

Business analysts and channel operations teams use this skill to review partner incentive spreadsheets, identify underperforming grids or channels, and produce concise remediation outputs. Teams can also use it to summarize and search related sales partner policy documents when those documents are provided.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill processes local business Excel and Word files and can generate shareable reports or dashboards containing sensitive operational data.

Mitigation: Use explicit safe input and output folders, and review generated files before distributing them.

Risk: Path-safety and dependency-hygiene caveats were identified in the server security summary.

Mitigation: Set YJ_SRC, YJ_DOC_DIR, and output variables to trusted locations, and pin dependencies before use in a controlled environment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/zxx580353-creator/skills/report-analysis)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Files, Guidance]

**Output Format:** [Markdown guidance plus generated Word, Excel, and self-contained HTML files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses user-provided local Excel and Word documents; outputs should be reviewed before sharing.]

## Skill Version(s):

2.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
