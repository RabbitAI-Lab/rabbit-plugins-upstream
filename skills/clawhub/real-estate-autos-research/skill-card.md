## Description:

Researches homes and used cars via the Crawlora API, including Zillow and Redfin property search, estimates, and market trends, plus CarMax, Autotrader, and Cars.com vehicle search and dealer or listing detail, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and agents use this skill to research public real-estate and used-car listings, property estimates, market trends, comparable properties, vehicle listings, and dealer or listing detail through documented Crawlora endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script can call Crawlora API endpoints outside the real-estate and used-car research scope.

Mitigation: Use only the documented Zillow, Redfin, CarMax, Autotrader, and Cars.com endpoints unless the caller has reviewed and approved additional Crawlora paths.

Risk: The skill requires a Crawlora API key and outbound Crawlora requests.

Mitigation: Store the key only in CRAWLORA_API_KEY, avoid hardcoding or committing it, and install the skill only when that external API access is acceptable.

Risk: Property estimates, market trends, vehicle pricing, and listing data can be stale, incomplete, or unsuitable for financial decisions.

Mitigation: Treat returned data as public listing research and verify important decisions with authoritative sources or qualified professionals.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/real-estate-autos-research)
- [Publisher profile](https://clawhub.ai/user/tonywangcn)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires a Crawlora API key in CRAWLORA_API_KEY and outbound HTTPS requests to Crawlora.]

## Skill Version(s):

1.0.5 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
