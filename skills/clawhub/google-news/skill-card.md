## Description:

Provides agent guidance for using the Fetcher Google News API to retrieve Google News search results, latest and section headlines, topic headlines, supported language-region codes, and decoded Google News redirect URLs as JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external agent users use this skill to configure authenticated or x402-paid calls to a third-party Google News API for media monitoring, headline aggregation, news search, and press mention workflows.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill uses a third-party paid service.

Mitigation: Review the Fetcher service terms and confirm the prepaid or x402 billing model before use.

Risk: Bearer keys can authorize paid API access if exposed.

Mitigation: Store FETCHER_API_KEY in a secret manager or protected environment variable and rotate it if it may have been shared.

Risk: Private search terms or redirect URLs may be sent to the provider.

Mitigation: Avoid submitting sensitive terms or URLs unless sharing them with the provider is acceptable.

## Reference(s):

- [ClawHub skill listing](https://clawhub.ai/fetcher-sh/skills/google-news)
- [Server-resolved source provenance](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/google-news)
- [Full agent setup](https://google-news.fetcher.sh/skill.md)
- [OpenAPI 3.1 contract](https://google-news.fetcher.sh/openapi.json)
- [Condensed catalog](https://google-news.fetcher.sh/llms.txt)
- [Service site](https://google-news.fetcher.sh)

## Skill Output:

**Output Type(s):** [Guidance, Markdown, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with curl examples, JSON configuration snippets, endpoint descriptions, and API response shape guidance]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Guidance covers bearer-key and x402 payment flows, required request parameters, endpoint selection, and common HTTP error meanings.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
