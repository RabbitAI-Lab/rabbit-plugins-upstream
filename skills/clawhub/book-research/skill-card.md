## Description:

Researches books, authors, and audiobooks via the Crawlora API across Goodreads, Apple Books, and Audible, returning clean JSON for ratings, reviews, bibliographies, curated lists, audiobook details, and charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research public book, author, review, list, chart, and audiobook data from Goodreads, Apple Books, and Audible through Crawlora. It is suited for answering questions about ratings, reviews, bibliographies, reading lists, audiobook availability, narrators, series, and popularity charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book, author, audiobook, review, list, chart, and related query parameters are sent to Crawlora along with the user's Crawlora API key.

Mitigation: Use this skill only when that third-party transmission is acceptable, and avoid sensitive private reading data.

Risk: The helper requires a Crawlora API key to access the service.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not hardcode or commit it, and rely on the helper's documented key-handling path.

## Reference(s):

- [book-research endpoint reference](reference/endpoints.md)
- [Crawlora skill page](https://clawhub.ai/crawlora-org/skills/book-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON, Guidance]

**Output Format:** [Markdown guidance with shell commands that call the Crawlora helper and return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends GET requests to documented Crawlora book, author, review, list, chart, and audiobook endpoints.]

## Skill Version(s):

1.0.19 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
