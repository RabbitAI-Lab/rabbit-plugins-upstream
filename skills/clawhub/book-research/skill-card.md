## Description:

Researches books, authors, and audiobooks via the Crawlora API across Goodreads, Apple Books, and Audible, returning clean JSON for ratings, reviews, bibliographies, reading lists, audiobook details, and charts.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to research books, authors, reviews, curated lists, and audiobook metadata through the Crawlora API. It is useful when a user asks for ratings, bibliography details, reading recommendations, narrator information, series data, or current Apple Books and Audible charts.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can call broader Crawlora API paths than the book-focused skill purpose.

Mitigation: Review or constrain the helper before deployment so it only reaches the documented Goodreads, Apple Books, and Audible endpoints needed for the intended workflow.

Risk: An untrusted CRAWLORA_API_BASE value could redirect requests and expose the Crawlora API key.

Mitigation: Use the default Crawlora API base or a trusted allowlisted base, and run the skill with a dedicated low-privilege Crawlora key.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs depend on Crawlora API responses and may require pagination for full review or list coverage.]

## Skill Version(s):

1.0.9 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
