## Description:

用于 TikTok 数据助手、视频和图文搜索、帖子详情、评论分析、创作者资料和创作者帖子列表。覆盖 TikTok content and creator research，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research TikTok videos, image posts, comments, replies, creator profiles, and creator post lists through SocialDataX. It is suited for agents that can run the SocialDataX CLI or use the matching MCP tools with a user-provided API key.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SOCIALDATAX_API_KEY to be available to the SocialDataX CLI or MCP service.

Mitigation: Install and run it only when the user intends to use SocialDataX, and keep the API key scoped to the runtime environment that needs it.

Risk: The documented npx @latest commands can execute newer package code after this release.

Mitigation: Review package behavior before use in controlled environments, and pin an approved package version when reproducibility or change control is required.

Risk: Multi-page searches and all creator-post retrieval can consume SocialDataX API credits.

Mitigation: Start with narrow queries or limited pages, and use all-post retrieval only when the expected credit usage is acceptable.

## Reference(s):

- [SocialDataX API access and homepage](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-tiktok)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and tool names]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses SOCIALDATAX_API_KEY, Node.js, npm, and SocialDataX CLI or MCP tools for read-only TikTok data retrieval.]

## Skill Version(s):

0.1.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
