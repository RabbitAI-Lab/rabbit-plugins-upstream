## Description:

将一周的学习记录整理成有证据、有结论和下一步行动的中文周报，并引导学生自我复盘。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Chinese-speaking students in mainland China use this skill to review their weekly K-12 learning progress and choose one priority for the next week. With the student's consent, it can prepare a family-facing summary or hand off a growth summary and review reminder.

### Deployment Geography for Use:

Mainland China (Chinese-language K-12 contexts)

## Known Risks and Mitigations:

Risk: Sharing learning records, emotional observations, or reminders without the student's intended consent.

Mitigation: Check the student's current consent and privacy settings before family sharing, cross-skill handoffs, memory writeback, or reminder enrollment; honor opt-outs.

Risk: Applying mainland China curriculum, crisis resources, or consent assumptions in another locale.

Mitigation: Localize crisis resources, curriculum assumptions, consent rules, and privacy controls before use in another region or language.

Risk: Overstating progress or producing misleading statistics from incomplete learning records.

Mitigation: Identify data gaps, avoid unsupported counts and trends, and use a lighter student-led review when records are insufficient.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report templates](artifact/references/review-report-template.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)
- [Consent and reminder conventions](artifact/shared/vocab.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language weekly review in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Student-facing report by default; family-facing summary only with student consent. Limited data is identified rather than presented as certain.]

## Skill Version(s):

2.8.0 (source: ClawHub release metadata and SKILL.md frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
