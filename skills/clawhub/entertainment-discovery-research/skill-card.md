## Description:

Researches movies and TV titles across IMDb, TMDB, JustWatch, Rotten Tomatoes, and Metacritic using the Crawlora API for title discovery, cast and crew, ratings, reviews, streaming offers, similar titles, and release comparisons.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, researchers, and entertainment analysts use this skill to discover and compare movie and TV metadata, credits, ratings, reviews, streaming availability, similar titles, and release details across public entertainment sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Entertainment search terms, title IDs, and supplied entertainment URLs are sent to Crawlora with the user's Crawlora API key.

Mitigation: Use only entertainment research inputs you intend to send to Crawlora, and do not include private identifiers, secrets, or unrelated personal data in queries or URLs.

Risk: Streaming offers, ratings, reviews, and popularity signals can vary by country, date, plan, provider, and source-specific score definition.

Mitigation: Record the requested locale and retrieval time, preserve each platform's IDs and score definitions, and avoid averaging cross-platform scores unless denominators are explicitly preserved.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/entertainment-discovery-research)

## Skill Output:

**Output Type(s):** [Guidance, Shell commands, Markdown, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Preserve source IDs, score definitions, locale, and retrieval time when reporting results.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
