## Description:

Build event shortlists, dated calendars, and venue comparisons through Crawlora's Ticketmaster and TicketWeb endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public events, compare venues, and prepare dated shortlists or calendars with venue identity, timing, age restrictions, ticket fees, availability caveats, and fit rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can make authenticated Crawlora requests beyond the event-focused workflow if it is invoked with arbitrary paths or an unexpected API base.

Mitigation: Use only after reviewing the publisher and environment, confirm CRAWLORA_API_BASE before execution, avoid sensitive request bodies, and prefer a non-production Crawlora key.

Risk: Event availability, ticket status, and prices can change after collection.

Mitigation: Recheck shortlisted events close to delivery and preserve the collection time, status, price scope, and availability caveats in outputs.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown tables or calendars with concise notes and optional shell command snippets]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include event and provider IDs, canonical links, venue addresses, local start times and zones, status, age or access information, dated ticket price scope, availability, and fit rationale.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
