## Description:

Researches secondhand, resale, and handmade marketplaces via the Crawlora API, including Poshmark, Etsy, Vinted, StockX, Mercari, Depop, Whatnot, GOAT, and Leboncoin, returning clean JSON for listing, seller, shop, and price research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, agents, and marketplace researchers use this skill to find and compare public resale, secondhand, streetwear, sneaker, handmade, and vintage listings. It also supports seller, shop, product, livestream, release, taxonomy, and pricing lookups through the documented Crawlora API routes.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Marketplace searches, listing URLs or IDs, and the Crawlora API key header are sent to Crawlora.

Mitigation: Install only when that data sharing is acceptable, keep calls within the user's requested marketplace scope, and avoid unnecessary queries.

Risk: The Crawlora API key could be exposed if copied into prompts, committed to files, or passed directly on a command line.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not commit it, and use the provided helper so the key is supplied through a private curl config.

Risk: Successful API calls can consume Crawlora credits.

Mitigation: Confirm the target marketplace and endpoint before running requests, especially for GOAT and Leboncoin calls that the artifact notes can consume credits.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/resale-secondhand-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public marketplace data from documented Crawlora routes.]

## Skill Version(s):

1.0.17 (source: server release evidence, created 2026-09-14)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
