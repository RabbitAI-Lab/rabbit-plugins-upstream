## Description:

Retrieves public Douyin search results, trending topics, creator posts, and video comments through GuaiKei so agents can support social listening, competitor analysis, topic research, and Douyin data analytics.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, analysts, marketers, and developers use this skill to collect structured public Douyin data for content discovery, trend tracking, competitor monitoring, and comment insight workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The GuaiKei API token is sent in URL query parameters.

Mitigation: Use a limited-scope token when possible, avoid running on shared machines, and rotate the token if command lines or network logs may have exposed it.

Risk: Search terms, Douyin URLs, and the API token are sent to GuaiKei.

Mitigation: Use the skill only for topics and URLs suitable for third-party processing, and confirm authorization and data-sharing expectations before use.

Risk: Retrieved Douyin data is automatically saved locally under the skill directory.

Mitigation: Review and delete plaintext log files after use, and avoid sensitive research topics unless local retention is acceptable.

Risk: Public Douyin data can include user nicknames, comments, and other publicly visible personal data.

Mitigation: Anonymize or redact personal identifiers before wider sharing, publication, or commercial reporting.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-comments-guaikei)
- [Server-resolved GitHub provenance](https://github.com/why20261/douyin-comments-guaikei)
- [GuaiKei API token and service site](https://www.guaikei.com)
- [Complete command options](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Hot list response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [Markdown guidance with CLI commands and structured JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Commands write pure JSON to stdout, may save retrieved data under a local logs directory, and require GUAIKEI_API_TOKEN.]

## Skill Version(s):

0.1.0 (source: ClawHub release metadata; artifact metadata also reports 1.0.0 and changelog top entry reports 1.2.2)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
