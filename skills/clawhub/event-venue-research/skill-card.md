## Description:

Build event shortlists, dated calendars, and venue comparisons through Crawlora's Ticketmaster and TicketWeb endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Agents use this skill to research public events and venues for a destination, date range, audience needs, and budget. It supports shortlists, calendars, and venue comparisons with provider IDs, links, local timing, status, venue details, age or access notes, ticket price scope, availability, and fit rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Event search queries, selected event or venue IDs, and the Crawlora API key are sent to Crawlora's external API.

Mitigation: Keep the API key scoped and private, and review queries before running the helper.

Risk: Event availability, status, and prices can change, and a successful data response does not reserve seats or lock prices.

Mitigation: Recheck shortlisted events close to delivery and preserve the collection time and provider status in outputs.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown tables, calendars, concise guidance, and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include raw JSON from Crawlora API calls when the agent invokes the bundled helper.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
