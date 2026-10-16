## Description:

Helps agents search live and sold eBay listings, inspect product details, and look up seller profiles through Scavio.

This skill is ready for commercial/non-commercial use.

## Publisher:

[scavio-ai](https://clawhub.ai/user/scavio-ai)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and resale researchers use this skill to find comparable sold prices, browse current listings, inspect product details, and check public seller profiles.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, item IDs, seller names, and API credentials are sent to Scavio; calls consume credits.

Mitigation: Use only with consent to send these details; store the API key in an environment variable or secret store, and monitor credit use.

Risk: Historical sold prices or unexpected search filters may mislead resale decisions.

Mitigation: Include sale dates and listing URLs when citing prices, and verify category filters and returned listings.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/scavio-ai/skills/ebay-product-data)
- [Scavio eBay search documentation](https://scavio.dev/docs/ebay-search?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay product documentation](https://scavio.dev/docs/ebay-product?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio eBay seller documentation](https://scavio.dev/docs/ebay-seller?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)
- [Scavio rate limits](https://scavio.dev/docs/rate-limits?utm_source=agent-skills&utm_medium=skill&utm_campaign=ebay-product-data)

## Skill Output:

**Output Type(s):** [Text, Markdown, Code, Shell commands, Guidance]

**Output Format:** [Natural-language guidance with optional code and commands based on structured JSON results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include listing URLs and reported prices or seller details; API calls consume Scavio credits.]

## Skill Version(s):

1.0.5 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
