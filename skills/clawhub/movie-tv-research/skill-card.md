## Description:

Researches movies and TV shows through the Crawlora API, returning JSON on titles, cast and crew, ratings, reviews, streaming availability, and box-office performance across seven entertainment sources.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer movie and TV questions about credits, ratings, reviews, streaming options, similar titles, and box-office results using public entertainment data.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Entertainment queries, IDs, URLs, and the API key are sent to Crawlora.

Mitigation: Use public, nonsensitive lookup data; keep the key in the environment and never hardcode or commit it.

## Reference(s):

- [Skill release on ClawHub](https://clawhub.ai/crawlora-org/skills/movie-tv-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API and key access](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON]

**Output Format:** [JSON lookup results or concise text and Markdown answers]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; longer result lists may be paginated, and streaming offers depend on location.]

## Skill Version(s):

1.0.19 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
