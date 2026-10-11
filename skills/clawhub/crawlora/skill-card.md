## Description:

Fetches structured public web data through the Crawlora REST API as JSON across search, shopping, social, finance, maps, apps, media, and reviews.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to retrieve public web listings, search results, reviews, transcripts, trends, and market data without parsing website HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-web queries, URLs, and locations are sent to Crawlora.

Mitigation: Use only for public information; do not submit confidential internal data or personal secrets.

Risk: The Crawlora API key could be exposed if handled carelessly.

Mitigation: Keep CRAWLORA_API_KEY private in the environment; do not embed it in URLs or shared output.

Risk: Public source websites may impose terms and rate limits.

Mitigation: Respect each source site's terms and rate limits.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora](https://crawlora.net)
- [Crawlora skill on ClawHub](https://clawhub.ai/crawlora-org/skills/crawlora)

## Skill Output:

**Output Type(s):** [JSON data, Text summaries, Shell commands]

**Output Format:** [JSON responses and Markdown guidance with shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; some results are paginated.]

## Skill Version(s):

1.0.37 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
