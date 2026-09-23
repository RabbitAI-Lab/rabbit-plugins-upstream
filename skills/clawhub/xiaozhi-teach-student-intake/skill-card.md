## Description:

把试听从"体验课"变成一次双向诊断，并按最小化原则给新学员建档。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language K12 tutors use this skill to run trial lesson intake, confirm guardian consent, collect only the minimum student information needed for teaching, diagnose learning needs, and create an initial student profile. It covers the trial-to-enrollment intake window and routes scheduling, lesson logs, renewals, and retention work to other skills.

### Deployment Geography for Use:

China mainland by default; localize policy assumptions, curriculum framing, consent requirements, and crisis resources before use elsewhere.

## Known Risks and Mitigations:

Risk: The workflow handles minor student learning profiles and trial lesson observations.

Mitigation: Confirm guardian consent before creating records, use pseudonyms, and avoid real names, contact details, school/class, addresses, birth dates, and emergency contacts.

Risk: The skill is designed for Chinese-language mainland China K12 tutoring assumptions.

Mitigation: Localize consent rules, curriculum expectations, policy assumptions, and crisis resources before using it in another region or language.

Risk: Trial observations or follow-up drafts could be mistaken for final judgments or direct parent communication.

Mitigation: Require teacher review, mark single-session observations as insufficient sample, avoid score guarantees, and do not send messages on the teacher's behalf.

Risk: A learner may disclose self-harm, abuse, severe distress, bullying, or another issue outside the learning workflow.

Mitigation: Stop the intake flow and follow the crisis referral protocol, recording only that a referral occurred.

## Reference(s):

- [学生基本信息表](references/student-basic-info-form.md)
- [需求访谈 5W 提问清单](references/needs-interview-5w-checklist.md)
- [需求画像卡模板](references/needs-profile-card.md)
- [学情诊断卡模板](references/diagnosis-card-template.md)
- [试讲课 5 段结构模板](references/trial-lesson-5-segment-structure.md)
- [试听记录模板](references/trial-observation-record.md)
- [试听后转化期跟进节奏与话术](references/followup-scripts-trial-conversion.md)
- [正式学员档案模板](references/formal-student-profile-template.md)
- [平台能力约定与降级路径](shared/platform-conventions.md)
- [危机转介协议](shared/crisis-referral-protocol.md)
- [独立教师工作空间 schema](shared/solo-teacher-workspace.schema.json)
- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-student-intake)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown guidance, scripted teacher-facing text, and JSON-compatible workspace records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Creates or updates pseudonymous student profile, course package, and progress evidence records only after guardian consent; does not store contact details or send messages.]

## Skill Version(s):

2.2.0 (source: evidence.json release and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
