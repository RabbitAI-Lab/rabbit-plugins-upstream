## Description:

General-purpose web-intelligence utilities via the Crawlora API for scraping public URLs, extracting structured page data, fingerprinting web technology, geocoding, comparing cost of living, researching trade records, checking site traffic, and resolving brand metadata.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill for one-off web research and utility lookups through Crawlora, including page scraping, schema-based extraction, technology fingerprinting, geocoding, cost-of-living comparison, supplier research, traffic lookup, and brand metadata retrieval.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send broad raw Crawlora API requests when given arbitrary paths or payloads.

Mitigation: Review each endpoint path and payload before execution, especially when private, proprietary, or credential-like data may be included.

Risk: CRAWLORA_API_BASE can redirect requests to a non-default host if set in the environment.

Mitigation: Keep CRAWLORA_API_BASE unset or confirm it points to a trusted Crawlora API host before use.

Risk: The skill requires raw Crawlora API access through CRAWLORA_API_KEY.

Mitigation: Scope the API key to this use, store it only in the environment, and avoid committing or passing it in query strings.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs)
- [Crawlora playground](https://crawlora.net/playground)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/web-utilities-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key and sends requests to the configured Crawlora API base.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
