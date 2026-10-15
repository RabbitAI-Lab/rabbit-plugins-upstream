## Description:

Retrieves sports scores, standings, rosters, statistics, public sports media, routes, and betting odds through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports researchers and fans use this skill to answer questions about live games, player and team statistics, public sports coverage, routes, and odds using Crawlora's sports-data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports queries, public identifiers, route and club lookups, and the Crawlora API key are sent to a third party.

Mitigation: Use only if comfortable sharing these details with Crawlora; keep the API key secret and exclude confidential research targets and other secrets from requests.

Risk: Public Strava routes and club information can expose location-sensitive patterns.

Mitigation: Avoid sensitive personal location research and do not infer someone's home, routine, or location history from route or club data.

## Reference(s):

- [Sports Scores Research on ClawHub](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Crawlora endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Plain text or Markdown summary of retrieved sports data]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [May include scores, statistics, citations to public sports sources, routes, and informational odds.]

## Skill Version(s):

1.0.22 (source: ClawHub release)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
