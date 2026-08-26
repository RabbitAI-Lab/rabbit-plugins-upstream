## Description:

Looks up public LinkedIn company, product, and showcase pages by ID through the Crawlora API and returns normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve public LinkedIn company, product, and showcase data by known LinkedIn IDs for company enrichment, competitor profiling, and product or showcase page audits.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send arbitrary paths, HTTP methods, query parameters, and JSON bodies to the external Crawlora service.

Mitigation: Review or narrow use to the documented LinkedIn GET endpoints before installation or agent delegation.

Risk: Requests may transmit chosen paths, parameters, and possible JSON bodies to Crawlora.

Mitigation: Use only approved public LinkedIn company, product, or showcase IDs and avoid sending sensitive data in paths, query parameters, or bodies.

Risk: The skill requires an external API key.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, pass it in query parameters, or commit it.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/linkedin-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration instructions, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; intended endpoints require known LinkedIn company, product, or showcase IDs.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
