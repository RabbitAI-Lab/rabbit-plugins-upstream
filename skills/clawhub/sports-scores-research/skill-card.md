## Description:

Pulls live scores, standings, rosters, player and team stats, betting odds, and endurance-sport route or club data through Crawlora API endpoints and returns clean JSON-oriented results.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to answer sports and athletics questions that need current scores, schedules, standings, rosters, player or team statistics, game detail, head-to-head history, betting-odds snapshots, or Strava route and club lookups.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper can make broad Crawlora API calls beyond the sports examples.

Mitigation: Review the requested endpoint and parameters before running commands, and limit use to the sports-data calls needed for the task.

Risk: An overridden CRAWLORA_API_BASE could receive the Crawlora API key.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is trusted, and keep CRAWLORA_API_KEY in secret storage.

Risk: Prompts, proprietary data, or secrets passed in query parameters or JSON bodies may be sent to the API provider.

Mitigation: Use only public or non-sensitive inputs when constructing requests.

## Reference(s):

- [sports-scores-research endpoint reference](reference/endpoints.md)
- [Crawlora documentation](https://crawlora.net/docs?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)
- [Crawlora playground](https://crawlora.net/playground?utm_source=github&utm_medium=referral&utm_campaign=crawlora-skills)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, json, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; live data freshness depends on upstream sports-data providers.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
