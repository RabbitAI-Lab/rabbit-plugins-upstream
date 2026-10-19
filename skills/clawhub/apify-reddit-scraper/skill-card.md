## Description:

Guides agents in searching and scraping public Reddit posts, comments, users, and communities through a paid Apify Actor, with optional delivery to connected tools.

This skill is ready for commercial/non-commercial use.

## Publisher:

[harshmaur](https://clawhub.ai/user/harshmaur)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can collect Reddit posts, comments, user profiles, and community information for brand monitoring, community research, and structured datasets, then optionally deliver results to authorized connectors.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Broad searches, comment collection, and recurring runs can incur substantial Apify charges.

Mitigation: Estimate per-term and per-comment costs, start with smaller limits, and confirm large or recurring runs.

Risk: Queries and scraped public Reddit data go to Apify and may be forwarded through optional third-party connectors.

Mitigation: Scrape user histories or communities only when intended, and authorize and review destinations before forwarding results.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/harshmaur/skills/apify-reddit-scraper)
- [Apify MCP integration documentation](https://docs.apify.com/platform/integrations/mcp)
- [Input mapping](references/input-mapping.md)
- [Cost and usage gotchas](references/gotchas.md)

## Skill Output:

**Output Type(s):** [Markdown, Text, Shell commands, Configuration guidance]

**Output Format:** [Markdown summaries with example commands and JSON Actor inputs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Reports searched inputs, Reddit result counts and links, and estimated versus settled run costs.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
