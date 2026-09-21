## Description:

Collects public Douyin creator, video, trend, keyword search, and comment data as structured JSON for content research, competitor monitoring, social listening, and operations analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Developers, analysts, and content operations teams use this skill to query public Douyin search results, hot lists, creator posts, and comments, then feed the returned JSON into downstream analysis, summaries, reports, or tables.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can collect large public Douyin datasets and saves generated results locally, which may include usernames, comments, profile links, and IP-region labels.

Mitigation: Collect only data the user is allowed to process, choose the smallest useful limit, restrict access to generated logs, and delete logs when they are no longer needed.

Risk: GUAIKEI_API_TOKEN is required for API access and exposure could allow unauthorized use of the account or quota.

Mitigation: Store the token only in a local environment or secret manager, avoid sharing terminal sessions that reveal configuration, and rotate the token if exposure is suspected.

Risk: Requests and retrieved data are sent through guaikei.com, so usage may involve third-party data processing.

Mitigation: Confirm that the user has authorization for the requested collection and that third-party processing is acceptable before running the skill.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/why20261/skills/douyin-kol-crawler)
- [Publisher Profile](https://clawhub.ai/user/why20261)
- [Server-Resolved Source Repository](https://github.com/why20261/douyin-kol-crawler)
- [Guaikei API Website](https://www.guaikei.com)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search Request Schema](assets/search_cli_req.schema.json)
- [Search Response Schema](assets/search_cli_resp.schema.json)
- [Creator Posts Request Schema](assets/post_cli_req.schema.json)
- [Creator Posts Response Schema](assets/post_cli_resp.schema.json)
- [Hot List Response Schema](assets/hot_cli_resp.schema.json)
- [Comment Request Schema](assets/comment_cli_req.schema.json)
- [Comment Response Schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; successful tool calls return structured JSON and may write JSON log files.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; supports keyword, URL, sec_uid, aweme_id, sorting, filtering, and limit parameters.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
