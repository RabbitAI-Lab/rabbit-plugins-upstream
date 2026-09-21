## Description:

Compares public accommodation, short-term rental, hotel, flight, and activity listings across Airbnb, Agoda, Hotels.com, and Trip.com using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Travel planners, agents, and developers use this skill to compare public stays, flights, activities, host details, availability, prices, reviews, and source links across supported travel platforms. It supports research and evidence gathering only, without booking, payment, or traveler account changes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel search inputs and the Crawlora API key are sent to Crawlora for processing.

Mitigation: Use only the destination, date, occupancy, property ID, and similar details needed for the search; avoid unnecessary sensitive personal details and manage CRAWLORA_API_KEY as a secret.

Risk: Prices, availability, reviews, and cancellation terms are time-sensitive, platform-reported data.

Mitigation: Record retrieval time, source platform, dates, guests, and currency, and verify material booking decisions on the originating platform.

Risk: Platform-specific property IDs, route methods, and request bodies are not interchangeable.

Mitigation: Use the generated endpoint reference and the helper's fixed route and method checks before comparing or fetching details.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown or JSON-backed travel research summaries with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves platform, date, occupancy, currency, source, and retrieval context for comparisons.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
