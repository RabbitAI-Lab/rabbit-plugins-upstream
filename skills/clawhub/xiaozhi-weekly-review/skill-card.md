## Description:

帮助学生根据一周的学习记录生成有证据的复盘报告，并选定下周的一个行动重点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

学生用它整理每周学习记录、回顾知识掌握和薄弱点，并制定下周的重点。经学生授权后，可生成家庭分享版、保存成长摘要或安排复盘提醒。

### Deployment Geography for Use:

Global; localize crisis contacts, school-grade assumptions and minors' consent requirements outside mainland China.

## Known Risks and Mitigations:

Risk: Weekly reviews may use persistent student profiles or reminder queues without suitable platform controls.

Mitigation: Before installation, confirm consent controls and handoff recipients; require the student's current consent before sharing, saving summaries or queuing reminders.

Risk: Mainland China crisis contacts and student-data assumptions may be unsuitable elsewhere.

Mitigation: Localize crisis-support guidance and minor-consent requirements for the deployment region before use.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Review report templates](references/review-report-template.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language weekly review in Markdown, with an optional family-sharing summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May offer a short three-question review for younger students; reminders and profile updates require consent.]

## Skill Version(s):

2.9.0 (source: server release and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
