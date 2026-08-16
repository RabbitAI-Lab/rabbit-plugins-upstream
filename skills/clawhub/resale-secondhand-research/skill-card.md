## Description:

Researches secondhand, resale, and handmade marketplaces through the Crawlora API for listing search, seller review, resale-price checks, and handmade or vintage goods research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to search public resale and handmade marketplace listings, compare prices, review seller or shop profiles, and inspect sneaker, streetwear, vintage, and livestream-shopping data across supported platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The API helper can send the Crawlora API key and user-supplied data to endpoints beyond the stated resale marketplace use case.

Mitigation: Use a limited, revocable Crawlora API key and restrict calls to the documented resale marketplace endpoints and official Crawlora API base.

Risk: Search terms and other request data are sent to an external API service.

Mitigation: Avoid submitting secrets or sensitive personal data as search terms or parameters.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a CRAWLORA_API_KEY and external network access to the Crawlora API.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
