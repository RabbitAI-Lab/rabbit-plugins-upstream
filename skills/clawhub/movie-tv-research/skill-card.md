## Description:

Researches movies and TV shows, including metadata, cast and crew, ratings, reviews, streaming availability, and box-office performance, via Crawlora API sources including IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, employees, and developers use this skill to answer movie and TV research questions about cast and crew, ratings, reviews, streaming availability, similar titles, and box-office performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call unrelated Crawlora endpoints with arbitrary request bodies, so it is broader than a tightly constrained movie-only tool.

Mitigation: Restrict use to the documented movie and TV research endpoints, and review requested paths and request bodies before execution.

Risk: Movie, TV, review, streaming, and box-office queries are sent to Crawlora using the user's Crawlora API key.

Mitigation: Do not pass secrets, private account data, or unrelated JSON bodies through the helper, and keep the API key in CRAWLORA_API_KEY rather than hardcoding it.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [Text, Markdown, JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses and Markdown guidance with shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public movie, TV, review, streaming, and box-office data from Crawlora-backed sources.]

## Skill Version(s):

1.0.2 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
