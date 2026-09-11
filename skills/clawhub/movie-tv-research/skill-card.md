## Description:

Researches movies and TV shows for metadata, cast and crew, ratings, reviews, streaming availability, and box-office performance via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer movie and TV research questions about title identity, cast and crew, scores, reviews, streaming availability, similar titles, and box-office performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie or TV search terms, selected IDs or URLs, and the Crawlora API key are sent to Crawlora.

Mitigation: Use this skill only when that data sharing is acceptable, keep the key in CRAWLORA_API_KEY, and do not hardcode or commit the key.

Risk: The endpoint catalog includes a few broader public-data endpoints, including Metacritic games and Letterboxd member profiles.

Mitigation: Keep use scoped to the intended movie and TV research tasks and review selected endpoints before execution.

Risk: Public-data responses may be paginated, partial, or limited by upstream source availability.

Mitigation: Check pagination and partial-response fields before relying on results for comparisons, charts, or summaries.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY in the environment; API calls return public movie, TV, review, streaming, and box-office data.]

## Skill Version(s):

1.0.15 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
