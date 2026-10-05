## Description:

Retrieves public publisher headlines, articles, search results, and live coverage through the Crawlora API for source-specific news research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers, journalists, and other users retrieve source-specific public news coverage, article text, and publisher timestamps without scraping publisher sites directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries and article URLs are sent to Crawlora using the user's API key.

Mitigation: Avoid confidential URLs, secrets, regulated data, and sensitive investigation topics; use only when sharing them with Crawlora is acceptable.

Risk: Publisher feeds may be incomplete, and subscriber-only or challenged articles may be unavailable or partial.

Mitigation: Keep source links and timestamps, report retrieval gaps, and do not present bounded results as exhaustive coverage.

## Reference(s):

- [Publisher endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/news-media-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Source-linked text or Markdown grounded in JSON news results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserve article URLs and publication or update times; feeds and live pages are bounded snapshots.]

## Skill Version(s):

1.0.13 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
