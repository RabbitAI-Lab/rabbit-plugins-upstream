## Description:

This skill helps agents collect public Douyin search results, creator posts, video comments, and hot-trend data as structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to gather public Douyin content, creator, comment, and hot-list data for content research, competitor analysis, public-opinion review, and trend tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, account or video URLs, request limits, and GUAIKEI_API_TOKEN are sent to GuaiKei.

Mitigation: Use only terms and URLs appropriate for third-party processing, keep the token in an environment variable, and rotate the token if exposure is suspected.

Risk: Collected public comments and account data may be stored automatically in local JSON logs.

Mitigation: Review and delete stored logs when they are no longer needed, avoid sensitive internal research terms, and limit retention to the minimum needed for the task.

Risk: Large-scale collection of public Douyin data can create platform-terms or privacy compliance risk.

Mitigation: Confirm collection is limited to public data and complies with applicable platform terms, privacy rules, and internal review requirements before use.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-data-intake-to-json)
- [README](readme.md)
- [Complete options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search input schema](assets/search_cli_req.schema.json)
- [Search output schema](assets/search_cli_resp.schema.json)
- [Post input schema](assets/post_cli_req.schema.json)
- [Post output schema](assets/post_cli_resp.schema.json)
- [Comment input schema](assets/comment_cli_req.schema.json)
- [Comment output schema](assets/comment_cli_resp.schema.json)
- [Hot-list output schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON on stdout, operational logs on stderr, and timestamped JSON log files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command outputs follow the JSON schemas in assets/.]

## Skill Version(s):

1.0.0 (source: package.json, changelog, release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
