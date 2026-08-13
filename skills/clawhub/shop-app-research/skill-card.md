## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API and returns clean JSON for product discovery, merchant comparison, reviews, and catalog browsing.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research public Shop.app products, variants, merchants, collections, and reviews through documented Crawlora API endpoints instead of scraping Shop.app pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora API paths beyond the Shop.app endpoints described by the skill.

Mitigation: Restrict agent and user calls to the documented /shop-app endpoints unless a separate review approves broader Crawlora usage.

Risk: Search terms, shop handles, product IDs, and related identifiers are sent to Crawlora with the user's API key.

Mitigation: Avoid sending secrets, personal data, or confidential business queries, and review requested identifiers before making API calls.

Risk: The security verdict is suspicious because the general helper is broader than the Shop.app-only purpose.

Mitigation: Review the skill before installing and scan any local changes before deployment.

## Reference(s):

- [Shop.app endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/shop-app-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, JSON, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and documented Crawlora Shop.app endpoints; API results are limit-capped by endpoint.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
