## Description:

Retrieves public Douyin search results, creator posts, comments, and hot-list data as structured JSON for short-video operations analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Marketing, content operations, and data analysis teams use this skill to retrieve public Douyin search, creator post, comment, and hot-list data for topic research, competitor monitoring, sentiment review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords and links are sent to the third-party API at www.guaikei.com.

Mitigation: Use only authorized public-data queries, avoid sensitive monitoring terms on shared machines, and keep GUAIKEI_API_TOKEN private.

Risk: Fetched search, creator-post, and comment results may be saved locally under the skill logs directory.

Mitigation: Run the skill in a trusted workspace and review, retain, or delete logs according to internal data-handling policy.

Risk: The skill is intended for public Douyin data and internal analysis, not private, hidden, or login-state data.

Mitigation: Do not use it for private-data collection or write actions such as posting, liking, commenting, or following.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/douyin-yunying-zhushou)
- [Publisher Profile](https://clawhub.ai/user/why20261)
- [抖音运营技能官网](https://www.guaikei.com)
- [Options Reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Search Request Schema](artifact/assets/search_cli_req.schema.json)
- [Search Response Schema](artifact/assets/search_cli_resp.schema.json)
- [Post Request Schema](artifact/assets/post_cli_req.schema.json)
- [Post Response Schema](artifact/assets/post_cli_resp.schema.json)
- [Comment Request Schema](artifact/assets/comment_cli_req.schema.json)
- [Comment Response Schema](artifact/assets/comment_cli_resp.schema.json)
- [Hot List Response Schema](artifact/assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Guidance]

**Output Format:** [Structured JSON envelopes plus concise Markdown guidance.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; search, post, and comment commands may save fetched results under the skill logs directory.]

## Skill Version(s):

1.3.0 (source: server release metadata, skill metadata, package.json, changelog released 2026-09-17)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
