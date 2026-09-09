## Description:

Researches video games via the Crawlora API — Steam (store pages, pricing, reviews, player counts, charts, tags, achievements) and PlayStation Store (products, categories, deals) — returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

Developers, analysts, and external agents use this skill to research public game-store listings, prices, reviews, player counts, charts, tags, achievements, and deals across Steam, PlayStation Store, and referenced Roblox endpoints.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: The helper script is broader than the advertised game-research workflow and may call Crawlora endpoints outside the gaming use case.

Mitigation: Review proposed endpoint paths before execution and limit use to documented game-store endpoints unless the user explicitly approves broader Crawlora calls.

Risk: Setting CRAWLORA_API_BASE can send the Crawlora API key to a different server.

Mitigation: Leave CRAWLORA_API_BASE unset unless the destination is trusted, and use a limited, revocable Crawlora API key.

Risk: Requests may include user-provided terms or identifiers that are sent to the Crawlora API.

Mitigation: Avoid sending private or sensitive data in game research requests.

## Reference(s):

- [Endpoint reference](artifact/reference/endpoints.md)
- [Gaming Research ClawHub listing](https://clawhub.ai/tonywangcn/skills/gaming-research)
- [Crawlora](https://crawlora.net)
- [Crawlora API base](https://api.crawlora.net/api/v1)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, JSON]

**Output Format:** [Markdown guidance with shell command examples and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; accepts endpoint paths, query parameters, optional POST bodies, and optional CRAWLORA_API_BASE override.]

## Skill Version(s):

1.0.9 (source: server release metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
