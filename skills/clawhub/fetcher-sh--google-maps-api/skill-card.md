## Description:

Google Maps API guides agents to search places, fetch place details and reviews, and configure fetcher.sh paid HTTP or MCP access as a Google Places-style alternative.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to discover local businesses and points of interest, retrieve place details, monitor reviews, and configure paid fetcher.sh HTTP or MCP access without Google Cloud billing setup.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Enabled MCP tools can make paid API calls when invoked.

Mitigation: Review MCP configuration before deployment and enable paid tools only where per-call costs are acceptable.

Risk: Place-search queries and review requests are sent to fetcher.sh.

Mitigation: Avoid sending sensitive or restricted location, customer, or business data unless the deployment has approved that external processing.

Risk: Bearer credentials can authorize prepaid usage.

Mitigation: Store FETCHER_API_KEY in a secret manager or environment variable and do not commit it to skill files, prompts, or logs.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/google-maps-api)
- [Server-resolved source repository](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/google-maps)
- [Full agent setup](https://google-maps.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://google-maps.fetcher.sh/openapi.json)
- [Condensed catalog](https://google-maps.fetcher.sh/llms.txt)
- [Service site](https://google-maps.fetcher.sh)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown guidance with JSON and bash examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes endpoint descriptions, authentication options, MCP configuration, and error-handling guidance.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
