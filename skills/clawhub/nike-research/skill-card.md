## Description:

Researches Nike's catalog, including categories, search, product detail, colorways, reviews, and nearby stores, using the Crawlora API and returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to query Crawlora's Nike endpoints for catalog browsing, product comparison, review summaries, and nearby store lookup without scraping nike.com.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call endpoints outside the Nike-specific use case when given arbitrary paths.

Mitigation: Use the helper only with the documented Nike endpoints or constrain allowed paths before delegating execution.

Risk: The skill requires a Crawlora API key for live requests.

Mitigation: Use a dedicated key, keep it in CRAWLORA_API_KEY, and do not hardcode, log, or commit it.

Risk: Store lookup can send precise coordinates to the Crawlora API.

Mitigation: Send precise latitude and longitude only when location-specific store results are necessary.

## Reference(s):

- [nike-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, API Calls, JSON]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live API calls.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
