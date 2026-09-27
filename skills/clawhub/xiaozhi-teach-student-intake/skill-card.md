## Description:

帮助独立教师在监护人同意后开展诊断式试听，并以最少必要信息建立学员档案。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向独立教师：访谈家长和学生、设计诊断式试听、记录课堂观察，并在确认监护人同意后建立教学档案；试听后的报名跟进仅限这一阶段。

### Deployment Geography for Use:

Mainland China (Chinese-speaking K12); use elsewhere requires localization of consent rules, emergency contacts, curriculum assumptions and language.

## Known Risks and Mitigations:

Risk: A child's learning profile could be stored without valid guardian consent or with unnecessary personal details.

Mitigation: Confirm guardian consent before creating a record; limit fields to teaching needs, omit names and contact details, and honor retention and deletion controls.

Risk: Consent rules, emergency contacts, curriculum and language may not fit use outside Mainland China.

Mitigation: Localize these requirements before use with student data outside Mainland China.

Risk: A single trial lesson may lead to overconfident judgments about a student.

Mitigation: Mark trial observations as insufficient evidence and have the teacher review conclusions before sharing them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)
- [ClawHub publisher profile](https://clawhub.ai/user/qizhitang)
- [Student basic information form](artifact/references/student-basic-info-form.md)
- [Trial observation record](artifact/references/trial-observation-record.md)
- [Formal student profile template](artifact/references/formal-student-profile-template.md)
- [Student workspace schema](artifact/shared/solo-teacher-workspace.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [Teaching drafts and structured student profile entries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-reviewed guidance; profile entries require guardian consent and exclude contact details.]

## Skill Version(s):

2.7.0 (source: frontmatter and ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
