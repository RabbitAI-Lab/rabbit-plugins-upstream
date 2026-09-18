## Description:

抖音作品实时搜索 helps agents query public Douyin content, trends, creator posts, and comments through command-line tools that return structured JSON for analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, developers, and business analysts use this skill to collect public Douyin search results, hot-list items, creator posts, and comment data for content research, competitor monitoring, social listening, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin queries, links, IDs, and the GUAIKEI_API_TOKEN are sent to guaikei.com.

Mitigation: Install and run the skill only when that third-party data flow is acceptable for the user's organization and use case.

Risk: Local result logs may include public usernames, comments, profile IDs, links, and IP-region labels.

Mitigation: Review, protect, and delete local logs as needed, especially before sharing workspaces or publishing analysis.

## Reference(s):

- [Server-resolved GitHub source repository](https://github.com/why20261/douyin-realtime-searchs)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-realtime-searchs)
- [Douyin data API token provider](https://www.guaikei.com)
- [Complete option reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON CLI outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI tools write pure JSON to stdout and may save retrieved public Douyin results to local logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
