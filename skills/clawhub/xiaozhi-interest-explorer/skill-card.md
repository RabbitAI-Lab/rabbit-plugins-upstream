## Description:

通过每周一次的引导式探索，帮助学生观察自己面对困难时的反应，区分短暂喜好与值得继续探索的兴趣。

This skill is ready for commercial/non-commercial use.

## Publisher:

[qizhitang](https://clawhub.ai/user/qizhitang)

### License/Terms of Use:

MIT-0

## Use Case:

面向中国大陆小学中高段至高中学生的兴趣探索对话；在获得相应同意后，可跨周记录探索经历，并生成阶段性兴趣回顾。小学低段不适用，也不提供升学或职业规划建议。

### Deployment Geography for Use:

Mainland China; localize child-data consent and crisis support before use elsewhere

## Known Risks and Mitigations:

Risk: Long-term records about minors could be retained or shared without valid consent.

Mitigation: Confirm the host implements student and applicable guardian consent, record deletion and export, and separate permissions for parent access and cross-skill sharing before enabling tracking.

Risk: Reminders or parent summaries could reach others without the student's authorization.

Mitigation: Keep reminders and parent summaries off by default; enable each only through its explicit consent flow and limit summaries to facts the student agrees to share.

Risk: Mainland-China age rules and crisis contacts may not fit another region.

Mitigation: Localize consent requirements and crisis referrals for the deployment region before use with students outside mainland China.

## Reference(s):

- [ClawHub 技能页面](https://clawhub.ai/qizhitang/skills/xiaozhi-interest-explorer)
- [兴趣探索记录模板](references/interest-exploration-template.md)
- [平台适用地域与能力约定](shared/platform-conventions.md)
- [危机转介协议](shared/crisis-referral-protocol.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Chinese-language conversational text and structured interest summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Optional weekly interest records and milestone reports; persistence, parent summaries, sharing and reminders require the relevant consents and host-platform support.]

## Skill Version(s):

2.7.0 (source: ClawHub release metadata and skill frontmatter)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
