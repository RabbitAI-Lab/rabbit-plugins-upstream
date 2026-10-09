## Description:

按视频 ID 批量查询 TikTok 视频详情，单次最多查询 10 个视频。

This skill is ready for commercial/non-commercial use.

## Publisher:

[autoagc](https://clawhub.ai/user/autoagc)

### License/Terms of Use:

MIT-0

## Use Case:

TikTok 卖家和分析人员使用此技能按视频 ID 查询播放和带货相关的视频详情，并汇总查询结果。

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Installing qhkit or changing PATH introduces third-party software into the environment.

Mitigation: Review and approve installation or PATH changes; prefer managed or pinned installs.

Risk: Video IDs are sent to Qinghu's service and paid calls may consume credits.

Mitigation: Confirm the recipient and estimated credits before calling; obtain user consent and report actual credits charged.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/autoagc/skills/qinghu-tiktok-video-detail)
- [qhkit npm package](https://www.npmjs.com/package/@iqinghu/qhkit)

## Skill Output:

**Output Type(s):** [Text, Markdown, Files]

**Output Format:** [Concise answer with key video metrics; spreadsheet file for 10 or more records]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports Qinghu credits spent on paid queries; up to 10 video IDs per query]

## Skill Version(s):

0.1.0 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
