## Description:

Researches movie and TV metadata, cast, ratings, reviews, streaming availability, and box office through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People researching movies and TV shows use this skill to compare credits, ratings, reviews, streaming options, and box-office results across public sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie, TV, review, and streaming searches are sent to Crawlora; sensitive queries or exposed API keys may disclose private information.

Mitigation: Keep the API key in the environment and send only public, non-sensitive lookup terms; avoid secrets, confidential projects, and private watch-history analysis.

Risk: The endpoint catalog also contains public Metacritic game lookups outside the skill's main movie and TV purpose.

Mitigation: Limit requests to the movie and TV research task and review the chosen endpoint before sending a query.

## Reference(s):

- [Movie & TV research endpoint reference](reference/endpoints.md)
- [Movie & TV research on ClawHub](https://clawhub.ai/crawlora-org/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [Text, Guidance]

**Output Format:** [Markdown summaries informed by JSON lookup results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results depend on the selected public data sources and available Crawlora API credits.]

## Skill Version(s):

1.0.20 (source: server-resolved release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
