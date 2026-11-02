## Description:

Queries Crawlora's pre-built hosted datasets — Airbnb markets, App Store/Google Play apps, GitHub/Instagram/X users, job postings, US housing markets, Google Maps businesses, Goodreads, PitchBook, Steam, TrustMRR, Product Hunt, SEC companies, tech-stack, and more — via search/facets/item/nearby endpoints, returning clean JSON without live-crawling each platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to search Crawlora's periodically refreshed datasets for bulk, aggregate, filtered, and record lookup questions. It returns JSON results for research such as market analysis, hiring trends, and catalog discovery.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key and search parameters; live service behavior and provider data-retention practices were not verified.

Mitigation: Avoid confidential search text and review provider data-handling terms before sending sensitive information.

Risk: Bulk queries can consume API credits.

Mitigation: Set a credit budget and narrow filters or page sizes to the needed scope.

Risk: An exposed API key could be used to make requests on the account.

Mitigation: Keep the key in the CRAWLORA_API_KEY environment variable and never hardcode or commit it.

## Reference(s):

- [Crawlora Datasets endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Get a Crawlora API key](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Analysis]

**Output Format:** [JSON dataset records and aggregates, with concise text summaries as requested]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Paginated results; dataset freshness and available fields vary by source.]

## Skill Version(s):

1.0.26 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
