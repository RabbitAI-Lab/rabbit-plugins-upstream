## Description:

Pulls live scores, standings, rosters, and player/team stats through the Crawlora API for ESPN, SofaScore, MLB, and Strava, returning clean JSON for scoreboard, standings, roster, boxscore, play-by-play, head-to-head, and endurance-sport route or club requests.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and agents use this skill to retrieve current public sports scores, standings, rosters, player or team statistics, game details, and Strava route or club data through Crawlora-backed endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled Crawlora helper can call non-sports endpoints, so use may exceed a reader's expectation of a sports-only skill.

Mitigation: Review the skill before installation and limit operational use to the documented ESPN, SofaScore, MLB, and Strava sports endpoints unless broader Crawlora access is intended.

Risk: The skill requires a Crawlora API key and sends requests to Crawlora.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid committing it, and review outbound API use for the intended environment.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live Crawlora API calls.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
