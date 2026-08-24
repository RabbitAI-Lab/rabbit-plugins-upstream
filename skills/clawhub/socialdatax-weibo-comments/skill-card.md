## Description:

用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch Weibo first-level comments and comment replies through SocialDataX, then summarize themes, sentiment, pain points, FAQs, audience feedback, and discussion patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API-key authenticated requests send selected Weibo post and comment identifiers to SocialDataX.

Mitigation: Use a SocialDataX API key intended for this workflow and only analyze posts whose data sharing is acceptable.

Risk: Unbounded pagination or high page counts can increase credit use and data volume.

Mitigation: Prefer bounded --pages or --max-items values, and use --all only after confirming the expected scope and cost.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-comments)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON data from SocialDataX CLI or MCP tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs may include paginated Weibo comments and replies; broad pagination can increase data volume and credit use.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
