## Description:

Fetches public Douyin search, creator-post, comment, and hot-list data as structured JSON for content research, competitor analysis, public sentiment review, and trend tracking.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and content operations teams use this skill to gather public Douyin data for short-video topic research, competitor monitoring, comment analysis, and trend tracking. It is not intended for publishing, editing, downloading, or collecting private platform data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin keywords, URLs, and GUAIKEI_API_TOKEN are sent to guaikei.com during use.

Mitigation: Install and run the skill only when that data transfer is acceptable, keep the token in an environment variable, and avoid submitting sensitive or ambiguous searches.

Risk: Fetched public comments, profile identifiers, and other public data may be saved locally under logs by default.

Mitigation: Review generated log files after each run, restrict local access to the workspace, and delete logs that contain personal public data when they are no longer needed.

Risk: The security review reports broad activation rules and documentation/runtime mismatches.

Mitigation: Use the skill only for explicit Douyin public-data research tasks and review command parameters, generated output, and error behavior before relying on results.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-public-data-pipeline)
- [Complete Options](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI Input Schema](assets/search_cli_req.schema.json)
- [Search CLI Output Schema](assets/search_cli_resp.schema.json)
- [Post CLI Output Schema](assets/post_cli_resp.schema.json)
- [Comment CLI Output Schema](assets/comment_cli_resp.schema.json)
- [Hot List CLI Output Schema](assets/hot_cli_resp.schema.json)
- [Guaikei Token and Usage Help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, shell commands, configuration, guidance]

**Output Format:** [Structured JSON on stdout, optional JSON log files, and concise command guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14 or newer and a GUAIKEI_API_TOKEN environment variable; commands may save fetched public data under logs by default.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
