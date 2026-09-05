## Description:

把一周零散的学习记录整理成有结论、有证据、有下一步的周报，并带学生做一次自我复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External students and learning-support agents use this skill to turn weekly study activity into an evidence-based review with a focused next step. It also supports consent-gated family sharing and handoff summaries for related learning components.

### Deployment Geography for Use:

China mainland by default for K12 content, Simplified Chinese language, and safety-channel assumptions; localize before deployment elsewhere.

## Known Risks and Mitigations:

Risk: Profile writebacks and reminders may carry more student data than needed or route reminder data to the wrong component.

Mitigation: Require explicit consent checks before profile writes and reminders, narrow allowed profile fields, and route reminder_enqueue data only to the intended reminder component.

Risk: Family-facing reports may expose student information without the correct consent state.

Mitigation: Confirm the speaker, check parentSharingConsent before family sharing, check emotionSharingWithParent before emotion content, and honor the student's veto.

Risk: Crisis signals involving a student could be softened into routine study-summary language.

Mitigation: Stop weekly-report generation on crisis signals, follow the bundled crisis referral protocol, and record only the referral handling fact.

Risk: Low cross-session memory or statistics support may lead to unsupported progress claims.

Mitigation: Use the documented degradation path: avoid unsupported historical numbers, label sparse data clearly, and limit output to current-session review when memory is unavailable.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [review-report-template.md](artifact/references/review-report-template.md)
- [grade-bands.md](artifact/shared/grade-bands.md)
- [vocab.md](artifact/shared/vocab.md)
- [crisis-exception.md](artifact/shared/crisis-exception.md)
- [crisis-referral-protocol.md](artifact/shared/crisis-referral-protocol.md)
- [handover-protocol.schema.json](artifact/shared/handover-protocol.schema.json)
- [platform-conventions.md](artifact/shared/platform-conventions.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Configuration]

**Output Format:** [Markdown or plain text weekly review, with structured handoff payloads when reminders or profile updates are requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are student-facing by default; family-facing content requires the documented consent checks and student veto handling.]

## Skill Version(s):

2.1.6 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
