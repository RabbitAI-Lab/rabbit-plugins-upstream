## Description:

Mines App Store and Google Play data via the Crawlora API - app details, reviews, ratings, store rankings, and similar apps - as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and product teams use this skill to retrieve public mobile app metadata, reviews, ratings, rankings, privacy details, and similar-app lists for app review mining and app store optimization research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The skill sends app identifiers, search terms, locale parameters, and the Crawlora API key to Crawlora.

Mitigation: Install only when this data sharing is acceptable, keep CRAWLORA_API_KEY in the environment, and never commit the key.

Risk: Review and ranking results are paginated and locale-specific, so incomplete country, language, or page parameters can produce incomplete analysis.

Mitigation: Use explicit country, language, pagination, and result-count parameters when coverage matters.

Risk: The skill works with public app store data that may be subject to Apple or Google terms.

Mitigation: Use outputs for public-data research workflows and review downstream usage against applicable store terms.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API service](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends app identifiers, search terms, locale parameters, and the API key to Crawlora.]

## Skill Version(s):

1.0.17 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
