## Description:

用于 B站数据助手、视频和专栏搜索、内容详情、评论分析、点赞转发观察、UP主资料及视频、专栏和动态列表。覆盖 Bilibili / 哔哩哔哩，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and content researchers use this agent to search and analyze Bilibili videos, articles, comments, reactions, creator profiles, and dynamics. It can save a video locally only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API requests use a hosted service and may consume paid credits; exposed credentials could be misused.

Mitigation: Keep SOCIALDATAX_API_KEY private and monitor usage through the official service.

Risk: Using an unreviewed or moving CLI package version may introduce unexpected software changes.

Mitigation: Prefer a reviewed and pinned CLI version.

Risk: An optional video download writes files to the local filesystem.

Mitigation: Download only when requested and choose the destination folder explicitly.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)

## Skill Output:

**Output Type(s):** [JSON data, Analysis, Files]

**Output Format:** [Pretty-printed JSON for research results; video files for explicitly requested downloads]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Downloads are written to the user-selected local output directory.]

## Skill Version(s):

0.1.4 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
