## Description: <br>
用于快手评论分析、快手评论回复、快手评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Kuaishou / Kwai comments and comment replies，来自 SocialDataX 社媒数据助手。 <br>

This skill is ready for commercial/non-commercial use. <br>

## Publisher: <br>
[devinchen2014](https://clawhub.ai/user/devinchen2014) <br>

### License/Terms of Use: <br>
MIT-0 <br>


## Use Case: <br>
External users and developers use this skill to fetch Kuaishou first-level comments and replies through SocialDataX, then organize audience feedback into themes, sentiment, objections, pain points, FAQ topics, and discussion summaries. <br>

### Deployment Geography for Use: <br>
Global <br>

## Known Risks and Mitigations: <br>
Risk: The skill requires a SocialDataX API key for data calls. <br>
Mitigation: Keep SOCIALDATAX_API_KEY in the environment and do not place API keys in skill files, prompts, or command examples. <br>
Risk: Large pagination options such as --all, --pages, and --include-replies can consume API credits. <br>
Mitigation: Review pagination settings before running commands and prefer --max-items or limited page counts when exploring a new content item. <br>
Risk: Submitting private or unrelated Kuaishou links may expose data outside the intended analysis task. <br>
Mitigation: Use only content links, photo IDs, and comment IDs that are relevant to the user's requested analysis. <br>


## Reference(s): <br>
- [SocialDataX AI API access](https://socialdatax.com/ai?from=clawhub) <br>


## Skill Output: <br>
**Output Type(s):** [text, markdown, shell commands, configuration, guidance] <br>
**Output Format:** [Markdown guidance with CLI commands and JSON response interpretation] <br>
**Output Parameters:** [1D] <br>
**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY from the user's environment and can return paginated JSON comment and reply data.] <br>

## Skill Version(s): <br>
0.1.16 (source: ClawHub server release metadata) <br>

## Ethical Considerations: <br>
Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment. <br>
