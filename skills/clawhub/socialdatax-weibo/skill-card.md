## Description:

用于微博数据助手、微博热搜、微博内容研究、帖子详情、评论分析、评论回复观察、转赞互动、创作者资料和创作者内容列表。覆盖 Weibo post research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

People researching Weibo trends, posts, comments, engagement, or creator accounts can use this skill to retrieve relevant platform data and review it. It supports hot searches, post and comment details, comment replies, likers, reposts, creator profiles, and creator post lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The instructions run an unpinned `@latest` CLI package, creating a supply chain risk; scanner coverage is partial because some local references could not be resolved.

Mitigation: Prefer a reviewed, fixed package version if available. Avoid entering credentials or sharing sensitive search terms and post text until comfortable with the package and its data handling.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo)

## Skill Output:

**Output Type(s):** [API Calls, Analysis, Guidance]

**Output Format:** [Structured data (JSON) with concise text summaries or guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on available SocialDataX access and the requested data scope.]

## Skill Version(s):

0.1.23 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
