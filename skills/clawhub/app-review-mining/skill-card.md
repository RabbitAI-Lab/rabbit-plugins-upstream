## Description:

Mines App Store and Google Play app details, reviews, ratings, store rankings, and similar apps via the Crawlora API as clean JSON for mobile-app review and competitive ASO research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, product teams, and ASO researchers use this skill to retrieve public App Store and Google Play metadata, reviews, ratings, rankings, and similar-app lists for sentiment analysis, market comparison, and competitor tracking.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App IDs, search terms, locale choices, review-mining queries, and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when Crawlora's data handling is acceptable, avoid confidential competitive research terms, and keep the API key in CRAWLORA_API_KEY rather than in prompts, files, or command arguments.

Risk: Review and ranking data can vary by country, language, pagination, and storefront behavior.

Mitigation: Specify country and language parameters for market-specific work and document pagination choices when using results for analysis or comparisons.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell command examples that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to Crawlora for public App Store and Google Play data.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
