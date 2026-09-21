## Description:

Fetches public Douyin videos, hot keywords, creator posts, and comments through GuaiKei APIs for trend tracking, competitor monitoring, topic research, and social listening.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and marketing operators use this skill to query public Douyin search results, real-time hot lists, creator post lists, and video comments, then use the returned structured data for content planning, competitor analysis, public-opinion review, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, profile or video URLs, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install only when this third-party API use is acceptable, keep the token in local environment variables, avoid exposing terminal output, and rotate the token if exposure is suspected.

Risk: Fetched public user, post, and comment data may be saved to plaintext local logs.

Mitigation: Treat logs as potentially sensitive, exclude the logs directory from sharing, backups, and commits, and delete old logs when they are no longer needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-daily-hot-keywords)
- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-daily-hot-keywords)
- [GuaiKei API website](https://www.guaikei.com)
- [Options reference](artifact/references/options.md)
- [Changelog](artifact/references/changelog.md)
- [Search request schema](artifact/assets/search_cli_req.schema.json)
- [Search response schema](artifact/assets/search_cli_resp.schema.json)
- [Post request schema](artifact/assets/post_cli_req.schema.json)
- [Post response schema](artifact/assets/post_cli_resp.schema.json)
- [Hot list response schema](artifact/assets/hot_cli_resp.schema.json)
- [Comment request schema](artifact/assets/comment_cli_req.schema.json)
- [Comment response schema](artifact/assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON output from the invoked CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI tools write JSON to stdout and may save fetched Douyin data to local plaintext logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
