## Description:

Collects public Douyin data for keyword search, creator post collection, comment analysis, and realtime trending-topic research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, operations, and research teams use this skill to collect structured public Douyin search results, creator posts, comments, and hot-list data for trend tracking, competitor monitoring, public sentiment review, and reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can trigger too broadly for Douyin-related tasks.

Mitigation: Use it only when the user explicitly needs Douyin public-data research, and ask for clarification when the requested platform or goal is unclear.

Risk: Searches, video URLs, creator IDs, comments, user nicknames or IDs, and IP-region labels may be sent to the API provider.

Mitigation: Confirm the user intends to use guaikei.com for Douyin data collection and avoid sending data outside the requested research scope.

Risk: Collected social data may be stored in local log files.

Mitigation: Protect or delete generated logs according to the user's data-retention needs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-collect-public-data)
- [Guaikei API website](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON command output]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [CLI tools emit JSON to stdout and write task logs locally when data is collected.]

## Skill Version(s):

1.0.0 (source: release evidence, frontmatter metadata, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
