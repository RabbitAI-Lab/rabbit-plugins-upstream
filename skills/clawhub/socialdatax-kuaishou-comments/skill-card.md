## Description:

用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch Kuaishou first-level comments and replies through SocialDataX, then summarize themes, sentiment, objections, pain points, FAQs, and audience feedback from the returned comment data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill may use SOCIALDATAX_API_KEY and run npx to fetch the SocialDataX CLI package at runtime.

Mitigation: Confirm the runtime environment is allowed to execute npm/npx commands and that the API key is scoped for the intended SocialDataX account before use.

Risk: Using --all can create unbounded request size or cost exposure when paginating comments or replies.

Mitigation: Use --max-items or a bounded --pages value unless the user explicitly approves collecting all available pages.

## Reference(s):

- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-kuaishou-comments)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API/CLI result descriptions]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May describe paginated SocialDataX comment results, including page counts, item counts, and next-page tokens.]

## Skill Version(s):

0.1.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
