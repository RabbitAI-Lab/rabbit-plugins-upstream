## Description:

Researches movies and TV shows: metadata, cast and crew, ratings, reviews, streaming availability, and box-office performance via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and agents use this skill to look up movie and TV title metadata, credits, ratings, reviews, streaming availability, recommendations, and box-office performance from normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie and TV search terms, title IDs, URLs, and the configured Crawlora API key are sent to Crawlora.

Mitigation: Use a dedicated Crawlora API key, avoid sensitive queries, and install only in environments where sending those requests to Crawlora is acceptable.

Risk: The helper exposes some documented routes beyond the main movie and TV description, including Metacritic game and Letterboxd member-profile endpoints.

Mitigation: Review route usage against the endpoint reference and limit calls to the routes needed for the user's task.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/movie-tv-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses documented GET endpoints through scripts/crawlora.sh.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
