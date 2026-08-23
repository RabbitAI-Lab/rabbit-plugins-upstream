## Description:

Guides agents in using the read-only instagram.fetcher.sh API to retrieve public Instagram profiles, posts, reels, stories, comments, followers, hashtags, locations, and audio feeds with Bearer-key or x402 payment.

This skill is ready for commercial/non-commercial use.

## Publisher:

[fetcher-sh](https://clawhub.ai/user/fetcher-sh)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, data engineers, and agents use this skill to make lawful, consent-aware public Instagram data queries for profile lookup, content monitoring, influencer discovery, competitor tracking, and data pipelines without Meta Graph API business verification or browser automation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Instagram identifiers and public activity queries are sent to a third-party service.

Mitigation: Use the skill only for lawful, consent-aware public-data workflows and review the provider's privacy and retention practices for the intended use case.

Risk: Public Instagram data workflows can be misused for harassment or unauthorized profiling.

Mitigation: Limit use to legitimate monitoring, research, or pipeline needs, and check Instagram terms and applicable policy requirements before deployment.

Risk: Each API request may incur payment through credits or x402.

Mitigation: Use budget controls and review planned calls before running high-volume collection or polling workflows.

## Reference(s):

- [Server-resolved GitHub source](https://github.com/fetcher-sh/fetcher-skills/tree/main/skills/instagram-api)
- [ClawHub skill page](https://clawhub.ai/fetcher-sh/skills/instagram-api)
- [Instagram API site](https://instagram.fetcher.sh)
- [OpenAPI 3.1 contract](https://instagram.fetcher.sh/openapi.json)
- [Condensed endpoint catalog](https://instagram.fetcher.sh/llms.txt)
- [Endpoint reference](references/endpoints.md)
- [Usage scenarios](references/scenarios.md)
- [FAQ](references/faq.md)
- [API comparison](references/comparison.md)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Configuration, API calls]

**Output Format:** [Markdown with inline bash and JSON code blocks]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Read-only GET calls to instagram.fetcher.sh; service responses use a JSON envelope.]

## Skill Version(s):

0.1.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
