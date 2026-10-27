## Description:

Retrieves sports scores, standings, rosters, statistics, public sports media, and betting odds through Crawlora's sports-data API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Sports researchers, fans, and developers use this skill to answer questions about live scores, team and player performance, league news, public routes, and betting-odds snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports queries and public identifiers are sent to Crawlora with the user's API key.

Mitigation: Use only with an authorized API key and avoid confidential research targets.

Risk: Strava route and club lookups may reveal sensitive location patterns.

Mitigation: Limit lookups to the user's request and do not infer a person's home, routine, or location history.

## Reference(s):

- [Skill endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs)
- [ClawHub skill release](https://clawhub.ai/crawlora-org/skills/sports-scores-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands]

**Output Format:** [Markdown responses with sports data and optional shell examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Underlying sports-data responses are JSON; live scores reflect source update cadence.]

## Skill Version(s):

1.0.23 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
