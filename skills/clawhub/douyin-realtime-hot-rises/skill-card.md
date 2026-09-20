## Description:

抖音热点上升榜帮助内容创作者、运营、电商和营销团队查询抖音热榜、关键词内容、博主公开作品和视频评论，并把结果整理为可用于选题、竞品监控和趋势分析的结构化数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content creators, social media operators, ecommerce teams, marketers, and analysts use this skill to inspect public Douyin trends, keyword results, creator posts, and comments before planning content or comparing competitors. It is most useful when the user provides a Douyin keyword, public creator URL, public video URL, or asks for the current hot list.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Full search, post, and comment results are saved to local plaintext logs by default.

Mitigation: Inspect or delete the generated logs directory regularly, avoid collecting more public profile or comment data than needed, and account for local retention before using the skill on sensitive workflows.

Risk: Douyin query data and URLs are sent to guaikei.com using the configured API token.

Mitigation: Use the skill only when sharing those queries and URLs with the API provider is acceptable, and protect GUAIKEI_API_TOKEN as a credential.

## Reference(s):

- [Server-resolved source repository](https://github.com/why20261/douyin-realtime-hot-rises)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-realtime-hot-rises)
- [GUAIKEI API provider](https://www.guaikei.com)
- [完整选项参数说明](references/options.md)
- [更新日志](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with Node.js command examples and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14+ and GUAIKEI_API_TOKEN; full search, post, and comment results are saved to local plaintext logs by default.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
