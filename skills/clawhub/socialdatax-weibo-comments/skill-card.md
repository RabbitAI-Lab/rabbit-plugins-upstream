## Description: <br>
用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users, developers, and analysts use this skill to retrieve Weibo post comments and comment replies through SocialDataX, then summarize audience feedback, sentiment themes, objections, pain points, FAQs, and discussion patterns. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill calls SocialDataX with the user's SOCIALDATAX_API_KEY and can consume API credits. <br>
Mitigation: Confirm the key belongs to the intended SocialDataX account before use, and prefer --max-items or --pages when cost or volume needs to be bounded. <br>
Risk: Using --all or --include-replies can retrieve many comments or replies and increase API usage. <br>
Mitigation: Start with one page or a low --max-items value, then expand pagination only when the extra coverage is needed. <br>
Risk: Pagination tokens are opaque and changing them can cause failed or inconsistent retrieval. <br>
Mitigation: Pass returned next_page_token values back unchanged for the same Weibo post or comment chain. <br>


## Reference(s): <br>
- [SocialDataX AI API access](https://socialdatax.com/ai?from=clawhub) <br>
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-comments) <br>


## Skill Output: <br>
**Output Type(s):** [Text, Markdown, Shell commands, API Calls, Guidance] <br>
**Output Format:** [Markdown guidance with inline shell commands and JSON API results] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [May include paginated Weibo comment data, merged item counts, next-page tokens, and user-facing analysis grouped by observed themes.] <br>

## Skill Version(s): <br>
0.1.16 (source: server release evidence) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
