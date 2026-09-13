## Description:

Researches products, prices, brands, and categories on Zalando using the Crawlora API, returning clean JSON for product search, category browsing, autocomplete, product detail, and storefront-market lookup.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public Zalando catalog data through Crawlora instead of scraping Zalando pages directly. It supports current price checks, product comparisons, brand or category browsing, autocomplete, product-detail lookup, and market-code resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Zalando search terms, SKUs, market codes, and the Crawlora API key to Crawlora.

Mitigation: Use the skill only when that data sharing is acceptable, keep CRAWLORA_API_KEY in the environment, and never hardcode or commit the key.

Risk: Catalog research may be subject to Crawlora and Zalando terms for the user's intended use.

Mitigation: Review the applicable Crawlora and Zalando terms before using the skill in commercial workflows.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/zalando-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)
- [Crawlora](https://crawlora.net)
- [Zalando endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [text, json, shell commands, configuration, guidance]

**Output Format:** [JSON responses with concise Markdown guidance and shell command examples when useful]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends user-directed Zalando search terms, SKUs, and market codes to Crawlora.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
