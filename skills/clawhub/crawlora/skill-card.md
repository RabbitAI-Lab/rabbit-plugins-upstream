## Description:

Fetches structured public web data via the Crawlora REST API across search, commerce, social, finance, maps, app stores, media, and reviews, returning clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve live public website data such as prices, listings, reviews, search results, transcripts, trends, finance data, and places without maintaining scrapers or parsing HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests send public-web lookup terms, URLs, IDs, and request bodies to Crawlora.

Mitigation: Use only for public web data and obtain explicit approval before submitting sensitive personal, regulated, internal, authenticated, or secret-bearing data.

Risk: Crawlora API credentials could be exposed if hardcoded, logged, committed, or placed in URLs.

Mitigation: Keep CRAWLORA_API_KEY in the environment or approved secret storage, avoid query-string secrets, and do not commit keys.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/crawlora)

## Skill Output:

**Output Type(s):** [API Calls, Shell commands, JSON, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; sends public-web lookup terms, URLs, IDs, and request bodies to Crawlora.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
