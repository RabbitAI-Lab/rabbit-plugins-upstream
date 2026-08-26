## Description:

Researches products, variants, shops, and reviews on Shop.app using the Crawlora API, returning clean JSON for cross-store product and merchant research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External developers, analysts, and shopping research agents use this skill to search Shop.app products, compare merchant offerings, inspect variants and availability, pull public reviews, and produce market snapshots from Crawlora API results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora helper can use the configured API key against arbitrary Crawlora API paths and can send arbitrary JSON request bodies.

Mitigation: Use the skill only for Shop.app research, avoid untrusted prompts, keep CRAWLORA_API_KEY out of code and logs, and prefer a wrapper or revised helper that allowlists /shop-app endpoints.

## Reference(s):

- [Shop.app endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/shop-app-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; the helper prints raw JSON to stdout.]

## Skill Version(s):

1.0.4 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
