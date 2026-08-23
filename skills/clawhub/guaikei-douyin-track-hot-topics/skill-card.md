## Description:

Collects public Douyin search results, creator posts, video comments, and hot-topic lists through Node.js CLI commands for content research and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Douyin content, monitor competitors and trends, inspect audience comments, and export structured data for content planning or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, target Douyin URLs, and the GUAIKEI token are sent to the guaikei API.

Mitigation: Use the skill only for explicit Douyin research, avoid sensitive inputs, and keep the token in an environment variable with limited access.

Risk: Fetched public data is saved automatically to local JSON logs by default.

Mitigation: Review log retention expectations before use and remove generated logs when the data is no longer needed.

Risk: Broad natural-language triggers could route generic short-video research requests to a third-party API.

Mitigation: Confirm the task is intended for Douyin public-content research before invoking the CLI commands.

Risk: Returned video, author, and comment data may be subject to platform terms or rights restrictions.

Mitigation: Use results for internal analysis unless the user has confirmed that redistribution is permitted.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-track-hot-topics)
- [Guaikei Service Documentation](https://www.guaikei.com)
- [Usage Documentation](readme.md)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search Request Schema](assets/search_cli_req.schema.json)
- [Search Response Schema](assets/search_cli_resp.schema.json)
- [Post Request Schema](assets/post_cli_req.schema.json)
- [Post Response Schema](assets/post_cli_resp.schema.json)
- [Comment Request Schema](assets/comment_cli_req.schema.json)
- [Comment Response Schema](assets/comment_cli_resp.schema.json)
- [Hot Topics Response Schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout, operational messages on stderr, and optional local JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a GUAIKEI_API_TOKEN environment variable and Node.js >= 16.14.0; CLI requests can return up to 10000 public Douyin records per command.]

## Skill Version(s):

1.0.0 (source: server release metadata, artifact frontmatter, package.json, and changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
