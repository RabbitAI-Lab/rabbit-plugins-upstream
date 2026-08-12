## Description:

当用户需要做小红书评论分析、小红书评论洞察、小红书用户反馈分析、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察或内容讨论复盘时使用。基于用户提供的小红书笔记链接或 note_id 下的评论结果，面向内容运营、产品调研、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Content operations, product research, brand research, and creator teams use this skill to retrieve Xiaohongshu comment data from user-provided note links or note IDs, then summarize themes, pain points, objections, FAQs, and actionable opportunities.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a SocialDataX API key to retrieve Xiaohongshu comments.

Mitigation: Set SOCIALDATAX_API_KEY only for the intended account and provide only the note links or IDs that should be analyzed.

Risk: Unbounded collection can retrieve more comment pages than intended.

Mitigation: Use page limits or max-item limits instead of --all when the analysis should stay within a bounded sample.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights)
- [SocialDataX API key and product page](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [Shell commands, Markdown, Guidance]

**Output Format:** [Markdown analysis with optional shell commands and JSON retrieval results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses returned comments and replies as evidence; page limits can bound collection scope.]

## Skill Version(s):

0.1.6 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
