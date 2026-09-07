## Description:

Researches Old Navy and Gap Inc. sibling storefront catalogs for categories, products, colors, sizes, local pickup availability, and reviews using the Crawlora API, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to search Old Navy, Gap, Banana Republic, and Athleta product data, inspect product details and reviews, and check nearby in-store pickup availability without scraping storefront HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can send the Crawlora API key to an arbitrary configured API host.

Mitigation: Use the default Crawlora API base, avoid setting CRAWLORA_API_BASE, and review the destination before executing API calls.

Risk: Retail searches, store or ZIP inputs, coordinate inputs, and the Crawlora API key are sent to Crawlora.

Mitigation: Install and use the skill only when sharing those inputs with Crawlora is acceptable.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/oldnavy-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY.]

## Skill Version(s):

1.0.6 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
