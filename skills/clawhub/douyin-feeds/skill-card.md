## Description:

抖音信息源 helps agents retrieve public Douyin search results, trending topics, creator posts, and video or image-post comments as structured data for content research, competitor tracking, social listening, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and analysts use this skill to collect public Douyin content, hot-list, creator-post, and comment data for short-video topic selection, marketing analysis, competitor monitoring, public-opinion review, and daily reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Use a limited and rotatable token, confirm the data-sharing arrangement is acceptable, and avoid using sensitive query terms or private links.

Risk: Successful searches, creator lookups, and comment pulls may be saved as plaintext JSON logs in the skill directory.

Mitigation: Keep the workspace private, restrict access to generated logs, and delete or sanitize logs when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-feeds)
- [Server-resolved source repository](https://github.com/why20261/douyin-feeds)
- [Server-resolved source commit](https://github.com/why20261/douyin-feeds/tree/c6e77e53a42b740bb0fbef401d8c928167668b7b)
- [抖音信息源完整选项参数说明](references/options.md)
- [抖音信息源更新日志](references/changelog.md)
- [抖音数据 API website](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON command output with concise Markdown guidance when an agent summarizes or routes results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command stdout is JSON and operational logs are written separately.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata reports 1.0.0 and changelog top entry reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
