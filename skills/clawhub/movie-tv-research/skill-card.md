## Description:

Researches movies and TV shows - metadata, cast/crew, ratings, reviews, streaming availability, and box-office performance - via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research film and television titles, people, ratings, reviews, streaming availability, recommendations, and box-office performance through Crawlora API endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can send the user's Crawlora API key to an overrideable API base.

Mitigation: Use only in a trusted shell environment, avoid setting CRAWLORA_API_BASE, and prefer a release that hardcodes the Crawlora HTTPS base.

Risk: The helper script behavior is broader than the movie and TV purpose disclosed by the skill.

Mitigation: Restrict use to the documented movie and TV endpoints and avoid passing sensitive or unrelated user content through the helper.

## Reference(s):

- [movie-tv-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns paginated results where endpoint documentation notes pagination.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
