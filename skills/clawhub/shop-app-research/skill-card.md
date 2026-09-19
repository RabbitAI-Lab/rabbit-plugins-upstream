## Description:

Researches public Shop.app products, variants, shops, and reviews through the Crawlora API and returns normalized JSON for cross-store product and merchant research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Shop.app, compare public product and merchant offerings, inspect variants and availability, and retrieve public reviews without scraping Shop.app pages.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Shop.app research inputs and lookup identifiers are sent to Crawlora with a Crawlora API key.

Mitigation: Use the skill only when that external data flow is acceptable, and avoid confidential buying plans, private merchant research, and secrets.

Risk: API credential exposure could occur if the Crawlora key is hardcoded, passed in URLs, or committed.

Mitigation: Keep the key in CRAWLORA_API_KEY only, and rely on the helper's credential-safe curl configuration instead of embedding the key in commands or files.

Risk: Results are bounded by endpoint limits and reflect public Shop.app data available through Crawlora.

Mitigation: Use documented limit parameters and verify important product, price, availability, or merchant conclusions before relying on them.

## Reference(s):

- [Shop.app endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands; helper calls return JSON from Crawlora.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET-only Shop.app API routes.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
