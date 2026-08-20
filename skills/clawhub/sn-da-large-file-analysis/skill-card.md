## Description:

Guides agents through high-performance analysis of Excel datasets with 10,000 or more rows using streaming openpyxl reads, Parquet conversion, chunked processing, memory optimization, and large-file export patterns.

This skill is ready for commercial/non-commercial use.

## Publisher:

[sensenova-skills](https://clawhub.ai/user/sensenova-skills)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and data-analysis agents use this skill to process large Excel workbooks without exhausting memory, converting data to Parquet when useful and choosing streaming, vectorized, and chunked processing strategies by file size.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill reads user-provided spreadsheet data and can create analysis, cache, and output files that may contain sensitive data.

Mitigation: Review output paths and data handling before using the skill with sensitive datasets.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/sensenova-skills/skills/sn-da-large-file-analysis)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Python code blocks and command constraints]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance may lead agents to create Parquet, CSV, XLSX, and PNG output files during analysis workflows.]

## Skill Version(s):

2026.8.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
