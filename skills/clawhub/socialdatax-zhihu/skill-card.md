## Description:

用于知乎数据助手、知乎热榜、内容搜索、回答文章视频详情、评论分析、创作者资料和文章列表。覆盖 Zhihu content research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and content analysts use this skill to review Zhihu hot lists, search and inspect content, analyze comments, and look up creator profiles and article lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Submitted queries and share text are processed by SocialDataX and could contain private information.

Mitigation: Avoid including private information in queries or share text.

Risk: Unbounded pagination or package updates can affect API credit use and runtime behavior.

Mitigation: Use a reviewed fixed CLI version and set pagination limits.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-zhihu)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Text, JSON, Markdown]

**Output Format:** [Structured Zhihu research data and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; API access uses the user's SOCIALDATAX_API_KEY.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
