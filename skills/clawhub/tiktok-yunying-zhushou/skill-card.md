## Description:

Provides command-line access to public TikTok keyword search results, creator posts, and video comments, returning structured JSON for content research, competitor monitoring, trend discovery, and comment analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

External users, content operators, marketers, and developers use this skill to retrieve and analyze public TikTok videos, creator posts, and comment data without logging into a TikTok account. It supports short-video topic research, influencer and competitor tracking, social listening, and structured reporting workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries, target TikTok URLs or IDs, and the GUAIKEI_API_TOKEN are sent to www.guaikei.com.

Mitigation: Install and run the skill only when the user accepts this third-party API data flow, and keep the token in the GUAIKEI_API_TOKEN environment variable rather than prompts, files, or shared logs.

Risk: Returned public profile and comment data may be saved in local temporary logs.

Mitigation: Review local retention practices, remove unneeded temp logs, and de-identify user-facing exports when using the data externally or commercially.

Risk: Public TikTok data can include user nicknames, comments, and engagement metrics.

Mitigation: Use the data for analysis with appropriate privacy review and confirm platform, regional, and customer obligations before publishing or commercializing derived reports.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-yunying-zhushou)
- [GUAIKEI service site](https://www.guaikei.com)
- [Command options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search input schema](assets/search_cli_req.schema.json)
- [Search output schema](assets/search_cli_resp.schema.json)
- [Creator posts input schema](assets/post_cli_req.schema.json)
- [Creator posts output schema](assets/post_cli_resp.schema.json)
- [Video comments input schema](assets/comment_cli_req.schema.json)
- [Video comments output schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON envelope with status, error code, message, request metadata, results, and warnings.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0 or newer and a GUAIKEI_API_TOKEN environment variable; stdout is reserved for machine-readable JSON while logs and errors are written to stderr.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
