## Description:

Helps solo-company users turn recurring work into executable, checkable, transferable, and iterative SOPs while identifying steps suitable for AI or automation.

This skill is ready for commercial/non-commercial use.

## Publisher:

[cglt2026opc](https://clawhub.ai/user/cglt2026opc)

### License/Terms of Use:

MIT-0

## Use Case:

External users and solo-company operators use this skill to convert recurring workflows into structured SOP documents with execution steps, deliverables, quality checks, exception handling, and practical automation opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Generated SOPs can contain sensitive business process details.

Mitigation: Review generated content before saving or sharing it, and use the skill only in a workspace where creating local SOP documents is acceptable.

Risk: The skill can create Markdown files and duplicate a bundled spreadsheet template, which may affect local files if paths or filenames are not reviewed.

Mitigation: Confirm output paths, filenames, and overwrite behavior before writing files.

Risk: The bundled weekly workflow sheet contains a repeated column name that can make generated worksheet updates ambiguous.

Mitigation: When creating a new version, rename the fourth column to "下周行动" or another user-specified field.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/cglt2026opc/skills/sop-generator)
- [Bundled daily workflow SOP spreadsheet template](artifact/assets/一人公司每日工作流SOP模板.xlsx)

## Skill Output:

**Output Type(s):** [text, markdown, files, guidance]

**Output Format:** [Markdown SOP document with optional XLSX template copy and concise process guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Defaults to saving SOP output as SOP_{process name}.md; may copy the bundled spreadsheet template when the user needs daily, weekly, or monthly workflow worksheets.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
