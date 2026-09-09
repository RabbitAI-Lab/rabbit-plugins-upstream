## Description:

快手(Kuaishou)公开数据检索与竞品分析｜当用户要“搜索快手视频/抓取博主作品/拉取视频评论”时使用，输出结构化数据，用于爆款选题、竞品监控、KOL 筛选、评论舆情与趋势洞察。Kuaishou public data, search videos, list creator posts, fetch comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT

## Use Case:

External content creators, marketing teams, data analysts, and agent developers use this skill to retrieve public Kuaishou search results, creator posts, and video comments for topic research, competitor monitoring, KOL screening, comment analysis, and trend reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Kuaishou keywords, video URLs, profile URLs, and GUAIKEI_API_TOKEN to the third-party guaikei.com API.

Mitigation: Confirm that this data sharing is acceptable before installation or use, and protect the GUAIKEI_API_TOKEN as a credential.

Risk: The skill saves retrieved public comments, URLs, and related result data to local log files.

Mitigation: Review or delete local logs when collected comments, URLs, or analysis targets are sensitive to the workflow.

Risk: The skill is intended for public Kuaishou data and does not support private, hidden, or login-only content.

Mitigation: Use it only for public data collection and avoid requests for private, hidden, or unauthorized data.

## Reference(s):

- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Guaikei API Service](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON CLI results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Successful runs print JSON with status, request metadata, execution metadata, and results; result JSON is also written under logs/.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog released 2026-08-29)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
