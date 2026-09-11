## Description:

Researches Yahoo Autos, Entertainment, Health, Life, News, Shopping, Sports, and Tech content through the Crawlora API and returns clean JSON for feeds, articles, comments, deals, scores, standings, schedules, teams, players, and related sports data.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and agents use this skill to retrieve public Yahoo network story feeds, full article text, Yahoo News comments, Yahoo Shopping deals, and Yahoo Sports snapshots through documented Crawlora endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Requests may send Yahoo article URLs, categories, search text, comment IDs, and POST body content to Crawlora.

Mitigation: Use the skill only for Yahoo content the user is comfortable sending to Crawlora, and avoid private or sensitive data.

Risk: The Crawlora API key could be exposed if hardcoded, committed, or passed directly in command arguments.

Mitigation: Keep the key in CRAWLORA_API_KEY and use the helper's environment-based API key handling.

## Reference(s):

- [Yahoo network endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/crawlora-org/skills/yahoo-network-research)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, JSON, shell commands, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and returns public Yahoo network data from documented Crawlora endpoints.]

## Skill Version(s):

1.0.13 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
