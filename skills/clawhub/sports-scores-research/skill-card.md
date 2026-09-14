## Description:

Pulls live sports scores, standings, rosters, player and team stats, betting odds, and endurance-sport route or club data from the Crawlora API as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve current public sports data for scoreboards, standings, rosters, player or team statistics, game summaries, head-to-head context, sportsbook odds snapshots, and Strava route or club lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports queries, URLs, and identifiers are sent to Crawlora under the user's Crawlora API key.

Mitigation: Do not pass private or sensitive data as parameters, and confirm that sending the requested sports data to Crawlora is acceptable before use.

Risk: The skill includes Cricinfo endpoints even though the main description focuses on ESPN, SofaScore, MLB, Strava, and DraftKings.

Mitigation: Review the endpoint reference and helper route list before using cricket-related endpoints.

Risk: Betting odds data can be mistaken for betting advice or a betting service.

Mitigation: Treat odds as informational snapshots and verify any legal, compliance, or policy requirements before using them in user-facing workflows.

## Reference(s):

- [sports-scores-research ClawHub page](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends user-directed sports queries, URLs, and identifiers to Crawlora.]

## Skill Version(s):

1.0.16 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
