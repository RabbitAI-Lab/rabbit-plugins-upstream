## Description:

用于微博数据分析、微博热搜、微博内容研究、关键词观察、内容调研、竞品分析和趋势研究。覆盖 Weibo hot-search and post research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External researchers, analysts, and content teams can inspect Weibo hot searches and search posts by keyword to study content, competitors, and trends.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms are sent to SocialDataX, and requests may consume paid credits.

Mitigation: Use the skill only for the intended research source and keep queries focused; check account billing before making paid requests.

Risk: The API key must remain private, and the supplied assessment does not audit the downloaded package.

Mitigation: Keep SOCIALDATAX_API_KEY in the runtime environment and consider using a reviewed, pinned package version instead of @latest.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-search)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown]

**Output Format:** [Concise text or Markdown summaries of Weibo hot-search and keyword-search results, with relevant post details and links when useful.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Separates observed ranking or post details from interpretation; search results may be paginated.]

## Skill Version(s):

0.1.21 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
