## Description:

Researches movies and TV shows - metadata, cast/crew, ratings, reviews, streaming availability, and box-office performance - via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and entertainment-focused agents use this skill to answer movie and TV questions about titles, people, ratings, reviews, streaming availability, recommendations, and box-office performance using normalized Crawlora API responses.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The Crawlora helper can be repurposed beyond the declared movie/TV scope.

Mitigation: Use a restricted wrapper or endpoint allowlist that permits only the movie and TV endpoints needed for the task.

Risk: Movie and TV queries, identifiers, and API usage are sent to Crawlora with the user's API key.

Mitigation: Use a low-value key, keep it in CRAWLORA_API_KEY, monitor credit usage, and avoid exposing the key in prompts, URLs, or commits.

Risk: Custom API bases or non-movie/TV paths could route requests outside the expected data sources.

Mitigation: Disallow custom API bases in production wrappers and review requested paths before execution.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends movie/TV queries and identifiers to Crawlora endpoints.]

## Skill Version(s):

1.0.1 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
