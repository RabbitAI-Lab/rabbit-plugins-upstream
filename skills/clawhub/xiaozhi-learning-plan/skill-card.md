## Description:

为中学生制定可调整的30天学习计划，并为小学高段学生制定每周计划。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in upper primary, middle, and high school use this skill to turn learning goals and, with permission, study-profile summaries into manageable weekly or 30-day schedules. It can help adjust the plan as progress changes and prepare a parent-facing board only with the required consent.

### Deployment Geography for Use:

Mainland China; localize curriculum assumptions, minor-consent requirements, and crisis contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: A student's study-profile details or progress could be shared beyond their intended audience.

Mitigation: Obtain separate explicit consent before reading a profile, generating a parent-facing board, or queuing reminders; respect opt-outs and applicable guardian-consent rules.

Risk: Curriculum, minor-consent, or crisis-support assumptions may not fit deployment outside mainland China.

Mitigation: Localize those requirements and support contacts before deployment in another region.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-learning-plan)
- [Learning plan templates](references/plan-templates.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Consent and reminder guidance](shared/vocab.md)
- [Crisis-response guidance](shared/crisis-exception.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language study schedules, progress summaries, and optional parent-facing learning boards in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Upper primary uses weekly plans; older students may receive 30-day plans. Profile-based personalization, parent-facing boards, and reminders each require separate consent.]

## Skill Version(s):

2.11.0 (source: server release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
