## Description:

Provides Node.js CLI commands for searching public Douyin content, fetching creator posts and comments, and retrieving real-time hot lists as structured JSON for content research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[engheng-art](https://clawhub.ai/user/engheng-art)

### License/Terms of Use:

MIT-0

## Use Case:

External content strategists, marketers, and analysts use this skill to collect public Douyin search results, creator posts, comments, and hot-list data for topic planning, competitor research, and sentiment review.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad content-planning prompts can trigger Douyin data collection even when the user did not explicitly name Douyin.

Mitigation: Confirm that the user wants Douyin research before running the skill on ambiguous content-planning requests.

Risk: Douyin research prompts and targets are sent to guaikei.com with the configured API token.

Mitigation: Use only approved tokens, avoid sensitive research targets, and tell users before submitting queries to the third-party service.

Risk: Full API results are retained in local log files.

Mitigation: Review and delete logs that contain sensitive research, and avoid redistributing collected public data beyond allowed internal use.

## Reference(s):

- [ClawHub Skill Page](https://clawhub.ai/engheng-art/skills/guaikei-douyin-trending-for-hotspot-tracking)
- [Publisher Profile](https://clawhub.ai/user/engheng-art)
- [Guaikei Token and Help Site](https://www.guaikei.com)
- [Complete Options Reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search CLI Request Schema](assets/search_cli_req.schema.json)
- [Search CLI Response Schema](assets/search_cli_resp.schema.json)
- [Post CLI Request Schema](assets/post_cli_req.schema.json)
- [Post CLI Response Schema](assets/post_cli_resp.schema.json)
- [Comment CLI Request Schema](assets/comment_cli_req.schema.json)
- [Comment CLI Response Schema](assets/comment_cli_resp.schema.json)
- [Hot List CLI Response Schema](assets/hot_cli_resp.schema.json)
- [Declared Repository Metadata](https://github.com/um-why/douyin-search-openclaw)

## Skill Output:

**Output Type(s):** [Shell commands, JSON, Files, Guidance]

**Output Format:** [JSON on stdout with status logs on stderr and JSON result files saved locally]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires GUAIKEI_API_TOKEN and supports search, post, comment, and hot-list command modes.]

## Skill Version(s):

1.0.0 (source: evidence release metadata, package.json, and skill metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
