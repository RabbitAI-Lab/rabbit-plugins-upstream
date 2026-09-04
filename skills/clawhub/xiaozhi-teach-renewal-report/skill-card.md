## Description:

用学员真实的学习记录生成阶段报告、进展对比、下阶段计划和续课沟通草稿，让续课建议基于可核对的事实而不是销售话术。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

External Chinese-language independent teachers use this skill to turn existing lesson logs, homework follow-ups, progress evidence, course-package records, and consent fields into parent-ready stage reports and renewal conversation drafts. The skill is intended for teacher-reviewed output and does not send messages on the teacher's behalf.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may read sensitive student learning records while preparing reports.

Mitigation: Use it only after the teacher explicitly selects the student, keep reports based on recorded evidence, use aliases, and omit real names, contact details, family information, and unsupported percentages.

Risk: Parent-facing output can expose student progress or classroom-status information without proper consent.

Mitigation: Confirm parentCommunicationAllowed before generating a parent-facing report and confirm emotionSharingWithParent before including classroom status or emotional content.

Risk: Renewal guidance could pressure families or overstate educational outcomes.

Mitigation: Keep renewal recommendations tied to the documented 50% and 70% course-package checkpoints, avoid urgency tactics, and do not promise score gains, rankings, or admissions outcomes.

Risk: Record changes or deletion requests may be under-scoped if handled outside platform governance.

Mitigation: Constrain student status changes, report evidence writeback, and deletion requests to the platform's governed record-management process.

Risk: Included crisis hotline wording is locale-specific and may not be suitable outside Mainland China.

Mitigation: Do not rely on the listed hotline wording outside Mainland China without checking local emergency and mental-health support guidance.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-teach-renewal-report)
- [qizhitang publisher profile](https://clawhub.ai/user/qizhitang)
- [Stage report templates](artifact/references/stage-report-templates.md)
- [Renewal communication scripts](artifact/references/renewal-communication-scripts.md)
- [Crisis referral protocol](artifact/shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [text, markdown, guidance]

**Output Format:** [Chinese-language Markdown and structured text drafts]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Produces teacher-reviewed report sections, renewal suggestions, communication scripts, and consent-aware safety guidance; it does not directly send messages.]

## Skill Version(s):

2.1.0 (source: server-resolved release evidence and frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
