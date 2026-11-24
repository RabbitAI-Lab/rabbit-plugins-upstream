## Description:

Collects public Douyin search, creator, post, comment, and trending data as structured JSON for content research and analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[why20261](https://clawhub.ai/user/why20261)

### License/Terms of Use:

MIT

## Use Case:

Content creators, social media operators, marketers, and analysts use the skill to research public Douyin videos and accounts, track trends, review comments, and prepare structured material for topic, competitor, sentiment, and audience-needs analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, links, and IDs supplied for queries are sent to the third-party API.

Mitigation: Use public, non-sensitive query terms and identifiers, and proceed only when third-party processing is acceptable for the task.

Risk: The scanner reports that keyword-based account discovery is not fully described and that inspection was partial.

Mitigation: Review the documented account-search behavior and keep requests scoped to the public account discovery the user asked for.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/why20261/skills/douyin-data-research)
- [Service and API token information](https://www.guaikei.com)
- [Output contract](references/contract.md)
- [Intent routing](references/routing.md)
- [Command options](references/options.md)
- [Comment demand analysis](references/demand-mining.md)
- [Public audience research guidance](references/customer-acquisition.md)
- [Environment and FAQ](references/faq.md)

## Skill Output:

**Output Type(s):** [JSON, Markdown, Shell commands, Guidance]

**Output Format:** [Structured JSON data from Douyin queries, with concise Markdown summaries or analysis when requested.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results can be saved locally for later analysis; the skill documents public-data-only, read-only use.]

## Skill Version(s):

1.5.0 (source: SKILL.md frontmatter, package.json)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
