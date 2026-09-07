## Description:

Researches video games via the Crawlora API, covering Steam store pages, pricing, reviews, player counts, charts, tags, achievements, and PlayStation Store products, categories, and deals as clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and external users use this skill to research game listings, prices, reviews, live player counts, trending charts, sale opportunities, and platform-specific store details across Steam and PlayStation.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The packaged helper can call broader Crawlora API paths than the advertised Steam and PlayStation research endpoints.

Mitigation: Review commands before execution and restrict use to the documented gaming endpoints unless a trusted operator intentionally approves other Crawlora paths.

Risk: The API base can be overridden with CRAWLORA_API_BASE, which could send the Crawlora API key to an untrusted destination.

Mitigation: Do not set CRAWLORA_API_BASE unless the destination is trusted; prefer the default Crawlora API base.

Risk: The skill requires a Crawlora API key for live requests.

Mitigation: Store the key only in CRAWLORA_API_KEY and avoid hardcoding, committing, or passing it in query parameters.

## Reference(s):

- [Endpoint Reference](reference/endpoints.md)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)
- [ClawHub Skill Page](https://clawhub.ai/tonywangcn/skills/gaming-research)

## Skill Output:

**Output Type(s):** [text, markdown, code, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API results]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Uses Crawlora API responses; requires CRAWLORA_API_KEY for live requests.]

## Skill Version(s):

1.0.8 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
