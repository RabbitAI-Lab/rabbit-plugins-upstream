## Description:

Researches Costco products, categories, warehouse stock/availability, and reviews using the Crawlora API, returning clean JSON.

This skill is ready for commercial/non-commercial use.

## Publisher:

[tonywangcn](https://clawhub.ai/user/tonywangcn)

### License/Terms of Use:

MIT-0

## Use Case:

External users, developers, and shopping researchers use this skill to find Costco products, compare categories, check product details, review ratings, verify US delivery availability, and locate nearby warehouses through Crawlora instead of scraping Costco.com.

### Deployment Geography for Use:

Global, with Costco delivery availability limited to US ZIP and state destinations.

## Known Risks and Mitigations:

Risk: The bundled helper can call non-Costco Crawlora endpoints with arbitrary request bodies.

Mitigation: Review the requested endpoint before execution and restrict normal use to the documented /costco/* endpoints unless broader Crawlora access is intentionally approved.

Risk: The skill requires a Crawlora API key and sends lookup requests to a third-party service.

Mitigation: Provide the key only through CRAWLORA_API_KEY, avoid logging or sharing it, and review the data being sent before making requests.

Risk: Warehouse lookups may require precise latitude and longitude.

Mitigation: Use ZIP and state for availability checks when possible, and provide coordinates only when the warehouse endpoint is needed.

Risk: Costco price, stock, delivery, and review data may change after an API lookup.

Mitigation: Verify important purchase decisions against the current Costco listing or checkout flow before acting on the result.

## Reference(s):

- [Endpoint reference](reference/endpoints.md)
- [Crawlora](https://crawlora.net)
- [ClawHub skill page](https://clawhub.ai/tonywangcn/skills/costco-research)

## Skill Output:

**Output Type(s):** [JSON, Shell commands, Configuration, Guidance]

**Output Format:** [JSON API responses with Markdown guidance and inline shell commands]

**Output Parameters:** [1D]

**Other Properties Related to Output:** [Requires CRAWLORA_API_KEY; availability lookups require US postal_code and state; warehouse lookup requires latitude and longitude.]

## Skill Version(s):

1.0.1 (source: server release evidence)

## Ethical Considerations:

Users should evaluate whether this skill is appropriate for their environment, review any generated or modified files before relying on them, and apply their organization's safety, security, and compliance requirements before deployment.
