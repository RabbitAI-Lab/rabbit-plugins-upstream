## Description:

Queries Crawlora's hosted datasets for searches, aggregate breakdowns, nearby records, and record lookups without live-crawling each source platform.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to search, filter, aggregate, and retrieve records from Crawlora's pre-indexed public datasets, including jobs, apps, businesses, and housing markets.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Dataset searches, filters, record IDs, and supplied coordinates are sent to Crawlora.

Mitigation: Avoid sensitive private queries and share location coordinates only when appropriate.

Risk: The Crawlora API key could be exposed if embedded in commands or committed to source control.

Mitigation: Keep CRAWLORA_API_KEY in environment or secret storage; do not place it in URLs or files shared with others.

Risk: Scheduled dataset refreshes may leave results out of date for time-sensitive questions.

Mitigation: Check recency before relying on results, and use a live source when current data is required.

## Reference(s):

- [Crawlora datasets endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/crawlora-datasets)

## Skill Output:

**Output Type(s):** [Text, Guidance, Shell commands]

**Output Format:** [Markdown guidance and shell examples; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Search results may be paginated; datasets refresh periodically rather than in real time.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
