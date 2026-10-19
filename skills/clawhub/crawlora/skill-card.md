## Description:

Retrieves structured public-web data through Crawlora's hosted API for searches, bounded crawls, and research jobs.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and researchers use this skill to retrieve public-web prices, listings, reviews, transcripts, search results, trends, financial data, and places without building a scraper.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms, URLs, addresses, coordinates, and other request parameters are sent to Crawlora's hosted API.

Mitigation: Avoid secrets and unnecessary personal data; share only inputs needed for the request.

Risk: Successful requests may consume credits, and crawl or research jobs may continue after the initial call.

Mitigation: Confirm source scope, credit limits, and ongoing job behavior before starting a job.

## Reference(s):

- [Crawlora skill release](https://clawhub.ai/crawlora-org/skills/crawlora)
- [Crawlora website](https://crawlora.net)
- [Endpoint catalog](artifact/reference/catalog.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown with structured data summaries and optional shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Can summarize JSON results returned by Crawlora.]

## Skill Version(s):

1.0.42 (source: server-resolved release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
