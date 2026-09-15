## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research Zalando products, prices, brands, categories, storefront markets, autocomplete results, and product details through normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Zalando search terms, SKUs, markets, and the Crawlora API key are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep CRAWLORA_API_KEY in the environment, and do not hardcode or commit the key.

Risk: Commercial catalog or pricing research may be subject to Crawlora and Zalando terms.

Mitigation: Review the applicable Crawlora and Zalando terms before use in the intended workflow.

Risk: Search and category endpoints return only the first page, and category slugs and SKUs are market-specific.

Mitigation: Resolve storefront markets first, keep the same market between search and product-detail calls, and treat first-page catalog results as partial.

## Reference(s):

- [zalando-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/zalando-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a valid Zalando market code for most product endpoints.]

## Skill Version(s):

1.0.15 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
