## Description:

Merges U9C export spreadsheets for supported document types into a standardized overdue and stalled-document Excel report.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qingchazhushui](https://clawhub.ai/user/qingchazhushui)

### License/Terms of Use:

MIT-0

## Use Case:

Employees and operations reviewers use this skill to combine U9C export reports for purchasing, receiving, sales, shipping, and payment request workflows into one formatted review workbook.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: A broad folder scan may include similarly named U9C spreadsheets that were not intended for the report.

Mitigation: Use an explicit file list, or provide a narrow input folder and explicit output path before running the merge.

Risk: Incorrect source files or unexpected column layouts can produce an incomplete or misleading compliance workbook.

Mitigation: Review the matched file names and inspect the generated workbook before using it for compliance or administrative action.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qingchazhushui/skills/merge-u9c-reports)
- [Skill instructions](artifact/SKILL.md)

## Skill Output:

**Output Type(s):** [code, shell commands, guidance, files]

**Output Format:** [Python usage guidance and a generated Excel workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Processes local .xlsx files matching U9C filename prefixes and writes one formatted workbook.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
