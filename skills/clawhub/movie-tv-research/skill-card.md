## Description:

Researches movies and TV shows across IMDb, TMDB, JustWatch, Letterboxd, Rotten Tomatoes, Metacritic, and Box Office Mojo via the Crawlora API, returning normalized JSON for metadata, credits, ratings, reviews, streaming availability, and box-office analysis.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to answer movie and TV research questions about title identity, cast and crew, ratings, reviews, where to watch, recommendations, and box-office performance.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie and TV search terms, public URLs, identifiers, and account-linked usage are sent to Crawlora under the user's API key.

Mitigation: Use the skill only for queries acceptable to share with Crawlora and monitor credit usage when agents may call the helper automatically.

Risk: The endpoint catalog includes extra public entertainment capabilities beyond core movie and TV lookup, including game and Letterboxd member endpoints.

Mitigation: Review requested paths against the endpoint reference before enabling unattended or broad automated use.

## Reference(s):

- [movie-tv-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/movie-tv-research)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API calls consume Crawlora credits on successful responses.]

## Skill Version(s):

1.0.16 (source: release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
