## Description:

Researches public Shopify-powered storefronts through the Crawlora API, including products, collections, pages, sitemaps, search suggestions, product recommendations, and pre-wired DTC brand endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and commerce researchers use this skill to audit public Shopify catalogs, crawl storefront sitemaps, inspect product and collection details, and compare storefront search or recommendation behavior.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper sends the Crawlora API key and research inputs to Crawlora, and the security evidence warns that the API destination can be overridden.

Mitigation: Use only with a dedicated Crawlora API key, run it in a controlled environment, and prevent untrusted content from setting CRAWLORA_API_BASE.

Risk: The bundled helper is broader than a Shopify-only wrapper, which can increase misuse or accidental calls outside the intended research scope.

Mitigation: Restrict use to documented Shopify and pre-wired brand endpoints, and prefer a version that validates the API base and allowlists Shopify endpoints.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/shopify-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY for authenticated Crawlora API calls; results are paginated for list endpoints.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
