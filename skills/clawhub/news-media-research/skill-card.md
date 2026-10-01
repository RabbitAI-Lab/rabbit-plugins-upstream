## Description:

Retrieves public news headlines, article text, search results, live coverage, and section archives from major publishers through Crawlora.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Journalists, analysts, and researchers use this skill to find publisher-specific public news and retrieve article content with source URLs and timestamps.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, article URLs, and request metadata are sent to Crawlora.

Mitigation: Use only when third-party processing is acceptable; avoid confidential investigations or sensitive URLs.

Risk: Publisher feeds are snapshots and subscriber-only or challenged content may be missing or partial.

Mitigation: Keep original source links and timestamps, and do not present bounded results as exhaustive coverage.

## Reference(s):

- [News Media Research release](https://clawhub.ai/crawlora-org/skills/news-media-research)
- [Publisher endpoints reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown with source links; retrieved news records are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves publisher URLs and timestamps when available; results may be incomplete.]

## Skill Version(s):

1.0.12 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
