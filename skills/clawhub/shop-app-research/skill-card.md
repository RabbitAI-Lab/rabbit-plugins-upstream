## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API and returns normalized JSON instead of scraping Shop.app pages.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to search Shop.app products, compare merchant offerings, inspect variants and availability, pull public reviews, and browse merchant catalogs through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the Crawlora API key to an unvalidated destination if CRAWLORA_API_BASE is set.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is trusted; keep the API key scoped and disposable where possible.

Risk: The helper script is broader than the Shop.app workflow described by the skill.

Mitigation: Review commands before execution and restrict use to documented /shop-app GET endpoints unless a revised version narrows the helper.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/shop-app-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public Shop.app data exposed through documented Crawlora endpoints.]

## Skill Version(s):

1.0.7 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
