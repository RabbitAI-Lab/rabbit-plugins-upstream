## Description:

帮助独立教师完成新学员试听诊断、需求访谈和经监护人同意的最小化学员建档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师用它收集必要的学习信息、设计诊断式试听课、记录观察，并在确认监护人同意后建立学员档案；试听后跟进止于报名，不处理排课或续费。

### Deployment Geography for Use:

China (adapt consent, privacy, and retention requirements before use elsewhere)

## Known Risks and Mitigations:

Risk: Intake and trial observations involve children's learning information.

Mitigation: Confirm guardian consent before saving a record, collect only necessary data, keep contact details separately, and apply local privacy and retention rules.

Risk: A trial lesson may be mistaken for a definitive assessment or encounter a safety concern.

Mitigation: Have the teacher review observations before sharing them; stop the intake workflow and follow the crisis referral protocol when safety concerns arise.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [Student basic information form](artifact/references/student-basic-info-form.md)
- [Trial lesson observation record](artifact/references/trial-observation-record.md)
- [Formal student profile template](artifact/references/formal-student-profile-template.md)
- [Student workspace schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration]

**Output Format:** [Chinese-language intake guidance, trial-lesson notes, and structured student records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student records require guardian consent; contact details are excluded.]

## Skill Version(s):

2.7.1 (source: release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
