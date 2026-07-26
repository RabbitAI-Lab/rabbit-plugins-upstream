## Description: <br>
用于小红书评论分析、小红书用户反馈、小红书需求挖掘、痛点总结、购买顾虑整理、FAQ 提炼、口碑分析、评论回复观察和内容讨论复盘，基于用户提供的小红书笔记链接或完整 note_id 下的评论结果，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
Content operations, product research, brand research, and customer-insight teams use this skill to fetch and analyze Xiaohongshu / XHS / RedNote comments and replies for a user-provided note link or complete note_id. It helps turn returned comments into themes, pain points, purchase objections, FAQs, representative quotes, and actionable recommendations. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill sends the provided Xiaohongshu note, URL, or comment identifiers to SocialDataX using the user's API key. <br>
Mitigation: Confirm the user is comfortable sharing those identifiers with SocialDataX and keep SOCIALDATAX_API_KEY in the runtime environment rather than in skill files. <br>
Risk: Broad pagination, --all, or reply expansion can increase API usage or credit consumption. <br>
Mitigation: Use --max-items or --pages when full collection is not required. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/xhs-comment-insights) <br>
- [SocialDataX AI access page](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON data returned by SocialDataX CLI or MCP tools] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Requires SOCIALDATAX_API_KEY and node/npm; output should state whether comments are a partial sample, multi-page result, or include replies.] <br>

## Skill Version(s): <br>
0.1.3 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
