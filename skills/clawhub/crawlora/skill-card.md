## Description:

Fetches structured public web data from search engines, marketplaces, social platforms, finance sites, maps, app stores, media, and reviews through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can retrieve and summarize structured public web information such as product listings, search results, reviews, transcripts, and financial data without parsing website HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requested URLs, queries, parameters, and JSON bodies are sent to Crawlora under the user's API key.

Mitigation: Use only public, nonsensitive requests; avoid private, intranet, account-only, or sensitive URLs.

Risk: Crawl and research-job endpoints can start durable remote work and consume credits despite the skill's stated exclusion of generic scraping.

Mitigation: Require explicit confirmation before calling /web/crawl or /research/jobs.

## Reference(s):

- [Crawlora endpoint catalog](artifact/reference/catalog.md)
- [Crawlora skill release](https://clawhub.ai/crawlora-org/skills/crawlora)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Guidance]

**Output Format:** [Markdown responses and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [API access requires a Crawlora key; results may be paginated and successful requests may consume credits.]

## Skill Version(s):

1.0.38 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
