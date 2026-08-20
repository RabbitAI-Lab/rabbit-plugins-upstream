## Description:

Mines App Store and Google Play data via the Crawlora API — app details, reviews, ratings, store rankings, and similar apps — as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and ASO researchers use this skill to retrieve public App Store and Google Play details, reviews, ratings, rankings, privacy metadata, version history, and similar-app lists for mobile-app research and competitor tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper is broader than the stated app-review purpose and can call arbitrary Crawlora API paths and methods.

Mitigation: Use it only with trusted prompts, constrain calls to documented App Store and Google Play endpoints, and review commands before execution.

Risk: API parameters or request bodies could include sensitive data if a user provides it.

Mitigation: Avoid passing secrets or private data to Crawlora; keep the API key in CRAWLORA_API_KEY and never hardcode, query-parametrize, or commit it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; results depend on Crawlora API availability, store locale, pagination, and selected endpoint.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
