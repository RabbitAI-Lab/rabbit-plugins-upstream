## Description:

Researches books, authors, and audiobooks via the Crawlora API for Goodreads and Apple Books, returning clean JSON for ratings, reviews, bibliographies, reading lists, audiobook details, and charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up public book, author, review, list, quote, audiobook, series, and chart data from Goodreads and Apple Books through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included Crawlora API helper is broader than the stated Goodreads and Apple Books book-research purpose.

Mitigation: Limit use to the documented Goodreads and Apple Books endpoints unless a reviewer approves broader Crawlora API use.

Risk: Book, review, and catalog requests may send private or unrelated data through the API wrapper if prompts are not scoped.

Mitigation: Use public book and author queries only, and avoid passing private or unrelated data to the helper.

Risk: The skill requires a Crawlora API key.

Mitigation: Keep the key in CRAWLORA_API_KEY and do not hardcode, commit, or pass it as a query parameter.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and is intended for public Goodreads and Apple Books catalog and review data.]

## Skill Version(s):

1.0.1 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
