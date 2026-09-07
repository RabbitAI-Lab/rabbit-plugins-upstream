## Description:

Researches books, authors, reviews, reading lists, and audiobooks through the Crawlora API for Goodreads, Apple Books, and Audible, returning clean JSON for agent use.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Readers, researchers, authors, and agent developers use this skill to look up book metadata, author bibliographies, public reviews, curated reading lists, audiobook availability, narrators, series, and current charts across supported book platforms.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script is broader than the stated book-research purpose and can send a Crawlora API key to API routes outside the documented Goodreads, Apple Books, and Audible scope.

Mitigation: Allowlist only the documented book and audiobook routes before use, and avoid changing the API base unless the destination is explicitly trusted.

Risk: The skill requires a Crawlora API key and relies on the agent to keep credentials out of committed files, query parameters, and logs.

Mitigation: Provide the key only through CRAWLORA_API_KEY, review generated commands before execution, and remove secrets from any shared transcripts or artifacts.

## Reference(s):

- [Book Research Endpoint Reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/book-research)
- [Publisher Profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses CRAWLORA_API_KEY and Crawlora book, author, review, list, chart, and audiobook endpoints.]

## Skill Version(s):

1.0.8 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
