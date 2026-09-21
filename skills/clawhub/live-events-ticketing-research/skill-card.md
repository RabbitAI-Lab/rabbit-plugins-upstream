## Description:

Research public StubHub and SeatGeek event calendars and resale-price snapshots. Use for location, category, performer, or venue ticket-market comparisons; not for purchases, bids, or primary-ticket checkout.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to compare public, read-only secondary-market event calendars and resale-price snapshots across StubHub and SeatGeek for events, performers, venues, locations, and categories.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Ticket-search queries, event details, and optional coordinates are sent to Crawlora.

Mitigation: Use the skill only when this data sharing is acceptable, protect the Crawlora API key, and prefer coarse coordinates for privacy-sensitive searches.

Risk: Returned prices and availability are resale-market snapshots, not offers, holds, guarantees, checkout totals, or primary-market availability.

Mitigation: Report collection time, source, currency, and price-field meaning, and avoid presenting results as purchase-ready or all-in totals.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/live-events-ticketing-research)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown snapshot tables with source-faithful ticket-market details]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes provider, resale status, event/provider ID, canonical URL, venue, local time, price meaning, currency, availability signal, and observed_at timestamp.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
