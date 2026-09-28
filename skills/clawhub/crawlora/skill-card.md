## Description:

Fetches structured public web data across search, commerce, social, finance, maps, media, and reviews through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Agents and developers use Crawlora to retrieve public website listings, prices, reviews, search results, transcripts, and other structured data without parsing HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Public-web queries, URLs, locations, and request bodies are sent to Crawlora together with an API key.

Mitigation: Keep the key in the environment and do not use the skill for private sites or account data.

Risk: Fetched data may be subject to source-site terms and rate limits.

Mitigation: Review applicable source-site terms before fetching or reusing data.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill listing](https://clawhub.ai/crawlora-org/skills/crawlora)

## Skill Output:

**Output Type(s):** [JSON, Text, Shell commands]

**Output Format:** [JSON API responses or Markdown summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; successful requests may consume credits.]

## Skill Version(s):

1.0.28 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
