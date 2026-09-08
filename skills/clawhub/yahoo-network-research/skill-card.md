## Description:

Researches Yahoo's editorial content network -- Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech -- via the Crawlora API, returning clean JSON for feeds, articles, comments, deals, scores, standings, schedules, and related sports data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve normalized JSON from public Yahoo editorial, shopping, news, and sports surfaces through Crawlora endpoints. It supports section digests, article extraction, Yahoo News comment review, shopping deal lookups, and Yahoo Sports scoreboards, standings, schedules, rosters, player data, and event snapshots.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper is intended for Yahoo-focused use but can call unrelated Crawlora endpoints.

Mitigation: Limit usage to the documented Yahoo endpoints and review requested paths before executing the helper.

Risk: The helper can send the Crawlora API key to a configurable API base.

Mitigation: Use the default API base or strictly validate CRAWLORA_API_BASE before providing CRAWLORA_API_KEY.

Risk: Sensitive request data could be sent to the Crawlora service or another configured destination.

Mitigation: Do not run the helper with sensitive request bodies or in environments where CRAWLORA_API_BASE may be set by another party.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora API](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/yahoo-network-research)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, JSON]

**Output Format:** [Markdown guidance with shell commands that return JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and a Crawlora REST request path; endpoint outputs are normalized JSON.]

## Skill Version(s):

1.0.7 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
