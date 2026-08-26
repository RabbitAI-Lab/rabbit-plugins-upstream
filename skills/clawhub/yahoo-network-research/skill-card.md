## Description:

Researches Yahoo's editorial content network across Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech via the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to fetch Yahoo editorial feeds, article bodies, news comments, shopping deal lists, and sports scores, standings, schedules, rosters, and leaderboards as JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora endpoints outside the Yahoo-only purpose and can send arbitrary request bodies.

Mitigation: Review requested endpoint paths and request bodies before execution, and restrict use to trusted prompts and the documented Yahoo endpoints.

Risk: Queries, URLs, identifiers, and request bodies are sent to Crawlora.

Mitigation: Do not submit sensitive or private data unless sharing it with Crawlora is acceptable for the deployment.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/yahoo-network-research)

## Skill Output:

**Output Type(s):** [text, json, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; API responses are public Yahoo network data returned through Crawlora.]

## Skill Version(s):

1.0.3 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
