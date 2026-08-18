## Description:

Fetches structured public web data via the Crawlora REST API - search engines, e-commerce, social, finance, maps, app stores, media, and reviews - returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch current public web data such as product prices, search results, reviews, transcripts, financial data, maps data, and trend signals as structured JSON instead of scraping HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security review reports that the skill exposes Crawlora account-usage and recent-IP endpoints outside its public-web-data purpose.

Mitigation: Use the skill only for public web-data lookups and do not let an agent call /usage/me/* endpoints unless account telemetry inspection is intentional.

Risk: Queries or API parameters could disclose secrets, confidential identifiers, or sensitive business context to an external API.

Mitigation: Avoid sending secrets or confidential identifiers as queries, keep the API key in CRAWLORA_API_KEY, and do not hardcode or commit credentials.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and calls the Crawlora REST API for public web data.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
