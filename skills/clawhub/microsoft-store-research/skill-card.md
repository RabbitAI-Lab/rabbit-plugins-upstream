## Description:

Research Microsoft Store apps and games with Crawlora search, categories, charts, publisher listings, product details, and reviews to compare Windows apps and explore publishers, awards, and regional feedback.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, developers, and other users compare Microsoft Store apps and games, investigate publishers, and examine regional listings and review samples without installing or purchasing products.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when comfortable sharing those queries and the key with Crawlora; protect the key and keep requests scoped.

Risk: Unbounded searches and pagination may consume API credits.

Mitigation: Set a credit budget, bound pages and calls to the task, and monitor usage.

Risk: Regional prices, chart rankings, and small review samples may be mistaken for total cost, sales, or overall sentiment.

Mitigation: Record region, observation time, and sample coverage; distinguish ratings from sampled reviews and flag unanswered pricing questions.

## Reference(s):

- [Microsoft Store endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/microsoft-store-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Sourced Markdown comparison and review summary]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes source links, region and observation time, review sample size, and open pricing or compatibility questions.]

## Skill Version(s):

1.0.0 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
