## Description:

Use when users need product search and price evidence, product details, public store analysis, or keyword-based ecommerce competition reports through Commerce Radar; requires COMMERCE_RADAR_API_KEY.

This skill is ready for commercial/non-commercial use.

## Publisher:

[youteacher](https://clawhub.ai/user/youteacher)

### License/Terms of Use:

MIT-0

## Use Case:

Developers and analysts use this skill to query Commerce Radar for product listings, product details, public store summaries, and keyword competition reports. It helps preserve source URLs, observed prices, task status, artifacts, and billing headers from the Commerce Radar API response.

### Deployment Geography for Use:

Global

## Known Risks and Mitigations:

Risk: Commerce queries, public product or store URLs, location or language parameters, and report inputs are sent to the configured Commerce Radar API endpoint.

Mitigation: Install and use the skill only when this data sharing is intended, and keep requests limited to the documented Commerce Radar operations and fields.

Risk: The Commerce Radar API key could be exposed if pasted into chat, request bodies, logs, results, or artifacts.

Mitigation: Store COMMERCE_RADAR_API_KEY in the environment, send it only as an Authorization bearer token, and never echo the full value.

Risk: Product, store, and report results may be partial, pending, stale, or unavailable, and observed prices may not remain valid.

Mitigation: Present returned data as time-bound observations, preserve source URLs and task status, and avoid inferring inventory, sales, long-term prices, or factual absence from empty or pending results.

Risk: Unsafe or unsupported URLs could route requests outside the intended public ecommerce targets.

Mitigation: Accept only public HTTP(S) product and store URLs, reject loopback, private-network, localhost, credential-bearing, and non-web URLs, and do not scrape or call third-party providers directly.

## Reference(s):

- [API Key Configuration](artifact/references/API-KEY.md)
- [Operations Contract](artifact/references/OPERATIONS.md)
- [HTTP Requests and Task Polling](artifact/references/HTTP-REQUESTS.md)
- [Behavior and Error Rules](artifact/references/BEHAVIOR-RULES.md)
- [AI Skills Homepage](https://ai-skills.open-idea.net)
- [ClawHub Skill Page](https://clawhub.ai/youteacher/skills/commerce-radar)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and structured API response summaries]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Outputs should distinguish observed provider results from facts, preserve source URLs and task identifiers, and avoid exposing the API key.]

## Skill Version(s):

1.0.0 (source: server release evidence and packageVersion metadata)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
