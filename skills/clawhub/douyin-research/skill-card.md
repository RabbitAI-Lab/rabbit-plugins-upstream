## Description:

Queries public Douyin videos, creator posts, comments, and hot-list data through GuaiKei so agents can support market research, trend tracking, competitor monitoring, and content analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content, marketing, operations, and research teams use this skill to fetch structured public Douyin data for topic discovery, account benchmarking, comment review, hot-list tracking, and business reporting.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries send Douyin keywords or links and the GuaiKei API token to www.guaikei.com.

Mitigation: Install and run the skill only when this third-party API use is acceptable, and keep GUAIKEI_API_TOKEN scoped and protected.

Risk: Fetched comments and creator data are public but may still contain sensitive user-generated content.

Mitigation: Use results only for appropriate internal analysis and handle exported JSON according to the user's data retention and privacy requirements.

Risk: Search, creator-post, and comment commands can retain result files in a local logs directory.

Mitigation: Clean up local logs after analysis when retained Douyin data is not needed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/why20261/skills/douyin-research)
- [GuaiKei API token and support site](https://www.guaikei.com)
- [Options reference](references/options.md)
- [Changelog](references/changelog.md)
- [Search response schema](assets/search_cli_resp.schema.json)
- [Post response schema](assets/post_cli_resp.schema.json)
- [Comment response schema](assets/comment_cli_resp.schema.json)
- [Hot-list response schema](assets/hot_cli_resp.schema.json)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Structured JSON envelopes, with concise Markdown summaries when an agent reports results to a user]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires Node.js 16.14.0+ and GUAIKEI_API_TOKEN; commands return stdout JSON and may retain search, post, and comment results in local logs.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, changelog, server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
