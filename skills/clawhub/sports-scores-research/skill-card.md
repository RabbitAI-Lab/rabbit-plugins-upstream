## Description:

Pulls live scores, standings, rosters, player/team stats, and betting odds via the Crawlora API across ESPN, SofaScore, MLB, Strava, and DraftKings Sportsbook, returning clean JSON for sports and athletics research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to retrieve current sports scores, schedules, standings, rosters, player and team statistics, game details, public route or club data, and sportsbook odds through Crawlora-backed API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call non-sports endpoints beyond the skill's sports-research framing.

Mitigation: Review agent-proposed Crawlora paths before execution and keep use to the documented ESPN, SofaScore, MLB, Strava, and DraftKings endpoints.

Risk: The skill requires a Crawlora API key and performs external lookups.

Mitigation: Provide the key through CRAWLORA_API_KEY only, avoid secrets or personal data in request parameters, and do not hardcode or commit the key.

Risk: Live scores, statistics, route data, and odds reflect upstream source availability and update cadence.

Mitigation: Treat responses as current snapshots from their sources, poll live endpoints when freshness matters, and verify high-impact conclusions against the source data.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/sports-scores-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns source-dependent public sports, route, club, and odds data.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
