## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API and returns clean JSON for cross-merchant product discovery, shop comparison, review retrieval, and catalog browsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and shopping-analysis agents use this skill to search Shop.app, compare products and shops, inspect variants and availability, and retrieve public reviews through Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call unrelated Crawlora APIs and send arbitrary request data.

Mitigation: Review or restrict scripts/crawlora.sh to /shop-app endpoints before installation or use.

Risk: Shop.app search terms, product or shop identifiers, and selected options are sent to Crawlora under the user's API key.

Mitigation: Keep CRAWLORA_API_KEY secret and avoid using private or sensitive shopping information with the skill.

## Reference(s):

- [Shop.app endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora API key signup](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that call Crawlora and return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to Crawlora's public API.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
