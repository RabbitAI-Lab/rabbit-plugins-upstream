## Description:

帮助用户围绕小红书、抖音和快手开展社媒内容日历研究、选题规划、发布时间观察、内容主题分组与平台节奏对比。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向外部用户及社媒运营人员，研究小红书、抖音和快手的热点与内容样本，并整理选题日历、平台节奏比较和可执行的内容建议。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Running an unpinned npm release while granting it access to a SocialDataX API key can expose that credential to unreviewed package changes.

Mitigation: Use a pinned, reviewed package version when available, and run it only when you are comfortable granting access to SOCIALDATAX_API_KEY.

Risk: Generated tokenized URLs or pagination tokens could expose sensitive query or access context if shared too broadly.

Mitigation: Avoid sharing tokenized URLs or pagination tokens outside the conversation or tools that need them.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-content-calendar-research)
- [SocialDataX AI](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis]

**Output Format:** [Markdown summaries and research tables]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include platform, source, time-range, and pagination-scope details for research results.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
