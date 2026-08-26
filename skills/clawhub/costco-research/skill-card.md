## Description:

Researches Costco products, categories, warehouse stock/availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users and developers use this skill to research Costco products, compare category results, check warehouse or delivery availability, find nearby warehouses, and summarize product reviews through documented Crawlora API endpoints.

### Deployment Geography for Use:

United States for delivery availability; Global for general public Costco product research where Crawlora and Costco data access are available.

## Known Risks and Mitigations:

Risk: The included helper can call broader Crawlora endpoints beyond the documented Costco endpoints when given arbitrary paths.

Mitigation: Review calls before execution and prefer only the documented /costco/* endpoints.

Risk: Costco search terms and location-related inputs are sent to Crawlora for API-backed research.

Mitigation: Use the skill only when that data sharing is acceptable and do not pass secrets or unrelated prompt content through the helper.

Risk: Live Costco availability and delivery estimates may change after retrieval.

Mitigation: Treat returned stock and delivery data as point-in-time research and recheck before purchase decisions.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/costco-research)
- [Crawlora API](https://api.crawlora.net/api/v1)
- [Crawlora](https://crawlora.net)

## Skill Output:

**Output Type(s):** [text, markdown, shell commands, configuration, guidance]

**Output Format:** [Markdown guidance with shell commands and JSON API responses]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY for live Crawlora API calls; Costco delivery availability requires a US postal code and state.]

## Skill Version(s):

1.0.4 (source: ClawHub release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
