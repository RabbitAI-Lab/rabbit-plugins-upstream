## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API, returning clean JSON for cross-store product, merchant, and review research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and shopping research agents use this skill to query public Shop.app product, shop, variant, and review data through Crawlora instead of scraping pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an endpoint selected through CRAWLORA_API_BASE.

Mitigation: Use a dedicated Crawlora key and leave CRAWLORA_API_BASE unset or pin it to https://api.crawlora.net/api/v1 before running the helper.

Risk: The helper script is broader than the Shop.app use case described by the skill.

Mitigation: Review commands before execution and restrict use to /shop-app/ GET endpoints unless a separate review approves broader Crawlora API access.

Risk: Search terms and merchant or product inputs are sent to the Crawlora API.

Mitigation: Avoid sensitive search inputs and use only public Shop.app product, shop, variant, and review data.

## Reference(s):

- [Shop.app endpoint reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/shop-app-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY; requests use public Shop.app endpoints through the Crawlora API.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
