## Description:

This skill helps agents retrieve and analyze public Douyin content, including keyword search results, hot-list terms, creator posts, and video or image-post comments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, brand researchers, creators, and agents use this skill to gather structured public Douyin data for topic research, trend tracking, competitor monitoring, comment analysis, and downstream reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, target URLs, limits, and GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Install and run it only when that third-party API use is acceptable; keep the token in a local environment variable and rotate it if exposed.

Risk: Saved results can include public comments, nicknames, user IDs, profile identifiers, content metadata, and IP-region labels.

Mitigation: Review, redact, or delete generated logs before sharing results outside the intended personal or team analysis context.

Risk: The scanner verdict is suspicious because the skill handles an API token and stores scraped public-data results.

Mitigation: Review the security summary and guidance before installation, and verify that the intended use complies with applicable platform, privacy, and data-sharing requirements.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-data-scraper)
- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-data-scraper)
- [Douyin data API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search input schema](assets/search_cli_req.schema.json)
- [Search output schema](assets/search_cli_resp.schema.json)
- [Creator posts input schema](assets/post_cli_req.schema.json)
- [Creator posts output schema](assets/post_cli_resp.schema.json)
- [Hot list output schema](assets/hot_cli_resp.schema.json)
- [Comments input schema](assets/comment_cli_req.schema.json)
- [Comments output schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands, Files, Guidance]

**Output Format:** [Structured JSON from Node.js CLI commands, with optional concise text summaries and JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; command logs may be saved under a logs directory.]

## Skill Version(s):

0.1.0 (source: server release metadata and release changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
