## Description:

把独立教师的课后记忆变成结构化教学档案，每节课 5 分钟记完。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

独立教师可用本技能将课后观察整理为学习记录、知识点掌握情况和下节课衔接建议，并预览确认后保存。它也可生成待确认的课时条目及仅供教师审阅的家长事实摘要草稿。

### Deployment Geography for Use:

China

## Known Risks and Mitigations:

Risk: Lesson records may contain sensitive information about students, including minors.

Mitigation: Use learner aliases, avoid real names and family details, obtain required consent, honor retention limits, and delete records deliberately when requested or expired.

Risk: A workspace schema alone does not enforce consent, save confirmation, or lesson-credit controls.

Mitigation: Ensure the platform enforces consent and confirmation controls; review each lesson record and credit deduction before saving.

Risk: A parent-facing summary could be mistaken for an approved message or shared prematurely.

Mitigation: Keep summaries as internal drafts, check the required authorization, and let the teacher review and decide whether and when to send them.

Risk: Brief classroom observations could be turned into unsupported judgments about a student's traits.

Mitigation: Record observable behavior and mastery evidence only; have the teacher review summaries before use.

## Reference(s):

- [ClawHub release page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson log template](artifact/references/lesson-log-template.md)
- [Solo teacher workspace schema](artifact/shared/solo-teacher-workspace.schema.json)
- [Vocabulary and consent fields](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Guidance]

**Output Format:** [Markdown previews and structured JSON workspace records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses learner aliases; lesson records and credit entries require teacher review and confirmation before saving. Parent summaries remain private drafts.]

## Skill Version(s):

2.12.0 (source: frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
