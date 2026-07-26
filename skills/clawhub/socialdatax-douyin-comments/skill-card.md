## Description: <br>
用于抖音评论分析、抖音评论回复、抖音评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Douyin comments and comment replies，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch and analyze Douyin first-level comments and replies for audience feedback, sentiment themes, objections, pain points, FAQ extraction, and discussion summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: Douyin content identifiers, URLs or share text, pagination tokens, and the SocialDataX API key are sent to SocialDataX during data calls. <br>
Mitigation: Use the skill only when the user is comfortable sending that data to SocialDataX, and keep the API key in SOCIALDATAX_API_KEY rather than embedding it in prompts or files. <br>
Risk: Large comment threads can increase request volume and cost, especially with --all or --include-replies. <br>
Mitigation: Use --max-items or --pages to bound collection size before fetching large threads. <br>
Risk: Pagination can fail or retrieve the wrong continuation if opaque next_page_token values are modified. <br>
Mitigation: Pass returned next_page_token values back unchanged for the same content item or comment chain. <br>


## Reference(s): <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-douyin-comments) <br>
- [SocialDataX AI access](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and can include paginated Douyin comment and reply data.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
