## Description:

Retrieves public Douyin search results, rising hot lists, creator posts, and video comments for trend tracking, competitor research, public opinion monitoring, and short-video content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and operations analysts use this skill to query public Douyin data through Node.js commands and turn the JSON results into trend, content, competitor, and comment analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin search targets, creator or video URLs, comment requests, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only when that data transfer is acceptable, keep the token in an environment variable, and rotate the token if it may have been exposed.

Risk: Retrieved results are saved locally by default and may include public usernames, profile identifiers, and comments.

Mitigation: Review or delete generated logs after use, and redact personal identifiers before sharing exported results.

Risk: The skill is intended for public Douyin data and does not support private, hidden, login-only, or write actions.

Mitigation: Limit use to public-data analysis and stop when a request requires private data, login state, posting, liking, commenting, or following.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/douyin-real-hot-rise)
- [Server-Resolved GitHub Source](https://github.com/why20261/douyin-real-hot-rise)
- [GUAIKEI API Service](https://www.guaikei.com)
- [Complete Option Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI Request Schema](assets/search_cli_req.schema.json)
- [Search CLI Response Schema](assets/search_cli_resp.schema.json)
- [Creator Posts Request Schema](assets/post_cli_req.schema.json)
- [Creator Posts Response Schema](assets/post_cli_resp.schema.json)
- [Hot List Response Schema](assets/hot_cli_resp.schema.json)
- [Comment Request Schema](assets/comment_cli_req.schema.json)
- [Comment Response Schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Files, Guidance]

**Output Format:** [JSON command output with optional Markdown summaries and local JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command results are written to stdout and saved under logs by default.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata/package.json report 1.0.0 and changelog top entry reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
