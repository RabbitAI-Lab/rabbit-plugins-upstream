## Description:

Researches public Shopify storefront products, collections, pages, sitemaps, search suggestions, and recommendations through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and commerce researchers use this skill to audit public Shopify catalogs, explore store content, and analyze storefront search and product recommendations.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Storefront URLs, search terms, and the API key are sent to Crawlora when the skill runs.

Mitigation: Use the skill only when this data sharing is acceptable; keep the key in CRAWLORA_API_KEY and never paste it into prompts or files.

Risk: Successful API requests may consume Crawlora credits.

Mitigation: Confirm the requested scope before making calls, especially for full-store crawls.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/shopify-research)
- [Shopify research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, JSON]

**Output Format:** [JSON storefront results and text summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public storefront data; list results may require pagination.]

## Skill Version(s):

1.0.18 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
