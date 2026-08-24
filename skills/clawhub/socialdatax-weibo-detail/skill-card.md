## Description:

用于微博数据分析、微博帖子详情、帖子数据、互动指标、内容调研和内容分析。覆盖 Weibo post details，来自 SocialDataX 社媒数据助手。

This skill is ready for commercial/non-commercial use.

## Publisher:

[devinchen2014](https://clawhub.ai/user/devinchen2014)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve and summarize structured Weibo post details, including content, author, media, publish time, post URL, and interaction metrics. It supports content research and analysis workflows for a single Weibo post by ID or URL.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill requires SOCIALDATAX_API_KEY for SocialDataX-hosted Weibo data retrieval.

Mitigation: Install and use it only when comfortable providing that API key to SocialDataX-hosted endpoints, and keep the key in the runtime environment rather than in generated files.

Risk: Optional media saving can write files to a local path selected by the user.

Mitigation: Choose output files or directories deliberately and avoid sensitive, shared, or unexpected locations.

Risk: SocialDataX detail access is read-only and does not provide Weibo account actions.

Mitigation: Use returned post details for factual analysis only, and do not treat the skill as capable of login, posting, liking, commenting, or account changes.

## Reference(s):

- [SocialDataX API access](https://socialdatax.com/ai?from=clawhub)
- [ClawHub skill page](https://clawhub.ai/devinchen2014/skills/socialdatax-weibo-detail)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON data interpretation]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The underlying command prints JSON with platform, tool, arguments, and data; the agent may summarize factual Weibo post fields when available.]

## Skill Version(s):

0.1.18 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
