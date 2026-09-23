## Description:

把独立教师的课后记忆整理为结构化教学档案，生成课后五维记录、分知识点掌握度、课时待确认条目和下节课衔接建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent Chinese K12 teachers use this skill after class to convert lesson notes into structured records, learning-trace evidence, pending lesson-unit confirmations, and next-lesson planning cues. It is intended for teacher-reviewed drafts rather than automatic scheduling, homework tracking, parent messaging, or stage reporting.

### Deployment Geography for Use:

China Mainland by default; localize emergency-support wording before use elsewhere.

## Known Risks and Mitigations:

Risk: The skill is designed for a Chinese K12 teacher workflow and includes emergency-support wording that may not fit other regions.

Mitigation: Install it only for the intended workflow unless the operator localizes emergency-support wording and confirms the user's region before giving emergency contacts.

Risk: Lesson records and parent-facing summaries can expose student information if consent or sharing settings are wrong.

Mitigation: Confirm workspace consent fields before use, especially parent communication, emotion sharing, and cross-skill sharing permissions.

Risk: Lesson records, parent summaries, and lesson-unit changes could be treated as final without teacher review.

Mitigation: Keep outputs as teacher-reviewed drafts and require explicit confirmation before writing records, changing lesson-unit ledgers, or using parent summaries.

Risk: The skill may generate a same-type verification item as supporting material for a next lesson.

Mitigation: Run the bundled AI item self-check and mark generated items for human calculation review before adding them to a resource bank or assessment.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Lesson-log template](references/lesson-log-template.md)
- [Platform conventions](shared/platform-conventions.md)
- [Crisis exception protocol](shared/crisis-exception.md)
- [AI item self-check protocol](shared/ai-item-check.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Chinese Markdown guidance and structured workspace field suggestions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher confirmation is required before lesson records or lesson-unit changes are written; parent summaries remain internal drafts.]

## Skill Version(s):

2.2.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
