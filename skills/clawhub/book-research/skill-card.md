## Description:

Researches books, authors, and audiobooks via the Crawlora API across Goodreads, Apple Books, and Audible, returning normalized JSON for ratings, reviews, bibliographies, lists, audiobook details, and charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up public book, author, review, list, chart, and audiobook catalog data through Crawlora. It is useful for answering reading research questions, comparing print and audiobook availability, and retrieving normalized metadata from Goodreads, Apple Books, and Audible.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book and audiobook search terms and the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only when that provider relationship is acceptable, avoid private or sensitive search terms, and keep the key in CRAWLORA_API_KEY rather than hardcoding it.

Risk: API calls may consume Crawlora credits and return only public catalog or review data available through the supported sources.

Mitigation: Review planned queries before execution, monitor account usage, and rely on the documented endpoint reference for supported routes and pagination.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/book-research)
- [ClawHub publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [json, shell commands, configuration, guidance]

**Output Format:** [JSON from Crawlora API responses, usually accompanied by concise Markdown guidance and shell command examples.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses a documented GET-only route catalog.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
