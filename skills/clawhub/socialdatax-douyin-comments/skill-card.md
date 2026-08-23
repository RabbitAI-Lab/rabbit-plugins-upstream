## Description:

用于抖音评论分析、抖音评论回复、抖音评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Douyin comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and social media teams use this skill to retrieve Douyin first-level comments and replies through SocialDataX, then summarize themes, sentiment signals, objections, pain points, FAQs, and audience discussion patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SOCIALDATAX_API_KEY and installs/runs the SocialDataX npm package.

Mitigation: Confirm trust in the SocialDataX package before installation and provide the API key only through the SOCIALDATAX_API_KEY environment variable.

Risk: Using unbounded retrieval can increase API usage or cost.

Mitigation: Use --max-items for bounded collection when full pagination is unnecessary.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, API Calls, Analysis]

**Output Format:** [Markdown guidance with shell command examples; SocialDataX CLI and tool calls return JSON comment data.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and Node.js/npm; supports pagination, multi-page retrieval, and bounded collection with --max-items.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
