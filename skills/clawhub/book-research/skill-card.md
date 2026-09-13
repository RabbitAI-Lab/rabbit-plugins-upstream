## Description:

Researches books, authors, and audiobooks via the Crawlora API -- Goodreads (books, authors, reviews, lists, quotes), Apple Books (books, audiobooks, series, reviews, charts), and Audible (audiobook catalog search, product detail, narrators/series, reviews, charts, editorial lists) -- returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and reading-focused agents use this skill to look up public book, author, review, list, chart, and audiobook metadata across Goodreads, Apple Books, and Audible through the Crawlora API.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Book and audiobook lookup terms are sent to Crawlora with the configured API key.

Mitigation: Only send intended public lookup terms, and avoid secrets or private personal text in query parameters or JSON bodies unless that disclosure is intended.

Risk: The helper makes outbound requests to a third-party API and may consume Crawlora account credits.

Mitigation: Review commands before execution, set CRAWLORA_API_KEY only in the intended environment, and monitor Crawlora usage for unexpected calls.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/book-research)
- [Crawlora API key and service information](https://crawlora.net)

## Skill Output:

**Output Type(s):** [json, shell commands, configuration, guidance]

**Output Format:** [JSON API responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends user-requested lookup terms to the Crawlora API.]

## Skill Version(s):

1.0.16 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
