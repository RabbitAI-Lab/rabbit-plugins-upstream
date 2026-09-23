## Description:

Manipulate CSV files from the command line to view, filter, sort, select columns, convert to and from JSON, compute statistics, deduplicate, and merge files.

This skill is ready for commercial/non-commercial use.

## Publisher:

[johnnywang2001](https://clawhub.ai/user/johnnywang2001)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill to inspect, clean, transform, and summarize local CSV datasets from the command line.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated CSV values from untrusted data may contain formula-like cells that remain active when opened in spreadsheet software.

Mitigation: Treat CSV or JSON inputs from untrusted sources cautiously and sanitize formula-like cell values before opening generated files in spreadsheet applications.

Risk: The local command-line helper reads input files and writes outputs specified by the user.

Mitigation: Run commands only on intended local files and review output paths before writing generated CSV or JSON files.

## Reference(s):

- [Csv Toolkit ClawHub page](https://clawhub.ai/johnnywang2001/skills/csv-toolkit)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples, plus command-line text, CSV, or JSON output from the bundled script]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The bundled Python script reads local CSV or JSON files and can write user-specified output files.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
