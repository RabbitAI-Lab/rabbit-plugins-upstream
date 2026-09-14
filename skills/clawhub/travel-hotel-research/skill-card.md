## Description:

Researches hotels, flights, attractions, short-term rentals, and live events via the Crawlora API, returning clean JSON for travel and event comparison workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search and compare hotels, flights, attractions, short-term rentals, hosts, listings, venues, and live events across supported travel platforms. It is suited to itinerary research, price comparison, review lookup, and event discovery before a user makes booking or payment decisions outside the skill.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Travel searches, dates, locations, and itinerary details are sent to Crawlora and underlying travel data providers.

Mitigation: Review query content before sending sensitive itinerary details and install only when this data sharing is acceptable.

Risk: The Crawlora API key could be exposed if it is hardcoded, committed, or passed directly in command arguments.

Mitigation: Store CRAWLORA_API_KEY in the environment and avoid placing secrets in source files, shell history, or shared logs.

Risk: Some Expedia POST body shapes are documented as unconfirmed in the artifact.

Mitigation: Confirm current request payloads in the Crawlora documentation or playground before relying on Expedia endpoint results.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora API Playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/travel-hotel-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns public travel or event data from Crawlora-supported endpoints.]

## Skill Version(s):

1.0.16 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
