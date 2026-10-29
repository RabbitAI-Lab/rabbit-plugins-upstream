## Description:

用于小红书评论分析、小红书评论回复、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Xiaohongshu / XHS / RedNote comments，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Social media analysts and content teams use the skill to retrieve Xiaohongshu comments and replies, then review audience feedback, sentiment themes, objections, pain points, FAQs, and discussion patterns.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: An exposed SocialDataX API key could allow unintended account use.

Mitigation: Keep SOCIALDATAX_API_KEY in a protected environment variable and out of prompts, generated files, and logs.

Risk: Unbounded comment pagination can consume API credits per page.

Mitigation: Set --pages or --max-items to limit retrieval; consult the SocialDataX documentation for credit behavior.

Risk: The security review covers the supplied skill instructions, not later package releases.

Mitigation: Use a reviewed, fixed package version and review updates before adopting them.

## Reference(s):

- [SocialDataX documentation](https://socialdatax.com/docs)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Guidance]

**Output Format:** [JSON comment data and concise natural-language summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Comment retrieval may span multiple pages; the skill can report page and item counts and pagination state.]

## Skill Version(s):

0.1.20 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
