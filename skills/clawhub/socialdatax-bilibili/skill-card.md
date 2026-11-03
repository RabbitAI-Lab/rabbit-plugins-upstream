## Description:

用于 B站数据助手、视频和专栏搜索、内容详情、评论分析、点赞转发观察、UP主资料及视频、专栏和动态列表。覆盖 Bilibili / 哔哩哔哩，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Bilibili users and researchers can search videos and articles, inspect content and comments, review reactions, and explore creator profiles and posts. Video downloads are available only when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Lookup inputs and usage attribution are sent to SocialDataX, and external npm code and service data handling were not verified by this artifact review.

Mitigation: Avoid sensitive share text and private URL parameters; use a reviewed, fixed CLI version with limited local permissions.

Risk: API credentials could be exposed through unsupported storage or a committed settings file.

Mitigation: Store the key using supported secret storage and exclude credential settings files from version control.

## Reference(s):

- [SocialDataX API access and management](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Structured Bilibili data with concise text or Markdown summaries; optional downloaded video files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only research results; video files are saved locally only when explicitly requested and to a user-selected path.]

## Skill Version(s):

0.1.6 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
