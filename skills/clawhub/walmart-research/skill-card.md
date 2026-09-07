## Description:

Researches Walmart products, prices, sellers, and reviews using the Crawlora API, returning clean JSON for product search, price comparison, listing tracking, and review lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research public Walmart product data through Crawlora instead of scraping Walmart pages directly. It supports product discovery, price and availability comparison, seller checks, and review summaries.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to a configurable remote host.

Mitigation: Use a dedicated Crawlora key and verify that CRAWLORA_API_BASE is unset or pinned to https://api.crawlora.net/api/v1 before use.

Risk: The bundled script is broader than the advertised Walmart workflow.

Mitigation: Limit agent use to Walmart paths and GET requests unless a broader Crawlora API wrapper is intentionally needed.

## Reference(s):

- [walmart-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; intended endpoints cover Walmart search, product detail, and product reviews.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
