## Description:

Provides Douyin public-data search and analytics for hot rankings, keyword content search, author post tracking, and comment insights through GuaiKei API-backed Node.js CLI commands.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, and developers use this skill to retrieve public Douyin keyword results, hot rankings, author posts, and video comments for content research, competitor monitoring, public-opinion analysis, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin keywords, target URLs or IDs, and the GuaiKei API token to guaikei.com, and security evidence notes the token is placed in request URLs.

Mitigation: Confirm authorization to use the API before execution, keep the token out of shared terminals and logs, and rotate it if exposure is suspected.

Risk: Retrieved public Douyin data is automatically saved locally and may include usernames, profile IDs, comments, URLs, and research targets.

Mitigation: Review or delete the local logs directory after use and redact personal identifiers before sharing analysis or reports.

Risk: The skill is limited to public Douyin data and does not establish redistribution rights for retrieved content.

Mitigation: Use outputs for authorized internal analysis unless separate rights and privacy review permit broader use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-search-guaikei)
- [Server-resolved GitHub repository](https://github.com/why20261/douyin-search-guaikei)
- [GuaiKei API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI request schema](assets/search_cli_req.schema.json)
- [Search CLI response schema](assets/search_cli_resp.schema.json)
- [Author posts response schema](assets/post_cli_resp.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot ranking response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [json, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with executable Node.js commands and structured JSON CLI output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN; CLI stdout is JSON-oriented and retrieved data may also be saved as local JSON logs.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact files also list 1.0.0 metadata and 1.2.2 changelog/runtime constants)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
