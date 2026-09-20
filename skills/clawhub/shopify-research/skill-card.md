## Description:

Researches independent Shopify-powered storefronts, including products, collections, pages, sitemaps, search suggestions, and product recommendations, using the Crawlora API and returning normalized JSON for any store by domain plus pre-wired brand storefronts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to audit Shopify storefront catalogs, crawl store sitemaps, inspect product and collection data, and research public search or recommendation behavior through Crawlora-backed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Store domains, search terms, and optional location coordinates may be sent to Crawlora under the user's Crawlora API key.

Mitigation: Use the skill only for approved public storefront research and avoid confidential competitive targets or regulated personal data unless that third-party use is approved.

Risk: The skill executes a shell helper that sends authenticated GET requests to the Crawlora API.

Mitigation: Keep CRAWLORA_API_KEY in the environment, review commands before execution, and do not hardcode, pass in query parameters, or commit the key.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/shopify-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; Crawlora API calls return JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and public storefront or documented brand endpoint inputs.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
