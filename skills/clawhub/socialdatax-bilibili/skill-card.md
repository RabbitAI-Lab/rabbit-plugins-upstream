## Description:

用于 B站数据助手、视频和专栏搜索、内容详情、评论分析、点赞转发观察、UP主资料及视频、专栏和动态列表。覆盖 Bilibili / 哔哩哔哩，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Bilibili videos, articles, comments, reactions, creator profiles, creator content lists, and dynamics through SocialDataX. It can also guide explicit user-requested local video saving.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Bilibili queries, URLs, and SOCIALDATAX_API_KEY are sent to SocialDataX during data calls.

Mitigation: Install and use the skill only when that data sharing is acceptable, and manage SOCIALDATAX_API_KEY as a runtime secret.

Risk: The examples install socialdatax-skills with @latest, which can change over time.

Mitigation: Pin or review the npm package version before use in controlled environments.

Risk: The optional video download command writes media files locally and uses ffmpeg.

Mitigation: Run downloads only after an explicit user request, only for content the user is allowed to save, and choose an appropriate output directory.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)
- [Publisher profile](https://clawhub.ai/user/devinchen2014)
- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON-style command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY at runtime and requires Node.js/npm for the direct CLI examples.]

## Skill Version(s):

0.1.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
