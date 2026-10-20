## Description:

用于微博数据分析、微博热搜、微博内容研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Weibo hot-search and post research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and content teams use the skill to review Weibo hot-search topics and search posts by keyword for content, competitor, and trend research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search queries and usage attribution are sent to SocialDataX using the configured API key and may consume credits.

Mitigation: Keep searches within the intended scope and budget, protect the API key, and use a reviewed, pinned package version with only necessary credentials and local access.

Risk: The artifact content describes TikTok rather than the Weibo release identified by server evidence, so its examples may target the wrong platform.

Mitigation: Confirm the artifact and its commands match the intended Weibo release before execution.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Markdown, Shell commands]

**Output Format:** [JSON research results and concise Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research outputs; queries and usage attribution may be sent to SocialDataX and consume credits.]

## Skill Version(s):

0.1.20

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
