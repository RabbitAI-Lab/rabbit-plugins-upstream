## Description:

Researches Yahoo editorial content across Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech through Crawlora API endpoints that return normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and research agents use this skill to fetch public Yahoo story feeds, full article content, comments, shopping deals, and sports data for summarization or analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call non-Yahoo Crawlora endpoints or a redirected API host while carrying the user's API key.

Mitigation: Use only documented /yahoo-* endpoints and leave CRAWLORA_API_BASE unset unless the replacement host is fully trusted.

Risk: Private or confidential data could be sent through the helper to the external API service.

Mitigation: Use the skill only for public Yahoo content and avoid passing private data in URLs, parameters, or request bodies.

Risk: The Crawlora API key could be exposed if hardcoded, committed, or sent as a query parameter.

Mitigation: Keep the key in CRAWLORA_API_KEY and pass it only through the x-api-key header.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/yahoo-network-research)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; responses are public Yahoo network data returned as JSON.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
