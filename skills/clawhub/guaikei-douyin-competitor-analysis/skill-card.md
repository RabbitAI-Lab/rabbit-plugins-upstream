## Description:

Use this skill to search Douyin videos, inspect Douyin hot lists, read Douyin comments, collect creator posts, and support Douyin competitor analysis, short-video topic research, public-opinion monitoring, trend tracking, and viral content discovery.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, marketers, content operators, and developers use this skill to retrieve structured public Douyin search, trend, creator-post, and comment data for competitor research, content planning, sentiment review, and trend monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Douyin research queries and URLs are sent to guaikei.com.

Mitigation: Install and run the skill only when that third-party data transfer is acceptable for the user's research scope.

Risk: Full result sets may be saved under the skill's local logs directory and can include competitor research, comment, profile, or other sensitive analysis data.

Mitigation: Treat saved logs as sensitive, restrict access and sharing, and remove or retain them according to the user's data-handling policy.

Risk: Returned media URL fields may be usable for downloads.

Mitigation: Avoid using media URLs for downloading unless the user has the necessary rights and authorization.

## Reference(s):

- [Guaikei API Token and Service](https://www.guaikei.com)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search Request Schema](assets/search_cli_req.schema.json)
- [Search Response Schema](assets/search_cli_resp.schema.json)
- [Post Request Schema](assets/post_cli_req.schema.json)
- [Post Response Schema](assets/post_cli_resp.schema.json)
- [Comment Request Schema](assets/comment_cli_req.schema.json)
- [Comment Response Schema](assets/comment_cli_resp.schema.json)
- [Hot List Response Schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON stdout with optional concise Markdown summaries and local JSON logs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands may save full result sets under a local logs directory.]

## Skill Version(s):

1.0.0 (source: release evidence, frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
