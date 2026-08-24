## Description:

Retrieves public Douyin search results, hot lists, author posts, and comments for content benchmarking, competitor analysis, topic research, trend tracking, and social-media reporting.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and content operations teams use this skill to retrieve structured public Douyin data for keyword research, author benchmarking, comment analysis, hot-list monitoring, and downstream reports.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, Douyin URLs or IDs, requested limits, and GUAIKEI_API_TOKEN are sent to a third-party API.

Mitigation: Install and run only when data sharing with guaikei.com is acceptable, and protect the API token as a secret.

Risk: The skill automatically saves retrieved social-media datasets locally, including comments and author metadata.

Mitigation: Delete or restrict access to saved log files when they are no longer needed.

Risk: The skill is limited to disclosed, read-only retrieval of public Douyin data.

Mitigation: Use it only for public-data workflows and do not expect private, hidden, login-only, or write-action capabilities.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-authors-for-benchmarking)
- [Guaikei API website](https://www.guaikei.com)
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

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON on stdout with logs and saved result files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; reads public Douyin data through guaikei.com.]

## Skill Version(s):

1.0.0 (source: SKILL.md metadata, package.json, release evidence, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
