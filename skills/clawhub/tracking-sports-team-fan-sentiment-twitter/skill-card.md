## Description:

Tracks sports team fan sentiment on Twitter using apidojo's Tweet scraper, returning sentiment distribution, volume trends, top fan reactions, topic themes, and event-triggered spikes.

This skill is ready for commercial/non-commercial use.

## Publisher:

[apidojo-io](https://clawhub.ai/user/apidojo-io)

### License/Terms of Use:

MIT-0

## Use Case:

External sports marketing teams, brand sponsors, sports analytics firms, and sports media teams use this skill to monitor Twitter reactions to sports teams, games, player news, and events.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Search terms and resulting tweet data may be sent to Apify or Twitter scraping infrastructure.

Mitigation: Use the skill only when that data sharing is acceptable for the use case, and avoid submitting sensitive or private search terms.

Risk: Unsafe request examples can expose an Apify API token when tokens are placed in URLs.

Mitigation: Treat APIFY_TOKEN as a secret and prefer SDK-based or Authorization-header authentication instead of URL token parameters.

Risk: Unbounded tweet collection can increase cost and data volume.

Mitigation: Set explicit result limits such as maxItems before running the scraper.

## Reference(s):

- [ClawHub skill page](https://clawhub.ai/apidojo-io/skills/tracking-sports-team-fan-sentiment-twitter)
- [Apify tweet-scraper actor run API](https://api.apify.com/v2/acts/apidojo~tweet-scraper/runs)
- [Apify actor run dataset items API](https://api.apify.com/v2/actor-runs/$RUN_ID/dataset/items)

## Skill Output:

**Output Type(s):** [Text, Markdown, Shell commands, Configuration, Guidance]

**Output Format:** [Markdown tables and summaries with optional JSON or CSV data files]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Includes sentiment classifications, fan sentiment scores, volume trends, topic themes, top reactions, and event context.]

## Skill Version(s):

1.0.0 (source: release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
