## Description:

把独立教师的课后记忆变成结构化教学档案，每节课 5 分钟记完。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to turn after-class notes into structured lesson logs, topic-level mastery records, pending course-unit confirmations, and next-lesson handoff points.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged workspace schema includes parent-communication records that do not fit the skill's stated lesson-log role.

Mitigation: Before installation, confirm the platform enforces field-level permissions so the skill cannot read or write parentCommunicationLogs; keep parentSummary as an internal draft.

Risk: The skill handles persistent student lesson records and learning observations.

Mitigation: Use pseudonyms, clear consent controls, retention limits, and deletion workflows before storing or sharing learner records.

Risk: Course-unit suggestions could affect lesson-package accounting if applied automatically.

Mitigation: Keep all course-unit changes as pending confirmations until the teacher explicitly approves the units to apply.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson log template](artifact/references/lesson-log-template.md)
- [AI item check protocol](artifact/shared/ai-item-check.md)
- [Crisis exception](artifact/shared/crisis-exception.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)
- [Platform conventions](artifact/shared/platform-conventions.md)
- [Solo teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [Vocabulary](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown guidance and structured workspace field updates for lesson logs, parent-summary drafts, and pending course-unit confirmations.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Records and course-unit changes are presented for teacher review and require explicit confirmation before writing.]

## Skill Version(s):

2.1.6 (source: server release and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
