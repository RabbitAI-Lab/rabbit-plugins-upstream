## Description:

Exports public Douyin search results, author posts, video comments, and hot-trend data as structured JSON through Node.js CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill for Douyin content research, competitor monitoring, comment analysis, hot-topic tracking, and structured public-data export from publicly available data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, author URLs, or video URLs to a third-party Guaikei API using GUAIKEI_API_TOKEN.

Mitigation: Use the skill only when that data sharing is acceptable, store GUAIKEI_API_TOKEN as a protected environment secret, and rotate or revoke the token if exposure is suspected.

Risk: Exported public data, including comments or account-related fields, may be retained in local JSON log files.

Mitigation: Collect only the data needed for the task, avoid redistributing exported data in violation of applicable rules, and delete local logs when they are no longer required.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-author-posts-to-feed-export)
- [README](readme.md)
- [Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI Request Schema](assets/search_cli_req.schema.json)
- [Search CLI Response Schema](assets/search_cli_resp.schema.json)
- [Post CLI Request Schema](assets/post_cli_req.schema.json)
- [Post CLI Response Schema](assets/post_cli_resp.schema.json)
- [Comment CLI Request Schema](assets/comment_cli_req.schema.json)
- [Comment CLI Response Schema](assets/comment_cli_resp.schema.json)
- [Hot CLI Response Schema](assets/hot_cli_resp.schema.json)
- [Guaikei API Token Site](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Configuration]

**Output Format:** [JSON on stdout with local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI_API_TOKEN environment variable; stderr is used for logs and prompts.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
