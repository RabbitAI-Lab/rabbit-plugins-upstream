## Description:

Researches movies and TV shows across film and streaming data sources through the Crawlora API, returning title details, ratings, reviews, availability, and box-office figures.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

People and agents researching movies and TV shows use this skill to compare ratings and reviews, identify cast and crew, find streaming options, and check box-office results.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Movie and TV queries and the Crawlora API key are sent to an external service.

Mitigation: Use only if comfortable sharing these queries with Crawlora; keep CRAWLORA_API_KEY private and out of logs.

Risk: The endpoint catalog includes public-profile and game-review lookups beyond movie and TV research.

Mitigation: Limit requests to the intended research task and review requested endpoints before use.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/movie-tv-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [Text, Shell commands, Guidance]

**Output Format:** [Markdown guidance and shell commands; API responses are JSON]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key; responses may be paginated and successful requests may consume credits.]

## Skill Version(s):

1.0.21 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
