## Description:

Pulls live scores, standings, rosters, and player/team stats via the Crawlora API - ESPN, SofaScore, MLB, and Strava - returning clean JSON for sports and endurance-sport research.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and analysts use this skill to retrieve current sports scores, standings, rosters, player and team statistics, game summaries, play-by-play data, and public Strava route or club information.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call arbitrary Crawlora API paths, including unrelated services, with arbitrary request bodies.

Mitigation: Use it only with the documented ESPN, SofaScore, MLB, and Strava endpoints, or restrict or replace it with an allowlisted sports-only wrapper.

Risk: The skill uses a Crawlora API key and may send request bodies to the Crawlora API.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid passing private data in request bodies.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API docs](https://crawlora.net/docs)
- [Crawlora playground](https://crawlora.net/playground)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/sports-scores-research)

## Skill Output:

**Output Type(s):** [text, markdown, json, shell commands, configuration, guidance]

**Output Format:** [JSON responses with concise Markdown guidance and shell command examples]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public sports or activity-platform data from supported endpoints.]

## Skill Version(s):

1.0.2 (source: ClawHub release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
