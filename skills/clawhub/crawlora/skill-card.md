## Description:

Fetches structured public web data through Crawlora's hosted API for search, bounded crawls, and research jobs using a user-provided API key.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and other users can have agents retrieve public prices, listings, reviews, transcripts, search results, trends, financial data, and places through Crawlora. The skill also supports bounded web crawls and longer-running research jobs.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Successful requests may consume account credits, and crawl or research jobs can continue after the initial request.

Mitigation: Review the source scope and credit limit before starting a job; set a crawl credit cap, monitor progress, and cancel jobs no longer needed.

Risk: The API key or sensitive private data could be exposed in requests or logs.

Mitigation: Keep CRAWLORA_API_KEY private, do not include it in URLs or shared outputs, and avoid sending sensitive private data in request bodies.

## Reference(s):

- [Crawlora endpoint catalog](reference/catalog.md)
- [Crawlora skill on ClawHub](https://clawhub.ai/crawlora-org/skills/crawlora)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown answers based on structured JSON API results, with optional shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a user-provided Crawlora API key; successful requests may consume credits.]

## Skill Version(s):

1.0.40 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
