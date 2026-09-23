## Description:

输入关键词、抖音账号主页链接，自动拉取垂类、账号作品并解析无水印下载链接，支持一键批量下载到本地。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketers, analysts, and developers use this skill to collect public Douyin search results, creator posts, hot-list entries, and comments for content research, trend tracking, competitor monitoring, and downstream analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends user-provided Douyin keywords or links and the GUAIKEI_API_TOKEN to www.guaikei.com.

Mitigation: Install and run only when this data transfer is acceptable, keep the token scoped and protected, and avoid submitting sensitive or private inputs.

Risk: Returned public Douyin search, creator, hot-list, and comment data may be retained in logs or local result files.

Mitigation: Treat outputs as retained copies of platform data, delete them when no longer needed, and follow Douyin terms, privacy law, and content redistribution rules.

Risk: The skill is intended for public data and does not support private, hidden, or login-state Douyin content.

Mitigation: Use it only for public-data analysis and stop rather than attempting workarounds when a request requires private or account-authenticated data.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-batch-downloader)
- [Publisher profile](https://clawhub.ai/user/why20261)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [GUAIKEI API token service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes from Node.js CLI commands, with optional human-facing summaries or follow-up guidance from the agent.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may include public Douyin links, author metadata, engagement counts, tags, comments, and error/status fields.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
