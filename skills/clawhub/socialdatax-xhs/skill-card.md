## Description:

用于小红书数据助手、小红书搜索热榜、小红书数据分析、小红书笔记搜索、笔记详情、评论分析、博主数据和博主笔记。覆盖 Xiaohongshu / XHS / RedNote，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users use this skill to research Xiaohongshu content, including trending searches, note discovery and details, comment analysis, and creator profiles and posts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Inputs sent to the SocialDataX service may contain information the user does not want to share.

Mitigation: Submit only inputs the user is comfortable sending to the service.

Risk: External CLI code and hosted-service behavior are not verified by the available evidence.

Mitigation: Use a reviewed, fixed CLI version and limit its local access.

Risk: API calls may consume account credits.

Mitigation: Check expected usage and available credits before running large or repeated queries.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-xhs)

## Skill Output:

**Output Type(s):** [Analysis, JSON, Text]

**Output Format:** [Structured Xiaohongshu data with concise research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; API calls may consume credits.]

## Skill Version(s):

0.1.26 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
