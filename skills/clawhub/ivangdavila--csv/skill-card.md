## Description:

Parse and generate RFC 4180 compliant CSV that works across tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[ivangdavila](https://clawhub.ai/user/ivangdavila)

### License/Terms of Use:


## Use Case:

Developers and data practitioners use this skill to parse, validate, and generate CSV files that remain interoperable across common tools, locales, encodings, and spreadsheet applications.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: CSV files opened in spreadsheet applications can trigger formula injection when fields begin with characters such as =, +, -, or @.

Mitigation: Review generated CSV fields for spreadsheet formula prefixes and escape or prefix risky values before sharing files with spreadsheet users.

Risk: Locale-specific delimiters, ambiguous dates or numbers, and encoding choices can cause CSV data to be parsed incorrectly across tools.

Mitigation: Document delimiter, encoding, date, and number conventions for each export and validate representative files in the target consuming tools.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/ivangdavila/skills/csv)

## Skill Output:

**Output Type(s):** [guidance, markdown, code, configuration]

**Output Format:** [Markdown guidance with examples and implementation recommendations]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [No code execution, persistence, credential use, or hidden behavior is indicated by the security evidence.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
