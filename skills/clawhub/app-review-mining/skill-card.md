## Description:

Mines App Store and Google Play data via the Crawlora API - app details, reviews, ratings, store rankings, and similar apps - as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and ASO teams use this skill to retrieve public App Store and Google Play app metadata, reviews, ratings, rankings, and similar-app data for review mining, sentiment analysis, competitor tracking, and store-ranking research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: App lookup terms, app IDs, request bodies, and authenticated requests are sent to Crawlora.

Mitigation: Use the skill only for data you are comfortable sending to Crawlora and keep CRAWLORA_API_KEY private.

Risk: API usage can consume Crawlora account credits.

Mitigation: Monitor credit usage and scope review, ranking, and pagination requests to the needed apps, countries, languages, and pages.

Risk: Reviews and rankings are locale-sensitive and paginated, so incomplete parameters can produce partial or misleading analysis.

Mitigation: Specify country, language, and pagination parameters when comparing apps or summarizing review themes.

Risk: Untrusted raw path segments can be unsafe until curl globbing is hardened.

Mitigation: Use documented routes and trusted identifiers; avoid passing untrusted raw path segments to the helper.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/app-review-mining)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from Crawlora API endpoints.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on Crawlora API responses, available account credits, selected store, pagination, country, language, and endpoint parameters.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
