## Description:

为中国大陆中小学学习场景分派学习请求、避免重复协作，并在用户同意后汇总学习月报。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

Students, parents, and educators use this skill to route learning questions to related study skills, prevent duplicate follow-up, and request a five-part monthly learning summary with appropriate consent.

### Deployment Geography for Use:

Mainland China; curriculum, consent rules, and crisis contacts require localization elsewhere.

## Known Risks and Mitigations:

Risk: Learning summaries or emotion information about minors could be shared with other skills, parents, or teachers without appropriate permission.

Mitigation: Check the relevant consent and sharing settings before each handoff or report; share only the minimum needed and honor requests to pause or withhold sharing.

Risk: Reminder scheduling or monthly reporting could proceed without the user's agreement.

Mitigation: Request agreement before generating a monthly report, and queue reminders only with reminder consent; do not claim that this skill sends them.

Risk: China-specific learning assumptions and crisis contacts may be inappropriate outside Mainland China.

Mitigation: Review local curriculum, minor-consent requirements, and crisis resources before deploying elsewhere; confirm location before giving region-specific emergency contacts.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/qizhitang/skills/xiaozhi-skill-coordinator)
- [One-week multi-skill coordination example](references/one-week-linkage-record.md)

## Skill Output:

**Output Type(s):** [Guidance, Text, Markdown, Configuration]

**Output Format:** [Conversational text and structured monthly reports; consented handoff records when supported]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Routes requests rather than teaching or sending reminders directly; reports cover only authorized, available records.]

## Skill Version(s):

2.9.0 (source: skill frontmatter and server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
