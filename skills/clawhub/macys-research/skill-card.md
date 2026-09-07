## Description:

Looks up a Macy's product's full detail and customer reviews by its numeric productId, and pulls Macy's own search-box typeahead suggestions through the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping researchers use this skill to retrieve structured Macy's product details, reviews, rating summaries, variant information, pricing, availability, and autocomplete suggestions when they already have a numeric Macy's productId or a partial suggestion query.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script exposes broader Crawlora API access and credential handling than the Macy's-only purpose describes.

Mitigation: Keep CRAWLORA_API_BASE unset, use a limited Crawlora key if possible, and avoid sending private data through the helper until it restricts requests to the documented Macy's endpoints.

Risk: The skill cannot perform full-text product search or category browsing, so using it without a known productId can produce incomplete results.

Mitigation: Confirm the Macy's productId from a product page ?ID= value before requesting product details or reviews, and use the suggest endpoint only for typeahead term discovery.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/macys-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a known Macy's productId for product detail or review calls.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
