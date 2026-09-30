## Description:

引导中国中小学学生每周探索兴趣，通过面对困难时的反应区分短暂喜好与值得继续探索的兴趣，并在取得同意后记录进展。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students in Chinese middle and upper primary school, junior high, and high school use guided weekly activities to explore interests. With appropriate student and guardian consent, the agent can track interest signals across weeks and prepare progress summaries; without consent, it supports a one-time conversation without retaining records.

### Deployment Geography for Use:

Chinese K–12 context; localize language, consent rules, and crisis referral contacts before use elsewhere.

## Known Risks and Mitigations:

Risk: Long-term interest records about minors may be retained or shared without their informed permission.

Mitigation: Explain retention and sharing before tracking, obtain student and applicable guardian consent, and honor pause, deletion, and sharing controls.

Risk: Consent requirements and crisis referral contacts may not fit users outside the intended Chinese K–12 context.

Mitigation: Localize school-stage assumptions, guardian-consent rules, language, and crisis contacts before deployment elsewhere.

Risk: Brief exploration histories may be mistaken for definitive judgments about a student's interests.

Mitigation: Describe early signals as tentative, avoid definitive conclusions for the eight-week primary-school track, and share parent summaries only with the student's permission.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [Interest exploration record template](artifact/references/interest-exploration-template.md)
- [Grade-band guidance](artifact/shared/grade-bands.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational text and structured interest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional weekly records and milestone summaries require consent; no executable code.]

## Skill Version(s):

2.8.0 (source: ClawHub release and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
