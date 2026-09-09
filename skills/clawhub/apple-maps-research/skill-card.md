## Description:

Researches places, categories, guides, routes, transit, and travel times through Apple Maps via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research analysts use this skill to search Apple Maps places, inspect place details and guides, reverse-geocode coordinates, and estimate routes or travel times through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Apple Maps searches, coordinates, routes, and related location data to Crawlora using the user's API key.

Mitigation: Review before installing and avoid sending sensitive location data unless the Crawlora service and account controls are acceptable for the use case.

Risk: The helper script is broader and less constrained than the Apple Maps-focused skill description.

Mitigation: Constrain use to /apple-maps endpoints, validate JSON bodies and key=value query parameters, reject curl @ file-loading inputs, and remove or strictly validate CRAWLORA_API_BASE.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; Apple Maps search, coordinate, route, and location data are sent to Crawlora.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
