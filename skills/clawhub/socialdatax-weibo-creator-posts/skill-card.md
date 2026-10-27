## Description:

用于微博创作者数据、微博创作者内容列表、近期发布、内容调研和创作者内容分析。覆盖 Weibo creator posts，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can retrieve Weibo creator posts by user ID or profile URL, review recent publishing, and analyze content or creator activity. The skill can summarize returned post details such as content, publish time, media, and interaction counts when available.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Large or unbounded post retrieval can increase SocialDataX service charges.

Mitigation: Use a dedicated SocialDataX API key and set page or item limits appropriate to the task.

Risk: The documented commands execute the latest package release with the agent's permissions.

Mitigation: Prefer a reviewed, fixed package version before execution.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-creator-posts)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis]

**Output Format:** [JSON creator-post data with concise natural-language summaries, optionally in Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Available post fields vary and may include IDs, content, media, publish time, interaction counts, and author facts.]

## Skill Version(s):

0.1.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
