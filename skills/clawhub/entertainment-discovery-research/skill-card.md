## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API. Use for title discovery, cast and crew, ratings, critic and audience reviews, streaming offers, similar titles, and release comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers can research public entertainment listings, credits, ratings, reviews, and regional streaming offers, then compare results while preserving each source's identifiers and score definitions.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives research queries and the API key, and requests may consume API credits.

Mitigation: Use a dedicated API key, avoid private information in searches, and monitor credit usage.

Risk: The endpoint catalog supports public video-game research beyond the narrower movie and TV description.

Mitigation: Check the endpoint reference for supported content before relying on coverage.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [ClawHub release page](https://clawhub.ai/crawlora-org/skills/entertainment-discovery-research)

## Skill Output:

**Output Type(s):** [JSON, Text, Analysis, Guidance]

**Output Format:** [JSON API results summarized in text or Markdown]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserve source IDs, score definitions, locale, and retrieval time; do not treat scores from different platforms as interchangeable.]

## Skill Version(s):

1.0.7 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
