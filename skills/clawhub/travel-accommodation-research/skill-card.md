## Description:

Compares public accommodation, short-term rental, hotel, flight, and activity listings across Airbnb, Agoda, Hotels.com, and Trip.com using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and travel researchers use this skill to compare public travel listings, inspect property and host evidence, and keep dates, currency, occupancy, location, and platform identity attached to results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search details and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, and keep secrets, payment data, government IDs, and private account information out of requests.

Risk: Prices, availability, reviews, and cancellation terms can change after retrieval.

Mitigation: Record retrieval time and verify final prices and booking decisions on the originating travel platform.

Risk: Partial responses can omit fees, taxes, or booking terms needed for a final total.

Mitigation: Keep nightly rates, displayed totals, fees, taxes, cancellation terms, availability, and currency separate, and do not invent checkout totals.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/travel-accommodation-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should preserve source platform, retrieval time, dates, occupancy, location, prices, fees, taxes, cancellation terms, availability, and currency where available.]

## Skill Version(s):

1.0.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
