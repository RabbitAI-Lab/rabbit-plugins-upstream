## Description:

用于小红书数据助手、小红书搜索热榜、小红书数据分析、小红书笔记搜索、笔记详情、评论分析、博主数据和博主笔记。覆盖 Xiaohongshu / XHS / RedNote，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to explore Xiaohongshu trends, find notes, review note details and comments, and look up creator profiles and posts through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send submitted keywords, links, or share text to SocialDataX, and data calls use the SOCIALDATAX_API_KEY.

Mitigation: Submit only content you are comfortable sending to the service and protect the API key in the runtime environment.

Risk: Using the @latest CLI package can change behavior when the package is updated.

Mitigation: Prefer a reviewed, fixed CLI version and limit its access to unrelated files and secrets.

Risk: Large comment or creator-post requests may consume additional credits.

Mitigation: Keep page and reply requests scoped to the amount of data needed, and review credit usage for large requests.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown summaries, JSON service results, and inline Bash CLI examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research; result coverage depends on query limits, pagination, available credits, and service responses.]

## Skill Version(s):

0.1.25 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
