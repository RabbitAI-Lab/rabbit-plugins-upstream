## Description:

抓取微信公众号文章、搜索公众号、文章列表、爆款查询与分析。触发场景：mp.weixin.qq.com 链接、微信公众号文章、公众号文章分析。

This skill is ready for commercial/non-commercial use.

## Publisher:

[one2agi](https://clawhub.ai/user/one2agi)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketers, and developers use this skill to fetch WeChat public-account article text, search accounts and article lists, compare accounts or URLs, and inspect trending engagement data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can use stored WeChat session cookies, which may act like account access.

Mitigation: Use the least-privileged account possible, avoid sharing full browser cookie exports, rotate cookies regularly, and remove cookies from shared logs or repositories.

Risk: Article URLs and search terms may be sent to third-party WeChat-related APIs.

Mitigation: Avoid submitting confidential URLs, private draft content, or sensitive search terms unless the receiving service is approved for that data.

Risk: Bundled or user-provided API keys can be exposed through configuration files or command output.

Mitigation: Replace bundled keys with user-owned credentials, keep secrets out of shared workspaces, and scrub command transcripts before distribution.

Risk: The security evidence says this skill's HTTPS behavior should be reviewed before installation.

Mitigation: Install only after reviewing the network behavior, and prefer unauthenticated or API-key-only modes when they satisfy the task.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/one2agi/skills/wechat-article-grab)
- [Environment variable guide](artifact/env-guide.md)
- [Priority and fallback reference](artifact/references/priority.md)
- [mptext API dashboard](https://wechat.faiz-world.com/dashboard/api)
- [WeChat Official Accounts platform](https://mp.weixin.qq.com/)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, HTML, Shell commands, Configuration guidance]

**Output Format:** [Command-line text output, with optional JSON or HTML trend reports.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May require MPTEXT_API_KEY or WeChat cookie/token depending on the command; some article-fetching and trend commands can return partial content or no match.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
