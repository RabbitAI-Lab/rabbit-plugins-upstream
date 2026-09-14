## Description:

Yahoo Network Research helps agents retrieve normalized JSON for Yahoo Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech feeds, articles, comments, deals, scores, schedules, standings, and related public content through the Crawlora API.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and research agents use this skill to fetch public Yahoo editorial feeds, article content, reader comments, shopping deal lists, and sports data snapshots through Crawlora for summarization and analysis.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests go to Crawlora and may include Yahoo article URLs, sports identifiers, comment IDs, or search text supplied by the user.

Mitigation: Keep CRAWLORA_API_KEY in the environment, avoid sending private or sensitive URLs or text, and use the included helper for documented Yahoo routes.

Risk: Some Yahoo Sports endpoints return Yahoo's current or next public snapshot rather than a caller-selected historical edition.

Mitigation: Check endpoint parameters before relying on time-sensitive sports results, schedules, rankings, fight cards, or medal counts.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/yahoo-network-research)
- [Crawlora publisher profile](https://clawhub.ai/user/crawlora-org)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and routes requests through the documented Yahoo endpoints exposed by Crawlora.]

## Skill Version(s):

1.0.14 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
