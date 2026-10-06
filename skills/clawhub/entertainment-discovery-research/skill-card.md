## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and researchers use this skill to discover and compare movies and TV shows, cast, reviews, ratings, and regional streaming options.

### Deployment Geography for Use:

Global; streaming availability depends on the requested country or locale.

## Known Risks and Mitigations:

Risk: Entertainment searches, IDs, URLs, and locale parameters are sent to Crawlora using a Crawlora API key.

Mitigation: Use only if comfortable sharing those inputs with Crawlora; avoid sensitive search terms and protect the API key.

Risk: Scores from different platforms and regional streaming offers can be misread as directly comparable or permanent.

Mitigation: Keep score definitions and counts separate, and report the source, locale, and retrieval time for each result.

Risk: The available read-only endpoints also include game reviews, beyond the movie and TV focus.

Mitigation: Keep requests within the user's intended entertainment research scope.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/entertainment-discovery-research)
- [Endpoint reference](reference/endpoints.md)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance, Shell commands]

**Output Format:** [Markdown research summaries with optional shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source-specific title IDs, score definitions, locale, and retrieval time.]

## Skill Version(s):

1.0.5 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
