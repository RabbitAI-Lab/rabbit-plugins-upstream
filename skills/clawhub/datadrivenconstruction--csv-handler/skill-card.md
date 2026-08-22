## Description: <br>
Handle CSV files from construction software exports, including delimiter and encoding detection, data cleaning, merging, splitting, and type conversion. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[datadrivenconstruction](https://clawhub.ai/user/datadrivenconstruction) <br>

### License/Terms of Use: <br>
MIT <br>


## Use Case: <br>
Construction project managers, analysts, and developers use this skill to process project CSV exports, clean messy tabular data, and prepare schedule or cost data for review, merging, splitting, or export. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The activation wording is broader than the CSV-focused implementation, so users may expect support for tasks outside local construction CSV or related tabular-data workflows. <br>
Mitigation: Use the skill for CSV and closely related tabular cleanup or analysis, and clarify unsupported requests before processing. <br>
Risk: Generated exports or cleaned data may be incorrect if input paths, delimiters, encodings, or inferred data types are wrong. <br>
Mitigation: Use explicit file paths, validate inputs before processing, and review generated exports before relying on them. <br>


## Reference(s): <br>
- [ClawHub Skill Listing](https://clawhub.ai/datadrivenconstruction/skills/csv-handler) <br>
- [Publisher Homepage](https://datadrivenconstruction.io) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, code, configuration, guidance] <br>
**Output Format:** [Markdown with structured tables, Python code examples, and optional CSV, Excel, or JSON export guidance] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses user-provided local data paths or direct tabular input; Python 3 is required for the implementation examples.] <br>

## Skill Version(s): <br>
2.1.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
