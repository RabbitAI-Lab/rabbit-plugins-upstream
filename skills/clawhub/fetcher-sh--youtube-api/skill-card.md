## Description:

A YouTube API alternative on fetcher.sh for searching and retrieving YouTube video, channel, playlist, comment, hashtag, and trending data through paid HTTP GET endpoints without OAuth or daily quota limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to build YouTube data workflows such as video search, channel monitoring, playlist inspection, comment retrieval, trend tracking, and analytics inputs through fetcher.sh endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill can guide calls to a third-party paid API that may consume prepaid credits or trigger x402 payment flows.

Mitigation: Confirm cost controls and payment posture before enabling API or MCP calls, and monitor credit balance or x402 spending.

Risk: Using prepaid access requires storing or providing a FETCHER_API_KEY.

Mitigation: Store the key in an approved secret manager or environment variable, avoid committing it to files, and rotate it if exposed.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/youtube-api)
- [Server-resolved GitHub provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/youtube-api)
- [Full agent setup](https://youtube.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://youtube.fetcher.sh/openapi.json)
- [Condensed endpoint catalog](https://youtube.fetcher.sh/llms.txt)
- [Service site](https://youtube.fetcher.sh)

## Skill Output:

**Output Type(s):** [guidance, markdown, shell commands, configuration, code]

**Output Format:** [Markdown with HTTP endpoint examples, curl commands, JSON MCP configuration, and parameter guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May guide paid API or MCP calls that require a Bearer key or x402 payment flow.]

## Skill Version(s):

0.1.0 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
