## Description:

Helps agents research public Douyin content by running Node.js commands for keyword search, creator post collection, video comment retrieval, and real-time hotlist queries.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and operations teams use this skill to gather structured public Douyin data for content research, competitor monitoring, comment analysis, trend tracking, and follow-on reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Douyin research inputs and the GUAIKEI_API_TOKEN to guaikei.com.

Mitigation: Use only when that third-party API use is acceptable, and keep the token out of shared logs, repositories, and transcripts.

Risk: Fetched social-media data is automatically stored locally as logs.

Mitigation: Treat generated logs as retained social-media data, store them in approved locations, and delete them when no longer needed.

Risk: Returned media URL fields may enable access beyond analysis even though the skill does not support downloads.

Mitigation: Use returned URLs only for the stated research workflow and avoid redistributing media or data outside authorized analysis.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-content-research)
- [Guaikei API site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post request schema](assets/post_cli_req.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Hotlist response schema](assets/hot_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON command outputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; command stdout is structured JSON while logs are written separately.]

## Skill Version(s):

1.0.0 (source: server release evidence, package.json, changelog, and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
