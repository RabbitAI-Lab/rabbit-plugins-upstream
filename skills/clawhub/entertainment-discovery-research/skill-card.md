## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API. Use for title discovery, cast and crew, ratings, critic and audience reviews, streaming offers, similar titles, and release comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and entertainment researchers use this skill to identify and compare movies, TV shows, people, ratings, reviews, streaming offers, similar titles, and release details across public entertainment sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Entertainment queries, public title URLs, platform IDs, and API usage are sent to Crawlora.

Mitigation: Use only when that third-party service and account boundary are acceptable, and avoid submitting secrets, private URLs, personal data, or proprietary research terms.

Risk: Streaming availability and provider offers can change by country, date, plan, and provider.

Mitigation: Record the requested locale and retrieval time, and treat offer data as a point-in-time snapshot.

Risk: Ratings and review scores from different platforms use different definitions and denominators.

Mitigation: Keep critic scores, audience scores, star ratings, review counts, and source IDs separate unless definitions are explicitly preserved.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API Base](https://api.crawlora.net/api/v1)
- [ClawHub Skill Page](https://clawhub.ai/crawlora-org/skills/entertainment-discovery-research)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses when commands are run]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Results should preserve source IDs, score definitions, locale, and retrieval time; streaming offers are snapshots that vary by country, plan, provider, and date.]

## Skill Version(s):

1.0.0 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
