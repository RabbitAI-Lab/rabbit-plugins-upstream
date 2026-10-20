## Description:

用于 YouTube 数据助手、视频搜索、视频详情、评论分析、频道资料以及频道视频和 Shorts 列表。覆盖 YouTube video and channel research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and developers can use an agent to search YouTube videos and retrieve video details, comments and replies, channel profiles, and channel video or Shorts lists.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and YouTube URLs are sent to SocialDataX, and API use may incur charges.

Mitigation: Keep confidential information out of queries and confirm applicable API charges before use.

Risk: The SocialDataX API key could be exposed if mishandled.

Mitigation: Keep the key in the designated environment variable and out of prompts, source files, and logs.

Risk: This artifact review does not certify future downloaded package releases.

Mitigation: Prefer a reviewed fixed CLI version rather than an unpinned latest release.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill release](https://clawhub.ai/devinchen2014/skills/socialdatax-youtube)

## Skill Output:

**Output Type(s):** [Text, Analysis]

**Output Format:** [Structured YouTube research results and summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only retrieval; output depends on the selected video, comment, or channel query.]

## Skill Version(s):

0.1.2 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
