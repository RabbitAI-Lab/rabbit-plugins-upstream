## Description:

Researches public Shop.app products, variants, merchants, and reviews through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Shoppers, researchers, and developers use this skill to compare public Shop.app listings, examine product options and reviews, and browse merchant catalogs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Research queries and the Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated key in CRAWLORA_API_KEY and avoid private or sensitive information in queries.

Risk: Result limits may omit relevant listings or reviews.

Mitigation: Treat market snapshots as bounded samples rather than exhaustive coverage.

## Reference(s):

- [Shop App Research on ClawHub](https://clawhub.ai/crawlora-org/skills/shop-app-research)
- [Shop.app endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Text]

**Output Format:** [Markdown guidance and shell commands; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public Shop.app results; endpoint-specific result limits apply]

## Skill Version(s):

1.0.16 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
