## Description:

A Yelp API alternative on fetcher.sh for local business search, business details, and reviews through paid HTTP GET calls that return clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

External developers and agents use this skill to search local businesses, retrieve Yelp-style business details, and fetch reviews for local discovery, restaurant or service research, review analysis, and competitor monitoring.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Business search queries and requested business identifiers are sent to yelp.fetcher.sh.

Mitigation: Use the skill only when sharing those queries with the third-party API provider is acceptable.

Risk: The skill can trigger paid API calls through a Fetcher Bearer key or x402 payment flow.

Mitigation: Review pricing, wallet use, credit top-ups, and refund limitations before allowing paid calls.

Risk: Fetcher API keys are used for prepaid-credit authentication.

Mitigation: Store keys in environment variables or an approved secret store and avoid exposing them in prompts, logs, or shared files.

## Reference(s):

- [Server-resolved GitHub provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/yelp)
- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/yelp-api)
- [Full agent setup](https://yelp.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://yelp.fetcher.sh/openapi.json)
- [Condensed catalog](https://yelp.fetcher.sh/llms.txt)
- [Yelp API site](https://yelp.fetcher.sh)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API calls, JSON]

**Output Format:** [Markdown guidance with inline bash commands, MCP configuration JSON, and HTTP API examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API responses are described as JSON objects with status, message, and data fields.]

## Skill Version(s):

0.1.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
