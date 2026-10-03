## Description:

帮助独立教师将课后观察整理为结构化教学记录、学习轨迹和下节课衔接建议。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中文 K12 场景的独立教师：课后按学员化名和日期记录知识点掌握情况、课堂事实与教学调整，预览并确认记录和待核对的课时条目，并获得下节课衔接建议。

### Deployment Geography for Use:

Mainland China

## Known Risks and Mitigations:

Risk: Persistent lesson records may expose minors' personal or sensitive information.

Mitigation: Confirm consent settings, use student aliases rather than real names, and let the teacher review each draft before saving.

Risk: Incorrect or unapproved lesson-unit deductions may alter course balances.

Mitigation: Keep lesson-unit entries pending until the teacher explicitly confirms any balance change.

Risk: Parent-facing drafts or crisis advice may disclose sensitive observations or use the wrong local guidance.

Mitigation: Check parent-communication consent, keep summaries internal for teacher review, and localize crisis channels and consent rules outside Mainland China.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-lesson-log)
- [Lesson-log templates](references/lesson-log-template.md)
- [Mastery levels and consent definitions](shared/vocab.md)
- [Crisis response and regional guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Structured lesson-log drafts, learning summaries, pending lesson-unit entries, and next-lesson suggestions in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher approval is required before saving lesson logs or changing lesson-unit balances; parent summaries are internal drafts, not sent messages.]

## Skill Version(s):

2.10.0 (source: skill frontmatter and ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
