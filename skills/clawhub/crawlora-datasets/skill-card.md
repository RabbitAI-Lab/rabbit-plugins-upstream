## Description:

Queries Crawlora's hosted, pre-indexed datasets for search results, aggregate breakdowns, nearby records, and individual records without live-crawling each source platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to search public hosted datasets, compare populations with facets, and retrieve records for market and business research.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: API credentials or sensitive search parameters are sent to Crawlora.

Mitigation: Use the key only through CRAWLORA_API_KEY, keep it out of logs and repositories, and review queries before sending.

Risk: Contact-oriented dataset records could be misused for spam, harassment, or profiling.

Mitigation: Use contact-oriented results only for legitimate, compliant research.

Risk: Scheduled dataset refreshes may make results stale for time-sensitive decisions.

Mitigation: Check recency and verify important findings against current sources.

## Reference(s):

- [Crawlora datasets endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Text or Markdown summarizing JSON API results, with optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Dataset results are paginated and refreshed periodically rather than in real time.]

## Skill Version(s):

1.0.23 (source: server-resolved release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
