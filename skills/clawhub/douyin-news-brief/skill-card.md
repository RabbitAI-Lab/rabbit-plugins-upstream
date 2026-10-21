## Description:

Retrieves public Douyin search results, trending topics, creator posts and comments to support news briefs and social-media analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT-0

## Use Case:

Content teams, marketers and analysts use this skill to research public Douyin videos and images, monitor trends and creators, and summarize comments for briefs and audience insights.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, Douyin links and the API token are sent to the GUAIKEI service.

Mitigation: Confirm outbound sharing is authorized; avoid submitting sensitive terms or identifiers and protect the token.

Risk: Successful search, creator-post and comment results are saved to local logs without a command-level opt-out.

Mitigation: Use only where local retention is acceptable, or add controls to disable or clean the logs.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-news-brief)
- [GUAIKEI service](https://www.guaikei.com)
- [Options and usage](references/options.md)
- [Demand-mining workflow](references/demand-mining.md)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured JSON results; optional prose summaries and reports]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, creator details and engagement metrics when available.]

## Skill Version(s):

1.3.0 (source: frontmatter, package.json, changelog)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
