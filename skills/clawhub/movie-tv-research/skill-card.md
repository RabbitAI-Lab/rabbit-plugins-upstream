## Description:

Researches movies and TV shows, including metadata, cast and crew, ratings, reviews, streaming availability, and box-office performance, through the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and media analysts use this skill to look up public movie and TV metadata, ratings, reviews, streaming availability, similar titles, and box-office results from supported entertainment data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie, TV, and possibly Metacritic game lookup terms plus the Crawlora API key are sent to Crawlora.

Mitigation: Use the skill only for queries and credentials that are acceptable to share with the API provider; avoid confidential titles, private URLs, and sensitive internal research queries.

Risk: The helper includes minor off-scope Metacritic game endpoint coverage.

Mitigation: Use the skill for movie and TV research unless a game lookup is intentionally requested and approved for the same data-sharing posture.

Risk: Public media data can be partial, paginated, or dependent on upstream source availability.

Mitigation: Check pagination fields and corroborate high-impact claims before using results in published or decision-critical work.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples; helper calls return JSON from the Crawlora API.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET endpoints for public movie and TV data.]

## Skill Version(s):

1.0.18 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
