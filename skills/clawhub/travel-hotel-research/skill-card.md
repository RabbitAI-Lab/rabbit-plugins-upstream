## Description:

Researches hotels, flights, attractions, short-term rentals, and live events through the Crawlora API and returns normalized JSON for comparison and due diligence.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Travel researchers, planners, and assistant agents use this skill to compare hotels, flights, attractions, short-term rentals, and live events across supported travel platforms. It is useful for price comparison, review checks, destination research, and host or listing due diligence.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel, hotel, flight, rental, attraction, and event search parameters are sent to Crawlora as third-party network requests.

Mitigation: Send only the search details needed for the task and avoid sensitive personal information beyond what is required for the query.

Risk: The skill requires a Crawlora API key that could be exposed if stored or passed incorrectly.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not hardcode or commit it, and use the helper so the key is sent as a header rather than as a query parameter.

Risk: Some Expedia POST payload details may need confirmation before operational use.

Mitigation: Check the current Crawlora documentation or playground before relying on Expedia endpoints whose body shape is uncertain.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/travel-hotel-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented Crawlora routes for public travel, lodging, rental, attraction, and event data.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
