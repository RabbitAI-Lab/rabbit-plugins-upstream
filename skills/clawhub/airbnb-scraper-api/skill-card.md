## Description:

Search Airbnb stays with the full discount ledger, pull one listing with its complete amenity list and rating breakdown, and page through real review bodies. 3 endpoints, 1 credit each, structured JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Agents, developers, and analysts use this skill to search Airbnb stay options, inspect listing details and amenities, retrieve rating breakdowns, and page through guest review text for travel planning, rental-market research, comparable sets, and host analytics.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses an external API key and optional SDK installation.

Mitigation: Use an isolated environment, expose only SCAVIO_API_KEY, and keep the key out of source control.

Risk: Every Airbnb API call spends credits, including empty results and paginated calls.

Mitigation: Set explicit search criteria and page or review limits before calling the API.

Risk: Review text and host profiles can contain personal data about real people.

Mitigation: Summarize review and host information and avoid building individual profiles.

Risk: Airbnb date defaulting, currency defaults, or listing-detail calls can produce misleading price answers.

Mitigation: Send explicit check-in, check-out, and currency values; check dates_are_defaulted; and use search responses as the only source for prices.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/airbnb-scraper-api)
- [Scavio Airbnb search documentation](https://scavio.dev/docs/airbnb-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=airbnb-scraper-api)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=airbnb-scraper-api)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON request and response examples, shell setup commands, and Python or JavaScript code snippets.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires SCAVIO_API_KEY; API responses are structured JSON and each Airbnb endpoint call uses one credit.]

## Skill Version(s):

1.0.4 (source: server release metadata; artifact frontmatter is 1.0.0)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
