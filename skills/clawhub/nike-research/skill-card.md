## Description:

Researches Nike's catalog, including categories, search, product detail, colorways, reviews, and nearby stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to browse and search Nike product data, compare product variants and prices, summarize product reviews, and locate nearby Nike stores through Crawlora's Nike endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends Nike lookup inputs, including coordinates for store searches, to Crawlora.

Mitigation: Use the skill only when sharing those inputs with Crawlora is acceptable, and avoid sending unnecessary sensitive location details.

Risk: The skill requires a third-party Crawlora API key.

Mitigation: Provide the key through CRAWLORA_API_KEY only; do not hardcode, place it in command arguments, or commit it.

Risk: Keyword search results may include Nike fallback recommendations rather than a confirmed exact match.

Mitigation: Verify product identity with returned slug, style_color, title, price, and colorway details before making purchase-oriented recommendations.

## Reference(s):

- [Nike endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY from the environment and returns normalized public Nike catalog, review, availability, recommendation, suggestion, and store data.]

## Skill Version(s):

1.0.13 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
