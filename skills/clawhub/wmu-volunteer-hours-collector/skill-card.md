## Description: <br>
WMU志愿时长收集器 helps Wenzhou Medical University student union practice departments consolidate volunteer signup spreadsheets into standardized monthly volunteer-hour Excel summaries. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[pkx07](https://clawhub.ai/user/pkx07) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Student union practice department staff at Wenzhou Medical University use this skill to process multiple volunteer signup spreadsheets, normalize student, activity, and hour fields, and produce a standardized monthly Excel workbook with a review summary. <br>

### Deployment Geography for Use: <br>
China <br>

## Known Risks and Mitigations: <br>
Risk: The skill reads and writes files in the target spreadsheet folder. <br>
Mitigation: Run it in a dedicated folder containing only the intended source spreadsheets and keep backups of original files before allowing writes. <br>
Risk: The security summary flags unnecessary network use for the stated workflow. <br>
Mitigation: Deny network access unless the skill gives a clear, task-specific reason and the user approves it. <br>
Risk: Spreadsheet normalization may infer ambiguous activity, student, major, grade, or hour values. <br>
Mitigation: Review the generated summary for unresolved confirmations, grade and student ID mismatches, missing group leaders, capped hours, and other reported exceptions before relying on the workbook. <br>


## Reference(s): <br>
- [College and Major Mapping Reference](references/mapping.md) <br>
- [Merged Cell Handling Reference](references/merged-cell-trap.md) <br>
- [ClawHub Skill Page](https://clawhub.ai/pkx07/skills/wmu-volunteer-hours-collector) <br>


## Skill Output: <br>
**Output Type(s):** [files, text, code, shell commands, guidance] <br>
**Output Format:** [Excel workbook plus concise text or Markdown status summary] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Produces a copied and renamed volunteer-hours workbook, then reports processed record counts and data issues that need review.] <br>

## Skill Version(s): <br>
1.1.0 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
