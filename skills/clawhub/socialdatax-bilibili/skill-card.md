## Description:

用于 B站数据助手、视频和专栏搜索、内容详情、评论分析、点赞转发观察、UP主资料及视频、专栏和动态列表，并支持按需下载视频到本地。覆盖 Bilibili / 哔哩哔哩，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, creators, and analysts use this skill to search Bilibili videos and articles, inspect content and discussion, review creator activity, and save a video locally when explicitly requested.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and supplied links are sent to SocialDataX and may consume paid credits.

Mitigation: Send only the information needed for the lookup and check the account's credit or billing status when usage may incur charges.

Risk: Direct CLI use depends on an API key and a third-party package.

Mitigation: Use a scoped secret store, keep keys out of chat and version control, and prefer a reviewed fixed CLI version.

Risk: Optional downloads write video media to local storage.

Mitigation: Download only when requested and choose the destination explicitly.

## Reference(s):

- [SocialDataX](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)

## Skill Output:

**Output Type(s):** [Text, Analysis, Files, Configuration instructions]

**Output Format:** [Text summaries and structured lookup results; optional local video file]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Online lookups send the required queries, content IDs, URLs, or share text to SocialDataX and may consume paid credits. Optional downloads save media to a user-selected local path.]

## Skill Version(s):

0.1.8 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
