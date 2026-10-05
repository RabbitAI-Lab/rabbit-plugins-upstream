## Description:

Fetches structured public web data through the Crawlora REST API, returning JSON for searches, listings, reviews, transcripts, trends, and other public-web research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and their users fetch structured public website data for research, price comparisons, reviews, search results, and summaries without parsing HTML directly.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests share the Crawlora API key and requested public-web queries or URLs with Crawlora; sensitive parameters could disclose private information.

Mitigation: Keep the key in CRAWLORA_API_KEY and exclude secrets, private data, and sensitive personal information from request parameters unless you intend to share them with Crawlora.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora skill on ClawHub](https://clawhub.ai/crawlora-org/skills/crawlora)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Text, Markdown]

**Output Format:** [Structured JSON data and agent-written text or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected public-web endpoint and requested query or URL.]

## Skill Version(s):

1.0.35 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
