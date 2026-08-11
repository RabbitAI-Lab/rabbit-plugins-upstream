## Description:

Researches Target's catalog - categories, products, filters, prices, questions, and reviews - using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to search or browse Target catalog results, compare prices and availability, and retrieve product details, questions, and reviews through Crawlora's normalized API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled API helper can call broader Crawlora endpoints than the advertised Target-only use case.

Mitigation: Review requested endpoint paths before execution and use the helper for Target endpoints only unless broader Crawlora API access is intentional.

Risk: Target searches, product identifiers, filters, and optional store IDs are sent to Crawlora.

Mitigation: Use the skill only when sharing those queries with Crawlora is acceptable, and avoid entering sensitive personal or proprietary information in searches.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Skill page](https://clawhub.ai/tonywangcn/skills/target-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses paginated Crawlora API responses; product, review, and question lookups are keyed by Target TCIN.]

## Skill Version(s):

1.0.0 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
