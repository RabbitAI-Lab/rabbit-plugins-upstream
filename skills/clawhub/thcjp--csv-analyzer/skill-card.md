## Description:

CSV数据分析器 helps agents analyze CSV files with Python standard-library workflows for statistics, row filtering, anomaly detection, grouping, aggregation, and result export.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agent users use this skill to inspect CSV files, calculate summary statistics, filter rows, detect basic numeric anomalies, group records, and export derived CSV results. It is not intended for real-time stream processing.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read CSV files selected by the user and may write derived output files.

Mitigation: Use only intended input files, choose explicit output paths in a safe workspace, and avoid overwriting important files.

Risk: The artifact documentation refers to analyzer commands but does not include a concrete analyzer script path.

Mitigation: Verify the analyzer script exists in the installed skill before relying on documented command examples.

## Reference(s):

- [CSV数据分析器 on ClawHub](https://clawhub.ai/thcjp/skills/csv-analyzer)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, code, configuration, guidance]

**Output Format:** [Markdown with inline shell command examples and CSV output guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read selected CSV files and may write derived CSV outputs when explicit output paths are provided.]

## Skill Version(s):

1.0.1 (source: server release metadata; artifact frontmatter reports 1.0.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
