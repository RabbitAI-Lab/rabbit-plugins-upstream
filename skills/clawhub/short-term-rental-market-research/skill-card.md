## Description:

Compare short-term rental supply, listing density, room mix, prices, and review signals using Crawlora Airbnb aggregates and selected live listings, while stating sampling and freshness limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, analysts, and developers compare observed short-term rental supply, density, room types, price distributions, and review signals across markets. Optional live listings illustrate the findings but are not a representative sample.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora API receives the user's API key and Airbnb-related search parameters.

Mitigation: Use the skill only when comfortable sharing those details with Crawlora; keep the key in the environment and limit queries to the approved scope and credit budget.

Risk: Sampled listings, suppressed cells, and public calendars may be mistaken for complete supply, bookings, occupancy, revenue, or legal permission.

Mitigation: Label coverage and collection dates, keep examples separate from aggregates, and do not infer occupancy, revenue, or legal permissibility from these signals.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/short-term-rental-market-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown market comparison with separately labeled listing examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes geography, filters, collection dates, price basis, coverage and suppression limits, and source identifiers where available.]

## Skill Version(s):

1.0.9 (source: server-resolved ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
