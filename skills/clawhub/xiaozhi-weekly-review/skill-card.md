## Description:

将学生一周的学习记录整理成有依据的周报，并引导学生确定下一周的一个重点。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆中文 K12 学生及陪同使用的家长或教师，整理每周学习进展、薄弱点和下一步行动，并在学生同意后提供家庭分享版。

### Deployment Geography for Use:

中国大陆；在其他地区使用前须本地化课程、同意规则及危机求助资源。

## Known Risks and Mitigations:

Risk: Minors' longitudinal study records and parent-visible reports may reveal sensitive learning or emotional information.

Mitigation: Confirm student and guardian consent settings before long-term storage, cross-skill sharing, reminders, or a family report; honor the student's sharing choices.

Risk: Mainland China curriculum assumptions and emergency contacts may misdirect students elsewhere.

Mitigation: Localize the curriculum, consent rules, and crisis resources before use outside mainland China.

Risk: Broad weekly-review phrases could trigger the skill outside an education context.

Mitigation: Constrain invocation to the intended student learning-review context.

## Reference(s):

- [ClawHub release: 每周学习复盘](https://clawhub.ai/qizhitang/skills/xiaozhi-weekly-review)
- [Weekly review report templates](references/review-report-template.md)
- [Grade-band guidance](shared/grade-bands.md)
- [Crisis referral protocol](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown weekly review or short three-question review; optional consent-gated family report]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [With student consent, may hand off a growth-summary update or weekly reminder request.]

## Skill Version(s):

2.11.2 (source: frontmatter and server release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
