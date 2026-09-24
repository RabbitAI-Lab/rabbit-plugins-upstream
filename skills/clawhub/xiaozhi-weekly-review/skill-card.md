## Description:

每周学习复盘把一周零散学习记录整理成有证据、有下一步的周报，并引导学生完成周维度自我复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, guardians, and learning-support agents use this skill to turn weekly Chinese K12 study activity into a concise student review, optional consent-gated family summary, and next-week focus plan.

### Deployment Geography for Use:

China-oriented K12 deployments; other regions require localization of curriculum assumptions, consent rules, and crisis-referral contacts before student-facing use.

## Known Risks and Mitigations:

Risk: Student learning summaries may expose personal study data if shared too broadly.

Mitigation: Use the skill only with its consent checks enabled: family summaries require parent-sharing consent, emotion content requires separate student consent, and users can view, correct, delete, pause, export, or limit sharing of weekly review data.

Risk: Reminders and profile writebacks can create unwanted retention or follow-up if consent is stale.

Mitigation: Keep reminder and writeback actions consent-gated, send them only through the declared handoff protocol, and have the receiving skill re-check consent before acting.

Risk: Crisis signals could be softened or hidden inside a normal family summary.

Mitigation: Apply the bundled crisis exception before ordinary reporting: stop the review flow, avoid diagnosis or minimizing language, contact trusted adults, and localize emergency guidance by region.

Risk: The skill can overstate trends when weekly history or cross-session statistics are unavailable.

Mitigation: When memory or statistics are unavailable, limit the review to current-session evidence, avoid precise historical numbers, and mark conclusions as data-limited.

Risk: Use during an active exam or restricted assessment may support cheating.

Mitigation: If the student says an exam or timed assessment is in progress, do not provide hints or answers; defer support until after the assessment.

Risk: Non-China deployments may use mismatched curriculum, consent expectations, or crisis contacts.

Mitigation: Localize curriculum assumptions, guardian-consent rules, reminder policies, and crisis-referral contacts before deploying outside the intended Chinese K12 context.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report template](references/review-report-template.md)
- [Grade bands and reminder windows](shared/grade-bands.md)
- [Consent, confidence, and reminder vocabulary](shared/vocab.md)
- [Crisis exception](shared/crisis-exception.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)
- [Platform conventions and degradation paths](shared/platform-conventions.md)
- [AI-generated item self-check protocol](shared/ai-item-check.md)
- [Handover protocol schema](shared/handover-protocol.schema.json)
- [Published handover protocol schema](https://xiaozhi-skills.openclaw.dev/schemas/handover-protocol.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, configuration, guidance]

**Output Format:** [Markdown weekly review reports plus structured handoff snippets for consent-gated writebacks and reminders.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs are weekly-scoped, evidence-based, grade-band aware, and adapted for student-only or consent-gated family sharing.]

## Skill Version(s):

2.3.0 (source: server release evidence and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
