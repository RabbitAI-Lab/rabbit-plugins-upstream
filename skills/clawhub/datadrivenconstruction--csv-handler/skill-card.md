## Description:

Handle CSV files from construction software exports. Auto-detect delimiters, encodings, and clean messy data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction)

### License/Terms of Use:

MIT

## Use Case:

Developers and construction project teams use this skill to profile, clean, merge, split, convert, and export CSV data from construction software such as schedule and cost exports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can read local project files and generate new CSV files.

Mitigation: Install only when local file access is acceptable, use dedicated output folders, and review destinations before export.

Risk: Split and export behavior can create files from user-provided column names or values.

Mitigation: Avoid splitting on untrusted column values, review generated filenames, and treat generated CSVs as untrusted before opening them in spreadsheet software.

## Reference(s):

- [Data Driven Construction](https://datadrivenconstruction.io)
- [ClawHub Skill Page](https://clawhub.ai/datadrivenconstruction/skills/csv-handler)

## Skill Output:

**Output Type(s):** [text, markdown, code, files, guidance]

**Output Format:** [Markdown tables and prose, with optional Python code snippets and generated CSV, Excel, or JSON files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires user-provided data or file paths; Python 3 is required by the skill metadata.]

## Skill Version(s):

2.1.0 (source: server release metadata and target metadata; artifact/claw.json lists 2.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
