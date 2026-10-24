## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Researchers and entertainment fans use this skill to discover and compare movie and TV titles, cast, ratings, reviews, and regional streaming availability across public sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Entertainment search terms, title IDs, and supported public platform URLs are sent to Crawlora under the user's API key.

Mitigation: Use only public entertainment queries; do not provide private or internal URLs, secrets, or personal data.

Risk: The available Metacritic endpoints include games, beyond the movie and TV focus of the description.

Mitigation: Review requested endpoints and limit use to the intended entertainment research scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/entertainment-discovery-research)
- [Supported entertainment endpoints](artifact/reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Text or Markdown research summaries; helper commands return JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source title IDs, score definitions, locale, and retrieval time when comparing results.]

## Skill Version(s):

1.0.6 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
