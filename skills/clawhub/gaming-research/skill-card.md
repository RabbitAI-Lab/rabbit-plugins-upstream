## Description:

Researches video games via the Crawlora API: Steam store pages, pricing, reviews, player counts, charts, tags, and achievements; PlayStation Store products, categories, and deals; and public Roblox game endpoints.

This skill is ready for commercial/non-commercial use.

## Publisher:

[crawlora-org](https://clawhub.ai/user/crawlora-org)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to retrieve public game store, review, pricing, player-count, chart, tag, achievement, deal, and catalog data as normalized JSON through Crawlora.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Game queries and the Crawlora API key are sent to Crawlora.

Mitigation: Avoid private information in search terms and provide the key only through CRAWLORA_API_KEY.

Risk: The artifact includes Roblox public-data endpoints although the main description highlights Steam and PlayStation.

Mitigation: Review endpoint coverage before deployment and tell users that Roblox public game endpoints are also available.

## Reference(s):

- [gaming-research endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY and sends game queries to Crawlora.]

## Skill Version(s):

1.0.17 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
