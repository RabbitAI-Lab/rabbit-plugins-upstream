## Description:

Researches movies and TV shows — metadata, cast/crew, ratings, reviews, streaming availability, and box-office performance — via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON. Use when the user asks about a title's cast, ratings/scores, where to stream it, critic or user reviews, or its box-office numbers.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Users can research a movie or TV title's metadata, credits, ratings and reviews, streaming availability, and box-office performance across the supported services.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Queries are sent to Crawlora and calls may consume credits; the remote service itself was not audited.

Mitigation: Use a dedicated Crawlora key, keep private information out of queries, and account for credit use.

## Reference(s):

- [Crawlora API](https://api.crawlora.net/api/v1)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub release](https://clawhub.ai/crawlora-org/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [JSON]

**Output Format:** [JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Normalized title, cast and crew, ratings and reviews, streaming offers, and box-office data.]

## Skill Version(s):

1.0.22 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
