## Description:

作业跟进管家 helps independent teachers register homework, track submission and correction status, classify homework error causes, and turn homework evidence into next-lesson follow-up guidance.

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External independent teachers use this skill to keep homework follow-up records, review completion status, classify mistakes by shared error dimensions, and decide what to address in the next lesson. It is designed for one-on-one and small-group teaching workflows using aliases and teacher-confirmed writeback.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Student homework follow-up records may include information about minors and learning progress.

Mitigation: Install only where teachers are allowed to keep these records, use student aliases, and avoid collecting real names, raw homework answers, original mistake text, or family supervision details.

Risk: Homework conclusions could be shared across skills or become parent-facing output without appropriate consent.

Mitigation: Confirm consent settings before cross-skill sharing or parent-facing output, and keep unconfirmed weak-point evidence in progress records until the teacher explicitly approves writeback.

Risk: AI-generated practice items used for follow-up could contain mistakes.

Mitigation: Run the bundled AI item self-check, label teacher-side generated items as requiring manual verification, and do not add unverified items to a resource bank or send them to students.

Risk: Crisis referral information may be region-specific.

Mitigation: Replace the listed mainland China crisis resources with local emergency contacts when deployed elsewhere, and preserve the crisis-referral escalation flow for immediate safety concerns.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-homework-tracker)
- [作业完成度追踪视图模板](artifact/references/completion-tracking-views.md)
- [错题回流清单模板](artifact/references/error-reflow-checklist-template.md)
- [顽固弱项档案模板](artifact/references/persistent-weakness-file-template.md)
- [下节课预诊断输出模板](artifact/references/pre-diagnosis-output-template.md)
- [学员作业画像模板](artifact/references/student-homework-profile-template.md)
- [全库统一词表](artifact/shared/vocab.md)
- [AI 出题自检协议](artifact/shared/ai-item-check.md)
- [平台能力约定与降级路径](artifact/shared/platform-conventions.md)
- [危机识别与转介协议](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown and structured text reports with workspace field guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Teacher-facing outputs should use aliases, avoid raw homework answers or original mistake text, and mark AI-generated practice items for teacher verification before reuse.]

## Skill Version(s):

2.1.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
