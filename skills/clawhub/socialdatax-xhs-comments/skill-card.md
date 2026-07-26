## Description: <br>
用于小红书评论分析、小红书评论回复、用户反馈、口碑分析、痛点总结和内容讨论分析，覆盖 Xiaohongshu / XHS / RedNote comments，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, analysts, and agents use this skill to fetch Xiaohongshu / XHS / RedNote comments and replies through SocialDataX, then group observed themes and summarize sentiment, objections, pain points, FAQs, and discussion patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends SOCIALDATAX_API_KEY to SocialDataX tooling at runtime. <br>
Mitigation: Use only API keys intended for SocialDataX, keep the key in the SOCIALDATAX_API_KEY environment variable, and avoid placing credentials in skill files or prompts. <br>
Risk: Using --all or multi-page options may fetch large Xiaohongshu comment sets. <br>
Mitigation: Use page limits or max item limits for exploratory work, and confirm the user is authorized to analyze the content before collecting broad comment sets. <br>
Risk: Comment summaries and sentiment themes may influence business or content decisions. <br>
Mitigation: Base conclusions on observed comment themes, mention whether one page or multiple pages were analyzed, and review outputs before acting on them. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs-comments) <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON tool output] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Read-only SocialDataX requests require SOCIALDATAX_API_KEY; multi-page options can return large JSON comment sets.] <br>

## Skill Version(s): <br>
0.1.15 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
