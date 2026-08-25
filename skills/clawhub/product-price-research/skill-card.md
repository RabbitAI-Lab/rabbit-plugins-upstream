## Description:

Researches products, prices, sellers, and reviews across major online marketplaces and retailers using the Crawlora API, returning clean JSON for product discovery, price comparison, listing tracking, and review lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping research agents use this skill to compare products, prices, sellers, availability, and reviews across supported marketplaces and retailers without scraping store pages directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send API-key-authenticated requests to arbitrary Crawlora paths or to an overridden API base.

Mitigation: Use only trusted Crawlora API destinations, avoid setting CRAWLORA_API_BASE unless the destination is fully trusted, and review requested paths before execution.

Risk: Queries may expose secrets or sensitive personal data to an external API.

Mitigation: Do not pass secrets or sensitive personal data in product, seller, review, or location queries; keep CRAWLORA_API_KEY scoped and rotateable.

Risk: The security verdict is suspicious because the helper script is broader than the product-price research behavior described by the skill.

Mitigation: Review before installing and narrow or document the helper's permitted endpoint scope before use in restricted environments.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/product-price-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses the Crawlora API and returns normalized JSON from supported marketplace and retailer endpoints.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
