## Description:

Etsy店铺查询 helps agents filter and retrieve Etsy store data by sales, favorites, reviews, opening date, country, category, and Raving or star status.

This skill is ready for commercial/non-commercial use.

## Publisher:

[linkfox-ai](https://clawhub.ai/user/linkfox-ai)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query and compare Etsy shops through LinkFox's hosted data service, including filtering by activity, sales, review, favorite, geography, category, and status signals.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The security verdict is suspicious because the skill includes account login, API key generation, and payment-order flows in addition to Etsy store queries.

Mitigation: Install only when the user intends to use LinkFox's paid hosted service, and ask for explicit user confirmation before account setup, SMS-code handling, API-key configuration, or billing actions.

Risk: Queries consume paid credits based on returned store count and may incur higher-than-expected cost for broad or repeated searches.

Mitigation: Explain the dynamic credit rule before running broad queries, use scoped filters and pagination, and let the user decide whether to continue.

Risk: Endpoint override environment variables can redirect requests away from the default LinkFox services.

Mitigation: Use endpoint overrides only in trusted development environments and review them before executing authentication, billing, or query commands.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/linkfox-ai/skills/linkfox-etsy-store-query)
- [_ehunt_storeQuery API reference](artifact/references/api.md)
- [Authentication and billing onboarding](artifact/references/onboarding.md)
- [LinkFox tool gateway](https://tool-gateway.linkfox.com)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, files, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with JSON API responses and optional saved JSON files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [The query script may summarize large responses while saving the full response as a JSON data file.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
