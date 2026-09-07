## Description:

Pulls live scores, standings, rosters, player and team stats, betting odds, and endurance-sport route or club data through the Crawlora API and returns structured JSON-oriented results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to answer live sports and athletics questions, including scoreboards, standings, rosters, player statistics, game summaries, play-by-play, head-to-head history, public odds snapshots, and Strava route or club lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The bundled helper can send the Crawlora API key to an overridden API host.

Mitigation: Use a low-privilege Crawlora key and avoid running the helper in environments where CRAWLORA_API_BASE may be controlled by untrusted automation.

Risk: The helper script is broader than the stated sports-data purpose.

Mitigation: Review requests before execution and prefer a release that restricts calls to documented sports endpoints and expected GET methods.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/sports-scores-research)

## Skill Output:

**Output Type(s):** [text, markdown, JSON, shell commands, configuration, guidance]

**Output Format:** [Markdown or text guidance with shell commands and JSON responses from Crawlora endpoints.]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and uses public sports, odds, and route data exposed by the configured Crawlora API endpoint.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
