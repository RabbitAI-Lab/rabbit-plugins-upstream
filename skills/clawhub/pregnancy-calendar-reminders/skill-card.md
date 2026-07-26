## Description: <br>
Generates, verifies, updates, and helps import bilingual pregnancy reminder calendars from a last menstrual period date or doctor-adjusted due date. <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[5fivelogistic-cell](https://clawhub.ai/user/5fivelogistic-cell) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and agents use this skill to calculate pregnancy date anchors, generate importable calendar reminders, and verify the resulting due date, event counts, and prenatal checkup windows. It is for family planning, appointment preparation, and reminder workflows, not diagnosis or individualized medical care. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Pregnancy reminders could be mistaken for medical advice or individualized clinical direction. <br>
Mitigation: Use the calendar for planning and appointment reminders only, follow obstetric guidance, and seek care promptly for danger signs described by the skill. <br>
Risk: Incorrect date anchors or stale calendar versions could create misleading reminders. <br>
Mitigation: Review the generated outline and validation report, confirm validation_passed is true, and use doctor-adjusted due dates when provided. <br>
Risk: Generated calendar files or optional live calendar changes could affect the wrong calendar. <br>
Mitigation: Review the output directory before import and only allow direct macOS Calendar changes when explicitly requested and the target calendar name matches this workflow. <br>


## Reference(s): <br>
- [Pregnancy Reminder Rules](artifact/references/pregnancy_rules.md) <br>
- [Skill README](artifact/README.md) <br>


## Skill Output: <br>
**Output Type(s):** [Files, Markdown, JSON, Shell commands, Guidance] <br>
**Output Format:** [Markdown guidance plus generated .ics, JSON, outline, and validation report files] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Runs locally and validates pregnancy anchors, key reminder windows, event counts, and calendar file consistency before delivery.] <br>

## Skill Version(s): <br>
1.0.0 (source: server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
