## Description:

Pulls live scores, standings, rosters, player/team stats, and betting odds via the Crawlora API for ESPN, SofaScore, MLB, Strava, DraftKings Sportsbook, and documented Cricinfo endpoints, returning clean JSON for sports research tasks.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and sports analysts use this skill to retrieve current public sports data, team and player stats, standings, rosters, play-by-play details, route and club data, and sportsbook odds through Crawlora API calls.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Sports queries, IDs, and provided public sports-page URLs are sent to Crawlora with the user's Crawlora API key.

Mitigation: Use only public sports data, avoid private or internal URLs, secrets, and personal data, and install only when this third-party request sharing is acceptable.

Risk: The security evidence notes disclosure gaps around Cricinfo support and third-party request sharing.

Mitigation: Review the endpoint reference before use, disclose Cricinfo-backed behavior where relevant, and make privacy expectations clear to users.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/sports-scores-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)
- [Endpoint reference](reference/endpoints.md)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [Crawlora documentation](https://crawlora.net/docs)
- [Crawlora playground](https://crawlora.net/playground)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a CRAWLORA_API_KEY environment variable and returns public sports data from supported Crawlora endpoints.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
