## Description:

Create, inspect, and edit Microsoft Excel XLSX workbooks with reliable formulas and dates, supporting Chinese-language agent workflows for workbook creation, checking, and editing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and automation teams use this skill to create, inspect, edit, and validate XLSX workbooks, including formulas, dates, workbook data, and change reports. It is intended for spreadsheet automation in constrained agent workspaces rather than encrypted-file recovery or non-XLSX spreadsheet formats.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad read, write, and command-execution behavior could expose or modify spreadsheet data in ways the skill does not clearly bound.

Mitigation: Run it only in a constrained workspace, use non-sensitive workbook copies, and review proposed commands and file writes before execution.

Risk: API usage and API-key handling are described without enough detail for unattended use with valuable business data.

Mitigation: Require publisher clarification on contacted APIs, credential use, and overwrite behavior before using the skill in production automation.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/excel-xlsx)

## Skill Output:

**Output Type(s):** [Files, Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with JSON-style result examples and generated or edited XLSX files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May propose file reads, writes, command execution, API-key configuration, and workbook validation steps.]

## Skill Version(s):

1.0.2 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
