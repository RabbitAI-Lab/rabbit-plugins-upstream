## Description:

Compares short-term rental market supply, listing density, room mix, price distributions, and review signals using Crawlora Airbnb aggregates and selected live listings while preserving sampling and freshness limits.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External analysts, developers, and market researchers use this skill to assemble comparable short-term rental market panels from Crawlora Airbnb aggregate data. It is suited to market comparison and scoping work, not occupancy, revenue, legal-permissibility, or investment-return claims.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an API base selected by CRAWLORA_API_BASE.

Mitigation: Before use, ensure CRAWLORA_API_BASE is unset or points only to https://api.crawlora.net/api/v1, and keep the Crawlora key scoped and rotatable where possible.

Risk: Market research queries and live listing examples may include sensitive private research intent or location details.

Mitigation: Do not pass sensitive private data in queries, and keep live listing examples separate from aggregate market statistics.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/short-term-rental-market-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown market comparison with optional shell command examples and source IDs or URLs]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes geography, filter scope, observed supply, density context, room and property mix where available, price basis, review signals, collection dates, and suppression or enrichment limitations.]

## Skill Version(s):

1.0.0 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
