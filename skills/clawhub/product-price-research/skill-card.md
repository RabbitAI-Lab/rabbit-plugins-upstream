## Description:

Researches products, prices, sellers, and reviews across major online marketplaces and big-box or specialty retailers using the Crawlora API, returning clean JSON for product discovery, price comparison, seller research, listing tracking, and marketplace or retailer reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and research agents use this skill to compare product prices, sellers, availability, variants, and reviews across supported marketplaces and retailers without scraping store pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can call a broader Crawlora API surface than the product-research workflow advertises.

Mitigation: Use a wrapper or policy that allowlists only the documented retailer and marketplace endpoints needed for the task.

Risk: The Crawlora API key could be exposed if CRAWLORA_API_BASE is redirected to an untrusted destination.

Mitigation: Keep CRAWLORA_API_BASE unset unless the destination is fully controlled, and use a separate Crawlora key with limited exposure.

Risk: Product, review, seller, store, or location lookups may include sensitive personal data or precise locations.

Mitigation: Avoid sending sensitive personal data or precise locations unless they are necessary for the user-requested research.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key and returns paginated normalized public product, seller, price, availability, and review data where supported.]

## Skill Version(s):

1.0.10 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
