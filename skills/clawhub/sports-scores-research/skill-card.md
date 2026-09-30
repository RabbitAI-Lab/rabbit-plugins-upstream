## Description:

Retrieves live sports scores, standings, rosters, statistics, match details, odds, and public endurance-sport information through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research current games, teams, players, league standings, sportsbook odds, and public routes or clubs across supported sports-data sources.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports-query parameters and the Crawlora API key are sent to Crawlora when making requests.

Mitigation: Use the skill only if this data sharing is acceptable; keep the API key in the environment and never include it in prompts, URLs, or committed files.

Risk: Live scores may lag source updates, and sportsbook odds can change quickly.

Mitigation: Check timestamps and refresh time-sensitive results; treat odds as information, not betting advice.

Risk: Cricinfo cricket routes are available but omitted from the main skill description.

Mitigation: Consult the endpoint reference before assuming the main description lists every available sports-data source.

## Reference(s):

- [Sports Scores Research on ClawHub](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora API documentation](https://crawlora.net/docs)

## Skill Output:

**Output Type(s):** [Text, Markdown, Guidance]

**Output Format:** [Markdown summaries of JSON sports-data responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Live data freshness depends on upstream updates; available routes also include Cricinfo cricket data.]

## Skill Version(s):

1.0.18 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
