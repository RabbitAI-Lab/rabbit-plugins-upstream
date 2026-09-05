## Description:

Profile and analyze CSV or other tabular data - column types, summary statistics, missing values, and anomalies.

This skill is ready for commercial/non-commercial use.

## Publisher:

[widoxm](https://clawhub.ai/user/widoxm)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data analysts, and other users apply this skill to inspect CSV, TSV, or DataFrame-like tabular data before cleaning, joining, or analyzing it.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CSV or tabular data can contain sensitive or regulated information.

Mitigation: Use the skill only in an agent environment approved for the dataset, and avoid providing highly sensitive data unless that environment is authorized.

Risk: Automatic delimiter, encoding, header, type, duplicate, and outlier detection can produce incorrect or incomplete conclusions.

Mitigation: Review the detected structure and validate important findings before using the recommendations for data cleaning or decision-making.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/widoxm/skills/csv-profiler)

## Skill Output:

**Output Type(s):** [text, markdown, code, guidance]

**Output Format:** [Markdown analysis with tabular summaries, findings, and recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include suggested cleaning steps, type classifications, anomaly flags, and example code or commands when useful.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
