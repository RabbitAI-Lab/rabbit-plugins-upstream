## Description:

Retrieves public publisher headlines, articles, searches, live coverage, and section archives as JSON through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, journalists, and other users can find and read public, publisher-specific news coverage while retaining article URLs and publication times.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: News URLs, search terms, and the API key are sent to Crawlora.

Mitigation: Use only approved public research targets and an authorized API key; do not send secrets, personal data, internal URLs, or regulated information without approval.

Risk: Publisher feeds may be incomplete, challenged, or missing subscriber-only content.

Mitigation: Preserve source URLs and timestamps, identify partial results, and avoid presenting bounded feeds as complete coverage.

## Reference(s):

- [Publisher endpoint reference](reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/news-media-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Natural-language responses with links and timestamps; retrieved publisher data is JSON.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Coverage is limited to public, publisher-specific snapshots; full text may be partial or unavailable.]

## Skill Version(s):

1.0.14 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
