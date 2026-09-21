## Description:

Researches products, prices, sellers, and reviews across major marketplaces and retailers using the Crawlora API, returning normalized JSON for comparison and review workflows.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to answer product research requests: search catalogs, compare marketplace prices and sellers, retrieve product details, and summarize public ratings or reviews without scraping retailer pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shopping searches, retailer or product identifiers, and optional location inputs are sent to Crawlora using the configured API key.

Mitigation: Avoid passing secrets, private storefront URLs, or precise coordinates unless required for the task; keep CRAWLORA_API_KEY in the environment and out of committed files, prompts, and command arguments.

## Reference(s):

- [Product Price Research Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/product-price-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and normalized JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API requests send shopping queries and selected product, seller, review, or location parameters to Crawlora.]

## Skill Version(s):

1.0.19 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
