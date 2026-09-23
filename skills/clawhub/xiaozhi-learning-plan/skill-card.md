## Description:

把学习目标拆成可执行的 30 天或周学习计划，并在学生明确开启后跟进执行偏差、生成家庭看板或入队提醒。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, families, and learning-support agents use this skill in a Simplified Chinese K12 context to turn goals, weak-point summaries, available time, and exam dates into concrete study plans. It supports weekly planning for upper primary students, 30-day plans for middle and high school students, optional family-facing boards, and consent-gated reminder handoff.

### Deployment Geography for Use:

Mainland China by default; localize curriculum assumptions, crisis-contact resources, language defaults, and minor-consent rules before use elsewhere.

## Known Risks and Mitigations:

Risk: Use outside the Mainland China K12 context may produce unsuitable curriculum assumptions, crisis-contact guidance, language defaults, or minor-consent handling.

Mitigation: Localize the curriculum context, crisis resources, language defaults, and consent rules before deploying in another region.

Risk: Profile reads, parent-visible boards, reminders, and plan storage could expose student learning data if enabled too broadly.

Mitigation: Keep each gate independent and off by default; require explicit consent for profile access, parent sharing, reminders, and plan storage.

Risk: Family-facing outputs could over-share sensitive learning or emotional information.

Mitigation: Generate family boards only after checking parent-sharing consent and student veto rights; keep boards limited to tasks and completion facts unless crisis handling applies.

Risk: Crisis or safety signals could be minimized in ordinary planning or family-board flows.

Mitigation: Stop the learning-plan flow when crisis signals appear and follow the bundled crisis exception protocol with localized emergency guidance.

Risk: Generated practice items or plan tasks may be incorrect, too broad, or hard to verify.

Mitigation: Use concrete completion criteria for each task and apply the bundled AI item self-check before presenting generated exercises.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Publisher profile](https://clawhub.ai/user/qizhitang)
- [Plan templates](references/plan-templates.md)
- [Grade bands](shared/grade-bands.md)
- [Consent and vocabulary](shared/vocab.md)
- [Crisis exception](shared/crisis-exception.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [Text, Markdown, Configuration, Guidance]

**Output Format:** [Markdown/text study plans, printable family-board tables, and consent-gated handover payload guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are intended for Simplified Chinese K12 learning workflows; profile reads, parent-visible boards, reminders, and plan storage are optional and require explicit consent.]

## Skill Version(s):

2.2.0 (source: server release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
