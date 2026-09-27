## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Entertainment researchers and viewers use this skill to identify and compare movies and TV shows, examine cast and ratings, and check region-specific streaming offers.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and lookup parameters are sent to the third-party Crawlora API.

Mitigation: Do not submit private notes, unreleased project names, or sensitive URLs as search terms or lookup parameters.

Risk: Exposure of the Crawlora API key could allow unauthorized use.

Mitigation: Keep the key scoped and rotate it if exposed.

Risk: Streaming availability and review samples may be incomplete or change over time.

Mitigation: Record locale and retrieval time, distinguish score types, and treat missing coverage as unavailable rather than zero.

## Reference(s):

- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/entertainment-discovery-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Guidance]

**Output Format:** [Markdown research summaries with optional shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserves source title IDs, score definitions, locale, and retrieval time.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
