## Description:

Pulls live scores, standings, rosters, player/team stats, and betting odds via the Crawlora API - ESPN (most sports/leagues), SofaScore (global soccer + more), MLB's own stats API, Strava (routes, clubs, challenges), and DraftKings Sportsbook (moneyline/spread/total odds, futures, live events) - returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current sports scores, standings, rosters, player and team statistics, game details, public route or club information, and sportsbook odds as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora receives the API key-authenticated sports queries and some source URLs submitted through the helper.

Mitigation: Install only when this data sharing is acceptable, keep CRAWLORA_API_KEY in the environment, and avoid submitting sensitive or private source URLs.

Risk: Cricinfo cricket endpoints are available in the route catalog but are not highlighted in the main description.

Mitigation: Review reference/endpoints.md before deployment so users understand the complete documented endpoint surface.

Risk: Live scores and odds reflect upstream source availability and update cadence.

Mitigation: Poll relevant endpoints and treat odds as informational rather than as betting advice or a transaction service.

## Reference(s):

- [sports-scores-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora documentation](https://crawlora.net/docs)
- [Crawlora playground](https://crawlora.net/playground)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands that return JSON from the Crawlora API]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; helper requests are GET-only and limited to the documented route catalog.]

## Skill Version(s):

1.0.17 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
