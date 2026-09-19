## Description:

Fetches public Douyin trend, search, creator-post, and comment data through Node.js CLI commands so agents can support content planning, competitor monitoring, social listening, and trend analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External creators, marketers, analysts, and agent developers use this skill to query public Douyin content, hot lists, creator posts, and comments for trend discovery, content ideation, competitor monitoring, and social listening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the API token, search terms, profile links, video links, and returned public datasets to a third-party API provider.

Mitigation: Use only when the publisher and guaikei.com are trusted, configure a revocable token with limited quota, and avoid submitting sensitive or regulated analysis inputs.

Risk: Collected video and comment data may be saved locally in the generated logs directory.

Mitigation: Periodically delete generated logs and avoid retaining public user data longer than needed for the analysis task.

Risk: Public Douyin results can include nicknames, comments, links, and interaction data that may be inappropriate to redistribute unchanged.

Mitigation: De-identify or aggregate user-facing reports and confirm authorization before commercial reuse or public distribution of collected data.

Risk: The security verdict requires review before installation.

Mitigation: Review the skill before installing and prefer official support channels over the personal contact listed in the artifact text.

## Reference(s):

- [Server-resolved GitHub repository](https://github.com/why20261/douyin-trend-insights-v1)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-trend-insights-v1)
- [Douyin data API provider](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, text, markdown, shell commands, configuration, guidance]

**Output Format:** [JSON results with optional Markdown summaries and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js >=16.14.0 and GUAIKEI_API_TOKEN; command logs may be saved locally under logs/.]

## Skill Version(s):

0.1.0 (source: server release metadata; artifact metadata reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
