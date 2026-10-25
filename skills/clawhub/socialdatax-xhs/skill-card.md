## Description:

为小红书、XHS 和 RedNote 提供热榜搜索、笔记与评论分析及博主数据查询。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

外部用户可通过 SocialDataX 查询小红书热榜、搜索笔记、查看笔记与评论，并查找博主资料及笔记，用于内容研究和数据分析。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, supplied links, and share text are sent to SocialDataX, and data calls may consume paid credits.

Mitigation: Avoid confidential inputs, confirm paid-credit usage, and review link query parameters before forwarding returned links.

Risk: The SocialDataX API key and CLI dependency require careful handling.

Mitigation: Keep SOCIALDATAX_API_KEY secret and use a reviewed, fixed CLI version rather than an unreviewed latest version.

## Reference(s):

- [SocialDataX API access and key management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)

## Skill Output:

**Output Type(s):** [JSON, API data, Shell commands]

**Output Format:** [Structured JSON results and shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only Xiaohongshu research; requires SOCIALDATAX_API_KEY and calls may consume paid credits.]

## Skill Version(s):

0.1.24 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
