## Description:

Researches books, authors, reviews, lists, quotes, audiobooks, and Apple Books charts through Crawlora API endpoints for Goodreads and Apple Books, returning normalized JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to look up public book and audiobook metadata, ratings, reviews, author bibliographies, curated lists, quotes, similar titles, and Apple Books charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call arbitrary Crawlora API paths and methods, which is broader than the documented Goodreads and Apple Books research use case.

Mitigation: Review requested paths and methods before execution and constrain use to documented Goodreads and Apple Books endpoints where possible.

Risk: Query parameters and POST bodies are sent to the Crawlora API.

Mitigation: Do not pass private text, secrets, credentials, or sensitive identifiers as query parameters or POST bodies; keep the API key only in CRAWLORA_API_KEY.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance, API Calls]

**Output Format:** [JSON responses with Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; uses public Goodreads and Apple Books catalog and review data.]

## Skill Version(s):

1.0.2 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
