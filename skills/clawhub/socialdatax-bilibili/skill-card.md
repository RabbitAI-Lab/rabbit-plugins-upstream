## Description:

用于 B站数据助手、视频和专栏搜索、内容详情、评论分析、点赞转发观察、UP主资料及视频、专栏和动态列表。覆盖 Bilibili / 哔哩哔哩，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, and developers use this skill to research Bilibili videos, articles, comments, reactions, creator profiles, creator posts, and video download links through SocialDataX-backed commands.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill claims read-only behavior, but the video download command can write local files.

Mitigation: Treat the skill as capable of local file output; use the download command only when explicitly needed and choose a controlled output directory.

Risk: Runtime data calls depend on SOCIALDATAX_API_KEY and Node/npm execution.

Mitigation: Install only in environments where npm execution is allowed and provide the API key through the environment rather than storing it in skill files.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-bilibili)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured command output when tools are run.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js, npm, and SOCIALDATAX_API_KEY for runtime data calls.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
