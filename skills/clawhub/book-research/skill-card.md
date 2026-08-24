## Description:

Researches books, authors, and audiobooks through the Crawlora API across Goodreads, Apple Books, and Audible, returning normalized JSON for ratings, reviews, bibliographies, curated lists, and audiobook details.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to look up book, author, review, list, chart, and audiobook metadata from Goodreads, Apple Books, and Audible through Crawlora. It is suited for answering reading research questions, comparing print and audiobook editions, and gathering structured public catalog data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call Crawlora endpoints beyond the book-research endpoints.

Mitigation: Review agent actions before execution and prefer only the Goodreads, Apple Books, and Audible endpoints documented in reference/endpoints.md.

Risk: The helper accepts arbitrary request bodies for non-GET requests.

Mitigation: Inspect POST payloads before sending them and avoid submitting private, sensitive, or unnecessary user data.

Risk: Crawlora API usage requires an API key and may consume credits on successful requests.

Mitigation: Store the key only in CRAWLORA_API_KEY, do not commit it, and monitor credit usage.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/book-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and may consume Crawlora API credits on successful requests.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
