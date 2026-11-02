## Description:

用于 YouTube 数据助手、视频搜索、视频详情、评论分析、频道资料以及频道视频和 Shorts 列表。覆盖 YouTube video and channel research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

内容研究者和社媒分析师可用此技能搜索 YouTube 视频、查看视频详情和评论、检查频道资料，并列出频道视频与 Shorts。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries may consume paid SocialDataX credits.

Mitigation: Check the query scope and available credits before making data calls.

Risk: The API key could be exposed if mishandled.

Mitigation: Keep SOCIALDATAX_API_KEY private and out of prompts, command output, and generated content.

Risk: Using the floating @latest package tag may run CLI code that has not been reviewed.

Mitigation: Prefer a reviewed, pinned CLI version before execution.

## Reference(s):


## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries and text from YouTube research results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research; results depend on SocialDataX availability and API credits.]

## Skill Version(s):

0.1.3 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
