## Description:

当用户需要做小红书博主内容研究、账号内容列表、近期发布复盘、内容风格分析、创作者对标或账号追踪时使用。面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

面向品牌、MCN、内容运营和创作者，用于研究小红书创作者的近期内容、复盘发布表现、分析内容风格、进行创作者对标和追踪账号。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Creator account identifiers or profile links are sent to a third-party service, and queries may consume paid credits.

Mitigation: Submit only the account identifier or profile link needed, use explicit page or item limits, and check the service's pricing before expanding a query.

Risk: An API key could be exposed if entered in chat, logs, screenshots, or skill files.

Mitigation: Store a dedicated SocialDataX key in the client's secret settings and never print or share its value.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/devinchen2014/skills/xhs-creator-content-research)
- [SocialDataX API access and key management](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, Markdown, Analysis, Guidance]

**Output Format:** [Markdown summaries and creator post lists with titles or descriptions, publish times, engagement signals, media links, and content analysis.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include paginated results and follow-up research suggestions.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
