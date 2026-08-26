## Description:

Researches movies and TV shows - metadata, cast/crew, ratings, reviews, streaming availability, and box-office performance - via the Crawlora API across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research films and television titles, including credits, ratings, reviews, streaming availability, recommendations, and box-office performance. It is suited to title lookups and comparative entertainment research that can be answered through Crawlora's movie and TV endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The included API script is broader than the movie and TV use case and can call unrelated Crawlora endpoints with arbitrary methods and request bodies.

Mitigation: Review the skill before installing in sensitive sessions and limit use of scripts/crawlora.sh to the documented entertainment endpoints.

Risk: The skill requires a Crawlora API key and can make external API calls.

Mitigation: Keep the key in CRAWLORA_API_KEY only, avoid committing secrets, and review outbound API usage before deployment.

## Reference(s):

- [Endpoint Reference](artifact/reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for API calls; API results are returned as JSON.]

## Skill Version(s):

1.0.5 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
