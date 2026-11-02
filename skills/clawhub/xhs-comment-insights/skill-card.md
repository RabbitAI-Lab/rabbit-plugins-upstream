## Description:

当用户需要做小红书评论分析、小红书评论洞察、小红书用户反馈分析、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察或内容讨论复盘时使用。基于用户提供的小红书笔记链接或 note_id 下的评论结果，面向内容运营、产品调研、品牌调研和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容运营、产品调研、品牌调研者和创作者可用它整理用户选定的小红书笔记评论与回复，归纳主题、痛点、购买顾虑、未满足需求和 FAQ，并形成可执行建议。结论仅反映已获取的评论和回复范围。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Post identifiers, links, or share text supplied for analysis are sent to SocialDataX.

Mitigation: Provide only the minimum necessary post identifier or link.

Risk: Retrieving many pages or comments may consume paid API credits.

Mitigation: Set page or item limits and expand retrieval only when needed.

Risk: A package update can change behavior or dependencies.

Mitigation: Prefer a reviewed, fixed CLI version over @latest and expose only the credentials needed for the task.

## Reference(s):

- [SocialDataX API key information](https://socialdatax.com/ai?from=clawhub)
- [SocialDataX billing](https://socialdatax.com/dashboard/billing)

## Skill Output:

**Output Type(s):** [Analysis, Text, Markdown, JSON]

**Output Format:** [Markdown analysis and recommendations; JSON comment and reply results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Findings are scoped to the comments and replies returned for the user-selected post.]

## Skill Version(s):

0.1.9 (source: server-resolved ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
