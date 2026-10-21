## Description:

Retrieves public Douyin search results, creator posts, trending topics, and comments to support content research and audience-demand analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content researchers, marketers, and product teams use public Douyin search, trend, creator, and comment data to identify content opportunities and investigate user needs. The agent can organize comments into themes and support findings with source excerpts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Douyin links and IDs are sent to Guaikei with an API token.

Mitigation: Use only when this external transfer is acceptable and keep the token secret.

Risk: Search, post, and comment results are retained in local JSON logs.

Mitigation: Avoid collecting targets or comments the workspace should not retain; review and remove logs when no longer needed.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/why20261/skills/douyin-demand-mining)
- [Demand-mining workflow](artifact/references/demand-mining.md)
- [Command options](artifact/references/options.md)
- [Guaikei API access and help](https://www.guaikei.com)

## Skill Output:

**Output Type(s):** [JSON, Analysis, Guidance]

**Output Format:** [Structured JSON results with optional Markdown summaries and demand analysis]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search, creator-post, and comment results are also saved as local JSON logs.]

## Skill Version(s):

1.3.0 (source: ClawHub release, frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
