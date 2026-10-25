## Description:

通过怪奇信息查询和分析 TikTok 视频、达人、评论和品类机会，为市场调研、竞品分析、爆款挖掘和短视频运营提供结构化公开数据。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

External users, analysts, marketers, and agent developers use this skill to retrieve TikTok keyword search results, creator posts, and video comments as structured JSON for market research, competitor monitoring, creator discovery, social listening, and content planning.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends GUAIKEI_API_TOKEN and TikTok search terms, profile URLs, or video IDs to www.guaikei.com.

Mitigation: Install only if this data-sharing model is acceptable; provide the token through the environment and avoid exposing it in prompts, shared logs, or reports.

Risk: Fetched comments and user identifiers are public personal data and fetched results may be saved locally.

Mitigation: Limit retention, avoid unnecessary sharing, delete temporary logs when no longer needed, and de-identify user information before external publication.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-research)
- [Guaikei API service](https://www.guaikei.com)
- [Parameter options](references/options.md)
- [Changelog](references/changelog.md)
- [Search request schema](assets/search_cli_req.schema.json)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Creator posts request schema](assets/post_cli_req.schema.json)
- [Creator posts response schema](assets/post_cli_resp.schema.json)
- [Comment request schema](assets/comment_cli_req.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Markdown, Guidance, Configuration]

**Output Format:** [Structured JSON from CLI stdout, with human-facing Markdown summaries or guidance when an agent interprets results.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js and GUAIKEI_API_TOKEN; commands return status, error_code, request metadata, results, and warnings.]

## Skill Version(s):

1.0.0 (source: server release metadata, SKILL.md frontmatter, package.json, changelog released 2026-09-20)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
