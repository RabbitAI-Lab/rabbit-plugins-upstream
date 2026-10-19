## Description:

Researches books, authors, reviews, and audiobooks across Goodreads, Apple Books, and Audible through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Readers and researchers use this skill to find book ratings, reviews, author bibliographies, reading lists, and audiobook details and charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms sent to Crawlora may contain sensitive information.

Mitigation: Avoid submitting private or sensitive search terms to the external service.

Risk: The Crawlora API key could be exposed if stored in source files.

Mitigation: Keep CRAWLORA_API_KEY in the environment and never commit it.

## Reference(s):

- [Book research endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Text]

**Output Format:** [JSON catalog results and plain-language research summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Public catalog and review data; some results are paginated.]

## Skill Version(s):

1.0.20 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
