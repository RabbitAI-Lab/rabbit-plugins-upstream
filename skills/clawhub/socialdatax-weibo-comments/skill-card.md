## Description:

用于微博评论分析、微博评论回复、微博评论洞察、用户反馈、口碑分析、痛点总结和内容讨论分析。覆盖 Weibo comments and comment replies，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to retrieve and analyze Weibo first-level comments and comment replies for audience feedback, sentiment themes, objections, pain points, FAQ extraction, and discussion summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill depends on the SocialDataX npm package and API service.

Mitigation: Confirm trust in the SocialDataX package and service before installing or running the skill.

Risk: SOCIALDATAX_API_KEY is required for runtime data calls.

Mitigation: Set the key only in the intended execution environment and avoid embedding it in files or shared outputs.

Risk: Broad comment collection can consume SocialDataX credits.

Mitigation: Prefer --max-items or limited --pages unless broad collection is intentional.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-comments)
- [ClawHub publisher profile](https://clawhub.ai/user/devinchen2014)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-backed analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and may return paginated Weibo comment or reply data.]

## Skill Version(s):

0.1.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
