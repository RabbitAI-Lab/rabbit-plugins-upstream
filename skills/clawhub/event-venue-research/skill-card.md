## Description:

Build event shortlists, dated calendars, and venue comparisons through Crawlora's Ticketmaster and TicketWeb endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public events and compare venues using Crawlora event endpoints. It helps produce dated shortlists, calendars, and venue comparisons with venue identity, timing, age or access restrictions, ticket fees, availability caveats, and fit rationale.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and event or venue IDs are sent to Crawlora with the user's CRAWLORA_API_KEY.

Mitigation: Install only when that data sharing is acceptable, keep the key in the environment, and treat it as a credential.

Risk: Ticket availability, prices, and event status can change after results are collected.

Mitigation: Recheck shortlisted events close to delivery and preserve source status, price scope, and collection time.

Risk: Some ticket states are ambiguous, such as TicketWeb events without purchasable sections.

Mitigation: Report the observable availability state and avoid guessing whether the event is free, sold out, or access-code-gated.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown tables or calendars with source links, local event times, venue details, ticket status, price caveats, and optional shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves provider IDs, collection time, availability caveats, and local timezone details; does not create calendar entries or buy tickets unless explicitly asked.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
