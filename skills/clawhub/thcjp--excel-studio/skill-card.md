## Description:

Excel工作室 helps agents generate Excel-oriented data tables, reports, charts, analysis summaries, and structured outputs for Chinese-language office automation workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, teams, and automation users can use this skill to guide an agent through spreadsheet generation, data analysis, report creation, chart output, and structured result handling. It is not intended for real-time streaming data processing or complex decisions that require human judgment.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad read, write, and execute authority without clearly scoping allowed commands or file paths.

Mitigation: Use it only in trusted workspaces and require confirmation before command execution or file overwrite.

Risk: The skill references external API use without clearly identifying the destination service.

Mitigation: Avoid providing secrets or sensitive spreadsheets unless the API destination and data handling are known.

Risk: Spreadsheet outputs and generated reports may be used directly in business workflows.

Mitigation: Review generated tables, charts, summaries, and structured results before relying on them for decisions.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/excel-studio)
- [Publisher profile](https://clawhub.ai/user/thcjp)
- [Skill homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON examples and shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide an agent to create spreadsheet-oriented files, reports, charts, summaries, and structured JSON-style results.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
