## Description:

Researches secondhand, resale, and handmade marketplaces via the Crawlora API — Poshmark, Etsy, Vinted, StockX, Mercari, Depop, Whatnot, GOAT, and Leboncoin — returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public resale, secondhand, streetwear, and handmade marketplace listings, seller storefronts, and price signals across supported platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace search terms, listing IDs, seller names, and supplied public listing URLs are sent to Crawlora with the user's Crawlora API key.

Mitigation: Keep requests user-directed, use the environment variable for the API key, and avoid private account pages or sensitive personal data.

Risk: Unsupported or unrelated Crawlora routes could expose data outside the intended marketplace research scope.

Mitigation: Use the bundled helper's documented GET-only route catalog and reject paths outside the supported marketplace endpoints.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/resale-secondhand-research)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with inline shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET routes for supported marketplaces.]

## Skill Version(s):

1.0.18 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
