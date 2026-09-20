## Description:

General-purpose web-intelligence utilities via the Crawlora API: scrape URLs to clean markdown or HTML, extract schema-conforming JSON from pages, fingerprint site technology, geocode addresses, compare cost of living, look up trade records, check site traffic, and resolve brand identity from domains.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and agents use this skill for one-off public web research and utility lookups through Crawlora, including scraping, structured extraction, geocoding, cost comparisons, trade-record lookups, traffic checks, and brand resolution.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests transmit lookup inputs and target URLs to Crawlora as a third-party provider.

Mitigation: Use the skill only for public web research and avoid submitting secrets, private or internal URLs, unpublished investigation targets, or sensitive personal data.

Risk: Scraped pages and third-party datasets may be incomplete, stale, or subject to source terms and robots directives.

Mitigation: Verify important findings against authoritative sources and respect each target site's terms of use before acting on results.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API docs](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends requested public web, domain, geocoding, or company lookup inputs to Crawlora.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
