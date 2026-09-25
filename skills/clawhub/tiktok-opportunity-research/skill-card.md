## Description:

研究 TikTok 搜索结果、作品结构、达人数据和用户反馈，筛选值得继续验证的机会。

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Creators, marketers, analysts, and operators use this skill to retrieve public TikTok search results, creator posts, and video comments for opportunity research, competitor monitoring, influencer screening, content analysis, and social listening.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends the API token and TikTok search terms, profile URLs, or video IDs to www.guaikei.com.

Mitigation: Use the skill only when that external service is trusted for the requested data and token handling.

Risk: Saved result logs may contain public usernames, profile identifiers, and comment text.

Mitigation: Delete or protect local logs when the collected public TikTok data is sensitive.

Risk: The skill returns public social media data that may require care before external publication or commercial use.

Mitigation: Review authorization and privacy requirements, and de-identify usernames or profile identifiers when appropriate.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/tiktok-opportunity-research)
- [TikTok data access service](https://www.guaikei.com)
- [Complete command options](references/options.md)
- [Changelog](references/changelog.md)
- [Search input schema](assets/search_cli_req.schema.json)
- [Search output schema](assets/search_cli_resp.schema.json)
- [Creator posts input schema](assets/post_cli_req.schema.json)
- [Creator posts output schema](assets/post_cli_resp.schema.json)
- [Comments input schema](assets/comment_cli_req.schema.json)
- [Comments output schema](assets/comment_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured JSON results from the command-line tools]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The command outputs use a consistent JSON envelope with status, error_code, request metadata, results, and warnings.]

## Skill Version(s):

1.0.0 (source: frontmatter, package.json, changelog, ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
