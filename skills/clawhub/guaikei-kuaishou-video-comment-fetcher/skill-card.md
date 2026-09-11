## Description:

当用户需要做快手竞品研究、快手竞品分析、同赛道观察、内容角度对比、内容策略对比或品牌内容调研时使用。提供关键词获取竞品视频、博主作品、视频评论等功能，面向品牌、MCN、内容运营和创作者。

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content creators, brand marketing teams, MCNs, and data analysts use this skill to retrieve public Kuaishou keyword search results, creator posts, and video comments for competitive research, trend monitoring, KOL review, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou search terms, profile URLs, video URLs, and an API token to the third-party guaikei.com service.

Mitigation: Use it only for queries approved for third-party processing, keep GUAIKEI_API_TOKEN scoped and private, and rotate or revoke the token if exposure is suspected.

Risk: Fetched public-data results are saved locally in logs until deleted.

Mitigation: Review log retention expectations before use and remove generated logs when results are no longer needed.

Risk: The skill is limited to public Kuaishou data and may return empty or error responses for deleted, unavailable, private, or restricted content.

Mitigation: Check the structured status and error_code fields before analysis, and do not treat failed or empty responses as factual findings.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-kuaishou-video-comment-fetcher)
- [Guaikei API Service](https://www.guaikei.com)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON result summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results may be saved locally under logs/.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact metadata, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
