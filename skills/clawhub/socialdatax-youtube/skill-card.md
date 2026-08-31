## Description:

用于 YouTube 数据助手、视频搜索、视频详情、评论分析、频道资料以及频道视频和 Shorts 列表。覆盖 YouTube video and channel research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to fetch public YouTube search results, video details, comments, replies, channel profiles, and channel video or Shorts lists through SocialDataX.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill runs an npm CLI package fetched externally at runtime.

Mitigation: Install only when the package source is trusted and the environment permits Node.js, npm or npx, and network execution.

Risk: The skill requires SOCIALDATAX_API_KEY for YouTube data lookups.

Mitigation: Keep the API key in the user environment, avoid embedding it in skill files, and confirm the key belongs to the intended SocialDataX account.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-youtube)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown with inline shell commands and returned YouTube data summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm or npx, network access to the SocialDataX npm package at runtime, and SOCIALDATAX_API_KEY in the environment.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
