## Description:

Researches Yahoo's editorial Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech content through Crawlora API endpoints and returns normalized JSON feeds, articles, comments, deals, sports scores, standings, and schedules.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public Yahoo editorial feeds, article bodies, comments, Yahoo Shopping deal/list data, and Yahoo Sports scores, standings, schedules, teams, rosters, players, and event details as JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Crawlora is a third-party API provider and receives the public Yahoo URLs, endpoint choices, and query terms submitted through this skill.

Mitigation: Use the skill only for public Yahoo content research; do not submit private, internal, regulated, or secret-bearing URLs or search terms.

Risk: The skill requires a Crawlora API key, which could be exposed if copied into files, command history, or shared logs.

Mitigation: Keep CRAWLORA_API_KEY in the environment, do not commit or hardcode it, and use the bundled helper so the key is not passed as a command-line argument.

Risk: Yahoo Sports current-snapshot endpoints and story feeds may return time-sensitive public data that changes over time.

Mitigation: Treat returned JSON as a current Yahoo/Crawlora snapshot and verify important time-sensitive facts before relying on them.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API service](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/yahoo-network-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Guidance]

**Output Format:** [Markdown guidance with shell command examples and raw JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses GET requests to documented Crawlora Yahoo endpoints; requires CRAWLORA_API_KEY in the environment.]

## Skill Version(s):

1.0.15 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
