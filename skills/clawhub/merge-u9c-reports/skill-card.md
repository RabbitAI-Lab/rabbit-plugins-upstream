## Description:

Merges U9C system export reports into a standardized overdue/stalled document Excel workbook organized by document type.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qingchazhushui](https://clawhub.ai/user/qingchazhushui)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operations staff, and finance or compliance reviewers use this skill to combine one or more U9C Excel exports into a single formatted overdue/stalled document report for review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running the skill against a broad or unintended folder can merge the wrong U9C report exports.

Mitigation: Use folders containing only the intended U9C exports, and prefer explicit file lists when practical.

Risk: Saving to an existing output path can replace a workbook.

Mitigation: Confirm the output filename before running and provide the input folder and output path explicitly.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qingchazhushui/skills/merge-u9c-reports)

## Skill Output:

**Output Type(s):** [Code, Shell commands, Configuration instructions, Files, Guidance]

**Output Format:** [Markdown guidance with Python examples and a generated Excel workbook]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces one formatted .xlsx workbook from matching U9C .xlsx inputs.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
