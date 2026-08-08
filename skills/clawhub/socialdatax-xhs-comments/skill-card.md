## Description:

用于小红书评论分析、小红书评论回复、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Xiaohongshu / XHS / RedNote comments，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social media operators use this skill to retrieve Xiaohongshu / XHS / RedNote comments and replies through SocialDataX, then summarize feedback, sentiment themes, objections, pain points, FAQs, and discussion patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Xiaohongshu note URLs or IDs to SocialDataX for comment retrieval.

Mitigation: Use it only when sharing those note identifiers with SocialDataX is acceptable for the intended workflow.

Risk: Using --all or broad multi-page fetching may consume SocialDataX API credits.

Mitigation: Set a page or item limit when exploring data, and avoid repeated retries on insufficient-balance errors.

Risk: The skill requires a SOCIALDATAX_API_KEY at runtime.

Mitigation: Provide the key through the environment and avoid embedding it in prompts, files, or shared logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Shell commands, API calls, Configuration, Guidance, Markdown]

**Output Format:** [Markdown guidance with shell command examples and JSON API output descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY and can fetch one page, multiple pages, all available pages, or a caller-specified maximum item count.]

## Skill Version(s):

0.1.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
