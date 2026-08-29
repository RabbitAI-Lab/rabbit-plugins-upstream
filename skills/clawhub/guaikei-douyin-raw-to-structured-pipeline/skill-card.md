## Description:

Provides command-line access to Douyin public data for keyword search, creator post retrieval, video or note comment retrieval, and real-time hot list queries, with structured JSON output for analysis workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, operators, content teams, and analysts use this skill to retrieve structured public Douyin search results, creator posts, comments, and hot-list entries for topic research, competitor monitoring, trend tracking, and public opinion analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin search terms, links, and the GUAIKEI_API_TOKEN are sent to the third-party guaikei.com API.

Mitigation: Use the skill only when that data sharing is acceptable, keep the token out of transcripts and shared logs, and rotate it if exposure is suspected.

Risk: Fetched public results may be written to local logs and could contain sensitive business research or personal data from public comments.

Mitigation: Review retention needs, restrict access to the skill directory, and clean up local logs when results are sensitive.

Risk: The skill is intended for public Douyin data and does not support private, restricted, or login-only content.

Mitigation: Do not use it for private or restricted content, and stop rather than retrying against authentication or authorization failures.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-raw-to-structured-pipeline)
- [Publisher profile](https://clawhub.ai/user/engheng-art)
- [Guaikei Douyin data service](https://www.guaikei.com)
- [README](readme.md)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search input schema](assets/search_cli_req.schema.json)
- [Search output schema](assets/search_cli_resp.schema.json)
- [Creator posts input schema](assets/post_cli_req.schema.json)
- [Creator posts output schema](assets/post_cli_resp.schema.json)
- [Comments input schema](assets/comment_cli_req.schema.json)
- [Comments output schema](assets/comment_cli_resp.schema.json)
- [Hot list output schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON from CLI tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI tools write pure JSON to stdout, logs to stderr, and may save fetched public results in a local logs directory.]

## Skill Version(s):

1.0.0 (source: server release metadata, skill metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
