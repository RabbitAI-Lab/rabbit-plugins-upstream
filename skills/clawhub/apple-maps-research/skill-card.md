## Description:

Researches places, categories, guides, routes, transit, and travel times through Apple Maps via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to research Apple Maps places, categories, guides, routes, transit departures, reverse geocoding, and travel-time estimates through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Map searches, coordinates, routes, place IDs, and related request data are sent to Crawlora using the user's Crawlora API key.

Mitigation: Avoid using precise home, work, or sensitive travel locations unless sharing that data with Crawlora is acceptable.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/apple-maps-research)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration]

**Output Format:** [JSON responses with Markdown usage guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
