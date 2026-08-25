## Description:

A Twitter/X API guide for agents that need to search tweets, resolve profiles, pull timelines and followers, read lists, check trends, and call fetcher.sh endpoints using Bearer-key credits or x402 payments.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to choose and call read-only Twitter/X data endpoints for search, profiles, timelines, followers, lists, trends, and related social-data workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Twitter/X queries and requested identifiers to twitter.fetcher.sh.

Mitigation: Confirm the destination service is acceptable for the data being queried before use.

Risk: Calls may spend prepaid credits or trigger x402 USDC payments, especially during polling or pagination.

Mitigation: Set spending controls and bound loops, polling intervals, and pagination depth before running automated workflows.

Risk: Fetcher API keys grant paid access if exposed.

Mitigation: Store API keys as secrets and avoid committing them or placing real keys in shared MCP configurations.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/twitter-api)
- [Server-resolved GitHub source](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/twitter-api)
- [Twitter / X endpoint reference](references/endpoints.md)
- [Twitter / X scenario cookbook](references/scenarios.md)
- [Twitter / X API FAQ](references/faq.md)
- [Twitter / X data access comparison](references/comparison.md)
- [Full agent setup](https://twitter.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://twitter.fetcher.sh/openapi.json)
- [Condensed endpoint catalog](https://twitter.fetcher.sh/llms.txt)
- [Fetcher.sh Twitter API site](https://twitter.fetcher.sh)

## Skill Output:

**Output Type(s):** [Guidance, API Calls, Shell commands, Configuration]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only HTTP GET guidance; API responses are described as JSON envelopes.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
