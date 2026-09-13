## Description:

Researches places, categories, guides, routes, transit, and travel times through Apple Maps via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Apple Maps places, categories, guides, routes, transit departures, reverse geocoding results, and ETA estimates through Crawlora's API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Apple Maps queries, precise coordinates, addresses, place IDs, route details, and the Crawlora API key are sent to Crawlora's external API.

Mitigation: Use the skill only for data you are comfortable sharing with Crawlora, avoid unnecessarily precise home, work, or sensitive travel locations, and keep the API key in a trusted environment.

## Reference(s):

- [Apple Maps endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/apple-maps-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to the Crawlora API.]

## Skill Version(s):

1.0.8 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
