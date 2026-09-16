## Description:

Fetches structured public web data via the Crawlora REST API, covering search engines, e-commerce, social, finance, maps, app stores, media, and reviews, and returns clean JSON instead of HTML.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use Crawlora to retrieve live structured data from public websites for product research, search results, reviews, transcripts, trends, finance, places, and other tasks that would otherwise require scraping or parsing HTML.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests, selected public-data lookup parameters, and the configured Crawlora API key are sent to Crawlora's hosted API.

Mitigation: Use the skill only for public-data lookups intended for Crawlora, and avoid sensitive personal, regulated, or private data unless that transfer is intentional.

Risk: The Crawlora API key could be exposed if it is hardcoded, placed in a URL, or committed.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode it, pass it in query parameters, or store it in source files.

Risk: Live public-web endpoints can return upstream errors, throttling, empty results, or stale data.

Mitigation: Check API responses before relying on them, retry when appropriate, and use another documented provider when the catalog or response suggests a fallback.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora website](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/crawlora)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requests to Crawlora's hosted API.]

## Skill Version(s):

1.0.22 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
