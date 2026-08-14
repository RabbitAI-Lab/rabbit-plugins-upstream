## Description:

Excel公式工具 helps agents generate Excel formulas from natural-language descriptions and diagnose spreadsheet errors such as VLOOKUP issues.

This skill is ready for commercial/non-commercial use.

## Publisher:

[thcjp](https://clawhub.ai/user/thcjp)

### License/Terms of Use:

MIT-0

## Use Case:

Employees, analysts, and developers use this skill to turn spreadsheet requirements into Excel formulas and troubleshoot formula errors during office automation workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requests broad file read/write and command-execution authority that is not clearly bounded to spreadsheet help.

Mitigation: Review requested actions before execution, limit workspace permissions, and use it only in an environment where those authorities are acceptable.

Risk: Sensitive spreadsheets, credentials, or broad workspace contents could be exposed if provided to the skill.

Mitigation: Avoid giving the skill sensitive spreadsheets, credentials, or broad workspace access; use sanitized sample data when possible.

Risk: Unscoped file-processing, API, or command behavior can create unexpected changes.

Mitigation: Require explicit commands, file paths, and API destinations before allowing write operations or command execution.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/thcjp/skills/excel-formula)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Guidance, Configuration]

**Output Format:** [Markdown or JSON-formatted response with formulas and diagnostic guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include Excel formulas, spreadsheet diagnostics, and validation steps.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
