## Description:

Creates, inspects, and edits Excel XLSX workbooks with support for formulas, dates, and Chinese-language interactions.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, business users, and automation teams use this skill to create, inspect, and update XLSX workbooks, validate formulas and dates, and produce workbook files or reports from agent workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill asks for broad read, write, and command authority for workbook handling.

Mitigation: Install only when that authority is acceptable, and review proposed file writes or command execution before proceeding.

Risk: Workbook contents may be read or modified by the agent during processing.

Mitigation: Use only workbooks you are comfortable allowing an agent to access, and provide only files relevant to the task.

Risk: API key guidance is vague.

Mitigation: Do not set an API key unless you know which service requires it, and keep keys in environment variables rather than prompts or files.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/thcjp/skills/excel-xlsx)
- [Skill Homepage](https://skillhub.cn/skill/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Files, Shell commands, Configuration]

**Output Format:** [Markdown or JSON status reports, with generated or edited XLSX files when workbook actions are performed]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May read, create, or modify workbook files; users should confirm before overwriting files or running commands.]

## Skill Version(s):

1.0.1 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
