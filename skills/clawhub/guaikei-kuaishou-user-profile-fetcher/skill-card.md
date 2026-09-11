## Description:

用于快手数据分析、快手视频详情、快手作品数据、互动指标、内容调研和快手内容分析。覆盖 Kuaishou / Kwai，来自GuaiKei社媒数据助手。提供快手关键词搜索、快手博主作品获取、快手视频评论获取等功能。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content creators, marketers, data analysts, and agents use this skill to search public Kuaishou videos by keyword, fetch public creator posts, and retrieve public video comments for analysis, reporting, topic research, competitor monitoring, and trend review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Kuaishou keywords, profile or video identifiers, and query parameters are sent to the third-party guaikei.com API with GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when the user accepts the third-party API flow, scope the token for this service, and avoid submitting confidential topics or private identifiers.

Risk: Fetched results and request metadata are written to local JSON log files, which may contain sensitive searched topics, URLs, comments, or account and video metadata.

Mitigation: Store generated logs in an approved location, restrict access, and delete or redact them when the analysis no longer requires the raw data.

Risk: The skill is designed for public Kuaishou data and does not support private, hidden, login-only, or unauthorized content.

Mitigation: Reject requests for non-public data and use returned status and error_code fields instead of inventing or filling missing results.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-user-profile-fetcher)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [GuaiKei API service](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; command execution returns structured JSON and writes local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; outputs include status, error_code, request metadata, skill metadata, and result arrays or null.]

## Skill Version(s):

1.0.0 (source: server release metadata, package.json, frontmatter, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
